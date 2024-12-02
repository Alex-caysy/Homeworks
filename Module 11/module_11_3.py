import inspect
import sys
from pprint import pprint
import test_func as test


def introspection_info(obj):
    print(f'\n {obj}')
    introspection_dict = dict()
    introspection_dict['type'] = obj.__class__.__qualname__
    list_of_methods = []
    list_of_attrs = []
    for attr in dir(obj):
        if callable(getattr(obj, attr)):
            list_of_methods.append(attr)
        else:
            list_of_attrs.append(attr)

    introspection_dict['attributes'] = list_of_attrs
    introspection_dict['methods'] = list_of_methods
    introspection_dict['module'] = (getattr(obj, '__module__', '__main__'))
    introspection_dict['platform'] = sys.platform

    return introspection_dict


my_object = test.MyClass(46)
oject_info = introspection_info(my_object)
pprint(oject_info)

number_info = introspection_info(42)
pprint(number_info)

pprint(introspection_info(test.my_obj))

pprint(introspection_info(test.func_summ))

print(inspect.getsourcelines(test.MyClass.attr_plus_two))
print(inspect.getsource(test.MyClass.attr_plus_two))
