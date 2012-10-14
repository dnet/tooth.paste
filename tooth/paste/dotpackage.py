"""
Implement the basic namespace support for tooth.paste, based on Templer.
"""
import copy
from paste.script import templates
from templer.core.basic_namespace import BasicNamespace
from tooth.paste.invisible import add_invisible_vars


# pylint: disable=R0904
class DotPackage(BasicNamespace):
    """
    This creates a basic name space Python package with one dot in the name.
    Adds invisible variables to be used by the template system.
    """
    _template_dir = 'templates/dotpackage'
    summary = "A basic namespace Python package (1 dot in name)"
    help = """
This creates a basic namespace Python package with one dot in the name.
"""
    required_templates = []
    use_cheetah = True

    vars = copy.deepcopy(BasicNamespace.vars)

    def check_vars(self, myvars, cmd):
        myvars = super(DotPackage, self).check_vars(myvars, cmd)
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
        super(DotPackage, self).pre(command, output_dir, vars)

    def run(self, command, output_dir, vars):
        templates.Template.run(self, command, output_dir, vars)
