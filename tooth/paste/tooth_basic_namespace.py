"""
Implement the basic namespace support for tooth.paste, based on Templer.
"""
import os
from templer.core.basic_namespace import BasicNamespace
from templer.core.vars import StringVar
from templer.core.vars import EASY
from templer.core.vars import EXPERT

class InvisibleStringVar(StringVar):
    """
    A StringVar that is not used for user input, but stored a value for
    use in the templates.
    """
    def __repr__(self):
        return self.default


class ToothBasicNamespace(BasicNamespace):
    """
    Implements the basic name space for tooth.paste, adding a few invisible
    strings that can be caught by the template system.
    """
    _template_dir = 'templates/tooth_nested_namespace'
    summary = "A custom basic Python project"
    help = """
This creates a Tooth Python project.
"""
    required_templates = []
    use_cheetah = True

    def check_vars(self, vars, cmd):
        vars = super(ToothBasicNamespace, self).check_vars(vars, cmd)
        vars['travisci'] =  InvisibleStringVar(
            'travisci',
            title='Travis-CI',
            description='Travis-Ci',
            default='.travis.ci',
            modes=(EASY, EXPERT),
            page='Metadata',
            help="""
Travis-CI
"""
            )

        vars['travisci_user'] =  InvisibleStringVar(
            'travisci_user',
            title='Travis-CI User',
            description='Travis-CI User',
            modes=(EASY, EXPERT),
            page='Metadata',
            help="""
Travis-CI URL
"""
            )

        vars['travisci_project'] =  InvisibleStringVar(
            'travisci_project',
            title='Travis-CI Project',
            description='Travis-CI Project',
            default=os.environ.get('USER', 'travisci_project'),
            modes=(EASY, EXPERT),
            page='Metadata',
            help="""
Travis-CI Project
"""
            )

        info = (vars['travisci_user'], vars['travisci_project'])
        vars['travisci_url'] =  InvisibleStringVar(
            'travisci_url',
            title='Travis-CI URL',
            description='Travis-CI URL',
            default="https://secure.travis-ci.org/%s/%s" % info,
            modes=(EASY, EXPERT),
            page='Metadata',
            help="""
Travis-CI URL
"""
            )

        vars['documentation_url'] =  InvisibleStringVar(
            'documentation_url',
            title='documentation_url',
            description='documentation_url',
            default="",
            modes=(EASY, EXPERT),
            page='Metadata',
            help="""
documentation_url
"""
            )

        vars['repository_url'] =  InvisibleStringVar(
            'repository_url',
            title='repository_url',
            description='repository_url',
            default="",
            modes=(EASY, EXPERT),
            page='Metadata',
            help="""
repository_url
"""
            )

        vars['zopeskel'] =  InvisibleStringVar(
            'zopeskel',
            title='ZopeSkel',
            description='ZopeSkel',
            default='.zopeskel',
            modes=(EASY, EXPERT),
            page='Metadata',
            help="""
ZopeSkel
"""
            )
        return vars
