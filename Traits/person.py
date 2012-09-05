""" Illustrates the simplicity of TraitsUI and a couple of concepts you gain 
with going with traits:
- type validation 
- listeners
- multiple views on a model
"""

from traits.api import HasTraits, Range, Str, Enum

class Person(HasTraits):
    """
    """
    first = Str
    last = Str
    age = Range(1, 99)
    gender = Enum("male", "female")
    

def print_value(value):
    print value
    
if __name__ == "__main__":
    p = Person(first = "Eric", last = "Jones")
    p.edit_traits()
    p.age = 10
    p.on_trait_change(print_value, name = "age")
    p.age = 55
    
    from traitsui.api import Item, View
    v = View(Item("age"), Item("first"))
    p.edit_traits(v)
    p.age = 75
    p.age = 100