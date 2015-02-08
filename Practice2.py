>>> class Class:
...   def one(self):
...     return 1
... 
>>> c=Class()
>>> c.one()
1
>>> def two(self):
...   return 2
... 
>>> Class.two=two
>>> c.two()
2
>>> Class.three=lambda self:3
>>> c.three()
3
>>> Class.one=lambda self:'New One.'
>>> c.one()
'New One.'

>>> def hello_world():
...     pass
... 
>>> hello_world.some_attribute = 'some value'
>>> print hello_world.some_attribute
some value
