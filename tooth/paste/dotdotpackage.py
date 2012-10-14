"""
Implement the nested namespace support for tooth.paste, based on Templer.
"""
import copy
from paste.script import templates
from tooth.paste.invisible import add_invisible_vars
from templer.core.basic_namespace import BasicNamespace
from templer.core.base import get_var


# pylint: disable=R0904
class DotDotPackage(BasicNamespace):
    """
    This creates a nested namespace Python package with two dots in the name.
    """
    _template_dir = 'templates/dotdotpackage'
    summary = "A nested namespace Python package (2 dots in name)"
    help = """
This creates a nested namespace Python package with two dots in the name.
"""
    required_templates = []
    use_cheetah = True

    vars = copy.deepcopy(BasicNamespace.vars)
    get_var(vars, 'package').default = 'example'

    def check_vars(self, myvars, cmd):
        myvars = super(DotDotPackage, self).check_vars(myvars, cmd)
        add_invisible_vars(myvars)
        return myvars

    def pre(self, command, output_dir, vars):
        if '.' in vars['egg']:
            # Taken from http://code.google.com/p/wsgitemplates/
            namespace = []
            for i in range(len(vars['egg'].split('.')) - 1):
                namespace.append(".".join(vars['egg'].split('.')[0:i+1]))
            vars['namespace'] = "\n      namespace_packages=%s," % namespace
        else:
           vars['namespace'] = ""
        super(DotDotPackage, self).pre(command, output_dir, vars)

    def run(self, command, output_dir, vars):
        templates.Template.run(self, command, output_dir, vars)
