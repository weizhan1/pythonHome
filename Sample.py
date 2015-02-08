O(n) is worse than O(1):

d = {1: 'a', 2: 'b', 3: 'c'}


def safe_get(d, key, value):
    if key in d.keys():
        return d[key]
    return value

print safe_get(d, 0, 'blah')

funcs = []
for i in range(5):
    def f():
        print i
    funcs.append(f)

for f in funcs:
    f()
    

funcs = []
for i in range(5):
    def f(i=i):
        print i
    funcs.append(f)

for f in funcs:
    f()    
    
def f(names=[]):
    names.append('some name')
    
    
>>> def choose_class(name):
...     if name == 'foo':
...         class Foo(object):
...             pass
...         return Foo # return the class, not an instance
...     else:
...         class Bar(object):
...             pass
...         return Bar
...     
>>> MyClass = choose_class('foo') 
>>> print(MyClass) # the function returns a class, not an instance
<class '__main__.Foo'>
>>> print(MyClass()) # you can create an object from this class
<__main__.Foo object at 0x89c6d4c>

Remember the function type? The good old function that lets you know what type an object is:

>>> print(type(1))
<type 'int'>
>>> print(type("1"))
<type 'str'>
>>> print(type(ObjectCreator))
<type 'type'>
>>> print(type(ObjectCreator()))
<class '__main__.ObjectCreator'>
Well, type has a completely different ability, it can also create classes on the fly. type can take the description of a class as parameters, and return a class.

(I know, it's silly that the same function can have two completely different uses according to the parameters you pass to it. It's an issue due to backwards compatibility in Python)

type works this way:

type(name of the class, 
     tuple of the parent class (for inheritance, can be empty), 
     dictionary containing attributes names and values)
e.g.:

>>> class MyShinyClass(object):
...       pass
can be created manually this way:

>>> MyShinyClass = type('MyShinyClass', (), {}) # returns a class object
>>> print(MyShinyClass)
<class '__main__.MyShinyClass'>
>>> print(MyShinyClass()) # create an instance with the class
<__main__.MyShinyClass object at 0x8997cec>
You'll notice that we use "MyShinyClass" as the name of the class and as the variable to hold the class reference. They can be different, but there is no reason to complicate things.

type accepts a dictionary to define the attributes of the class. So:

>>> class Foo(object):
...       bar = True
Can be translated to:

>>> Foo = type('Foo', (), {'bar':True})
And used as a normal class:

>>> print(Foo)
<class '__main__.Foo'>
>>> print(Foo.bar)
True
>>> f = Foo()
>>> print(f)
<__main__.Foo object at 0x8a9b84c>
>>> print(f.bar)
True
And of course, you can inherit from it, so:

>>>   class FooChild(Foo):
...         pass
would be:

>>> FooChild = type('FooChild', (Foo,), {})
>>> print(FooChild)
<class '__main__.FooChild'>
>>> print(FooChild.bar) # bar is inherited from Foo
True
Eventually you'll want to add methods to your class. Just define a function with the proper signature and assign it as an attribute.

>>> def echo_bar(self):
...       print(self.bar)
... 
>>> FooChild = type('FooChild', (Foo,), {'echo_bar': echo_bar})
>>> hasattr(Foo, 'echo_bar')
False
>>> hasattr(FooChild, 'echo_bar')
True
>>> my_foo = FooChild()
>>> my_foo.echo_bar()
True
You see where we are going: in Python, classes are objects, and you can create a class on the fly, dynamically.

This is what Python does when you use the keyword class, and it does so by using a metaclass.
<__main__.MyShinyClass object at 0x8997cec>
    
    
# the metaclass will automatically get passed the same argument
# that you usually pass to `type`
def upper_attr(future_class_name, future_class_parents, future_class_attr):
  """
    Return a class object, with the list of its attribute turned 
    into uppercase.
  """

  # pick up any attribute that doesn't start with '__' and uppercase it
  uppercase_attr = {}
  for name, val in future_class_attr.items():
      if not name.startswith('__'):
          uppercase_attr[name.upper()] = val
      else:
          uppercase_attr[name] = val

  # let `type` do the class creation
  return type(future_class_name, future_class_parents, uppercase_attr)

__metaclass__ = upper_attr # this will affect all classes in the module

class Foo(): # global __metaclass__ won't work with "object" though
  # but we can define __metaclass__ here instead to affect only this class
  # and this will work with "object" children
  bar = 'bip'

print(hasattr(Foo, 'bar'))
# Out: False
print(hasattr(Foo, 'BAR'))
# Out: True

f = Foo()
print(f.BAR)
# Out: 'bip'

class UpperAttrMetaclass(type): 

    def __new__(cls, clsname, bases, dct):

        uppercase_attr = {}
        for name, val in dct.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val

        return super(UpperAttrMetaclass, cls).__new__(cls, clsname, bases, uppercase_attr)
