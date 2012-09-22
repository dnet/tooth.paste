"""
Implement the nested namespace support for tooth.paste, based on Templer.
"""
import copy

from tooth.paste.basic_namespace import ToothBasicNamespace

from templer.core.base import get_var
from templer.core.nested_namespace import VAR_NS2


class ToothNestedNamespace(ToothBasicNamespace):
    _template_dir = 'templates/nested_namespace'
    summary = "A nested namespace Python package (2 dots in name)"
    ndots = 2
    help = """
This creates a nested namespace Python package with two dots in the name.
"""
    required_templates = []
    use_cheetah = True

    vars = copy.deepcopy(ToothBasicNamespace.vars)
    get_var(vars, 'namespace_package').default = 'my'
    vars.insert(2, VAR_NS2)
    get_var(vars, 'package').default = 'example'
