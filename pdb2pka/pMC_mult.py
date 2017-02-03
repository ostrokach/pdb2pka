# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_pMC_mult', [dirname(__file__)])
        except ImportError:
            import _pMC_mult
            return _pMC_mult
        if fp is not None:
            try:
                _mod = imp.load_module('_pMC_mult', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _pMC_mult = swig_import_helper()
    del swig_import_helper
else:
    import _pMC_mult
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _pMC_mult.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _pMC_mult.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _pMC_mult.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _pMC_mult.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _pMC_mult.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _pMC_mult.SwigPyIterator_equal(self, x)

    def copy(self):
        return _pMC_mult.SwigPyIterator_copy(self)

    def next(self):
        return _pMC_mult.SwigPyIterator_next(self)

    def __next__(self):
        return _pMC_mult.SwigPyIterator___next__(self)

    def previous(self):
        return _pMC_mult.SwigPyIterator_previous(self)

    def advance(self, n):
        return _pMC_mult.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _pMC_mult.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _pMC_mult.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _pMC_mult.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _pMC_mult.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _pMC_mult.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _pMC_mult.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _pMC_mult.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class IntVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, IntVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, IntVector, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _pMC_mult.IntVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _pMC_mult.IntVector___nonzero__(self)

    def __bool__(self):
        return _pMC_mult.IntVector___bool__(self)

    def __len__(self):
        return _pMC_mult.IntVector___len__(self)

    def __getslice__(self, i, j):
        return _pMC_mult.IntVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _pMC_mult.IntVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _pMC_mult.IntVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _pMC_mult.IntVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _pMC_mult.IntVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _pMC_mult.IntVector___setitem__(self, *args)

    def pop(self):
        return _pMC_mult.IntVector_pop(self)

    def append(self, x):
        return _pMC_mult.IntVector_append(self, x)

    def empty(self):
        return _pMC_mult.IntVector_empty(self)

    def size(self):
        return _pMC_mult.IntVector_size(self)

    def swap(self, v):
        return _pMC_mult.IntVector_swap(self, v)

    def begin(self):
        return _pMC_mult.IntVector_begin(self)

    def end(self):
        return _pMC_mult.IntVector_end(self)

    def rbegin(self):
        return _pMC_mult.IntVector_rbegin(self)

    def rend(self):
        return _pMC_mult.IntVector_rend(self)

    def clear(self):
        return _pMC_mult.IntVector_clear(self)

    def get_allocator(self):
        return _pMC_mult.IntVector_get_allocator(self)

    def pop_back(self):
        return _pMC_mult.IntVector_pop_back(self)

    def erase(self, *args):
        return _pMC_mult.IntVector_erase(self, *args)

    def __init__(self, *args):
        this = _pMC_mult.new_IntVector(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def push_back(self, x):
        return _pMC_mult.IntVector_push_back(self, x)

    def front(self):
        return _pMC_mult.IntVector_front(self)

    def back(self):
        return _pMC_mult.IntVector_back(self)

    def assign(self, n, x):
        return _pMC_mult.IntVector_assign(self, n, x)

    def resize(self, *args):
        return _pMC_mult.IntVector_resize(self, *args)

    def insert(self, *args):
        return _pMC_mult.IntVector_insert(self, *args)

    def reserve(self, n):
        return _pMC_mult.IntVector_reserve(self, n)

    def capacity(self):
        return _pMC_mult.IntVector_capacity(self)
    __swig_destroy__ = _pMC_mult.delete_IntVector
    __del__ = lambda self: None
IntVector_swigregister = _pMC_mult.IntVector_swigregister
IntVector_swigregister(IntVector)

class DoubleVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DoubleVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DoubleVector, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _pMC_mult.DoubleVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _pMC_mult.DoubleVector___nonzero__(self)

    def __bool__(self):
        return _pMC_mult.DoubleVector___bool__(self)

    def __len__(self):
        return _pMC_mult.DoubleVector___len__(self)

    def __getslice__(self, i, j):
        return _pMC_mult.DoubleVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _pMC_mult.DoubleVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _pMC_mult.DoubleVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _pMC_mult.DoubleVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _pMC_mult.DoubleVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _pMC_mult.DoubleVector___setitem__(self, *args)

    def pop(self):
        return _pMC_mult.DoubleVector_pop(self)

    def append(self, x):
        return _pMC_mult.DoubleVector_append(self, x)

    def empty(self):
        return _pMC_mult.DoubleVector_empty(self)

    def size(self):
        return _pMC_mult.DoubleVector_size(self)

    def swap(self, v):
        return _pMC_mult.DoubleVector_swap(self, v)

    def begin(self):
        return _pMC_mult.DoubleVector_begin(self)

    def end(self):
        return _pMC_mult.DoubleVector_end(self)

    def rbegin(self):
        return _pMC_mult.DoubleVector_rbegin(self)

    def rend(self):
        return _pMC_mult.DoubleVector_rend(self)

    def clear(self):
        return _pMC_mult.DoubleVector_clear(self)

    def get_allocator(self):
        return _pMC_mult.DoubleVector_get_allocator(self)

    def pop_back(self):
        return _pMC_mult.DoubleVector_pop_back(self)

    def erase(self, *args):
        return _pMC_mult.DoubleVector_erase(self, *args)

    def __init__(self, *args):
        this = _pMC_mult.new_DoubleVector(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def push_back(self, x):
        return _pMC_mult.DoubleVector_push_back(self, x)

    def front(self):
        return _pMC_mult.DoubleVector_front(self)

    def back(self):
        return _pMC_mult.DoubleVector_back(self)

    def assign(self, n, x):
        return _pMC_mult.DoubleVector_assign(self, n, x)

    def resize(self, *args):
        return _pMC_mult.DoubleVector_resize(self, *args)

    def insert(self, *args):
        return _pMC_mult.DoubleVector_insert(self, *args)

    def reserve(self, n):
        return _pMC_mult.DoubleVector_reserve(self, n)

    def capacity(self):
        return _pMC_mult.DoubleVector_capacity(self)
    __swig_destroy__ = _pMC_mult.delete_DoubleVector
    __del__ = lambda self: None
DoubleVector_swigregister = _pMC_mult.DoubleVector_swigregister
DoubleVector_swigregister(DoubleVector)

class FloatVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, FloatVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, FloatVector, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _pMC_mult.FloatVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _pMC_mult.FloatVector___nonzero__(self)

    def __bool__(self):
        return _pMC_mult.FloatVector___bool__(self)

    def __len__(self):
        return _pMC_mult.FloatVector___len__(self)

    def __getslice__(self, i, j):
        return _pMC_mult.FloatVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _pMC_mult.FloatVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _pMC_mult.FloatVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _pMC_mult.FloatVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _pMC_mult.FloatVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _pMC_mult.FloatVector___setitem__(self, *args)

    def pop(self):
        return _pMC_mult.FloatVector_pop(self)

    def append(self, x):
        return _pMC_mult.FloatVector_append(self, x)

    def empty(self):
        return _pMC_mult.FloatVector_empty(self)

    def size(self):
        return _pMC_mult.FloatVector_size(self)

    def swap(self, v):
        return _pMC_mult.FloatVector_swap(self, v)

    def begin(self):
        return _pMC_mult.FloatVector_begin(self)

    def end(self):
        return _pMC_mult.FloatVector_end(self)

    def rbegin(self):
        return _pMC_mult.FloatVector_rbegin(self)

    def rend(self):
        return _pMC_mult.FloatVector_rend(self)

    def clear(self):
        return _pMC_mult.FloatVector_clear(self)

    def get_allocator(self):
        return _pMC_mult.FloatVector_get_allocator(self)

    def pop_back(self):
        return _pMC_mult.FloatVector_pop_back(self)

    def erase(self, *args):
        return _pMC_mult.FloatVector_erase(self, *args)

    def __init__(self, *args):
        this = _pMC_mult.new_FloatVector(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def push_back(self, x):
        return _pMC_mult.FloatVector_push_back(self, x)

    def front(self):
        return _pMC_mult.FloatVector_front(self)

    def back(self):
        return _pMC_mult.FloatVector_back(self)

    def assign(self, n, x):
        return _pMC_mult.FloatVector_assign(self, n, x)

    def resize(self, *args):
        return _pMC_mult.FloatVector_resize(self, *args)

    def insert(self, *args):
        return _pMC_mult.FloatVector_insert(self, *args)

    def reserve(self, n):
        return _pMC_mult.FloatVector_reserve(self, n)

    def capacity(self):
        return _pMC_mult.FloatVector_capacity(self)
    __swig_destroy__ = _pMC_mult.delete_FloatVector
    __del__ = lambda self: None
FloatVector_swigregister = _pMC_mult.FloatVector_swigregister
FloatVector_swigregister(FloatVector)

class MC(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MC, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MC, name)
    __repr__ = _swig_repr

    def __init__(self, intpKas, lin_matrix, ab, num_states, charged_state):
        this = _pMC_mult.new_MC(intpKas, lin_matrix, ab, num_states, charged_state)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def calc_pKas(self, pH_start, pH_end, pH_step):
        return _pMC_mult.MC_calc_pKas(self, pH_start, pH_end, pH_step)

    def set_MCsteps(self, MCsteps):
        return _pMC_mult.MC_set_MCsteps(self, MCsteps)
    __swig_destroy__ = _pMC_mult.delete_MC
    __del__ = lambda self: None
MC_swigregister = _pMC_mult.MC_swigregister
MC_swigregister(MC)

# This file is compatible with both classic and new-style classes.


