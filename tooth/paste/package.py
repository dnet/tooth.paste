"""
Implement the package support for tooth.paste, based on Templer.
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

    def __str__(self):
        return self.default


# pylint: disable=R0904
class Package(BasicNamespace):
    """
    This creates a Python package.
    Adds invisible variables to be used by the template system.
    """
    _template_dir = 'templates/package'
    summary = "A basic namespace Python package (1 dot in name)"
    ndots = 0
    help = """
This creates a basic namespace Python package with one dot in the name.
"""
    required_templates = []
    use_cheetah = True

    def check_vars(self, myvars, cmd):
        myvars = super(Package, self).check_vars(myvars, cmd)
        myvars['travisci'] = InvisibleStringVar(
            'travisci',
            title='Travis-CI',
            description='Travis-Ci',
            default='.travis.ci',
            modes=(EASY, EXPERT),
            page='Metadata',
            help="""
Travis-CI
""")

        myvars['travisci_user'] = InvisibleStringVar(
            'travisci_user',
            title='Travis-CI User',
            description='Travis-CI User',
            modes=(EASY, EXPERT),
            page='Metadata',
            help="""
Travis-CI URL
""")

        myvars['travisci_project'] = InvisibleStringVar(
            'travisci_project',
            title='Travis-CI Project',
            description='Travis-CI Project',
            default=os.environ.get('USER', 'travisci_project'),
            modes=(EASY, EXPERT),
            page='Metadata',
            help="""
Travis-CI Project
""")

        info = (myvars['travisci_user'], myvars['travisci_project'])
        myvars['travisci_url'] = InvisibleStringVar(
            'travisci_url',
            title='Travis-CI URL',
            description='Travis-CI URL',
            default="https://secure.travis-ci.org/%s/%s" % info,
            modes=(EASY, EXPERT),
            page='Metadata',
            help="""
Travis-CI URL
""")

        myvars['documentation_url'] = InvisibleStringVar(
            'documentation_url',
            title='documentation_url',
            description='documentation_url',
            default="",
            modes=(EASY, EXPERT),
            page='Metadata',
            help="""
documentation_url
""")

        myvars['repository_url'] = InvisibleStringVar(
            'repository_url',
            title='repository_url',
            description='repository_url',
            default="",
            modes=(EASY, EXPERT),
            page='Metadata',
            help="""
repository_url
""")

        myvars['zopeskel'] = InvisibleStringVar(
            'zopeskel',
            title='ZopeSkel',
            description='ZopeSkel',
            default='.zopeskel',
            modes=(EASY, EXPERT),
            page='Metadata',
            help="""
ZopeSkel
""")
        return myvars
