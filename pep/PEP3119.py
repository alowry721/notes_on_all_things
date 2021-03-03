""" 
PEP 3119 -- Introducing Abstract Base Classes


 --- A way to overload isinstance() and issubclass(). ---
 
 
 --- A new module abc which serves as an "ABC support framework". It defines a metaclass for
 use with ABCs and a decorator that can be used to define abstract methods. ---
 
 
 --- Specific ABCs for containers and iterators, to be added to the collections module. ---



"""

class ABCMeta(type):
	"""
	A way to overload isinstance() and issubclass().  This is regards how to best determine
	if an object is what it says it is.  
	
	This is meant to solve dilemma between standardizing many fine grained choices or fewer
	coarse grained.  
	"""

    def __instancecheck__(cls, inst):
        """Implement isinstance(inst, cls)."""
        return any(cls.__subclasscheck__(c)
                   for c in {type(inst), inst.__class__})

    def __subclasscheck__(cls, sub):
        """Implement issubclass(sub, cls)."""
        candidates = cls.__dict__.get("__subclass__", set()) | {cls}
        return any(c in candidates for c in sub.mro())

class Sequence(metaclass=ABCMeta):
    __subclass__ = {list, tuple}

assert issubclass(list, Sequence)
assert issubclass(tuple, Sequence)

class AppendableSequence(Sequence):
    __subclass__ = {list}

assert issubclass(list, AppendableSequence)
assert isinstance([], AppendableSequence)

assert not issubclass(tuple, AppendableSequence)
assert not isinstance((), AppendableSequence)
