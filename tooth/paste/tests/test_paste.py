"""
Unit tests for the tooth.paste Python module.
"""
from tooth.paste.tooth_basic_namespace import ToothBasicNamespace
from tooth.paste.tooth_basic_namespace import InvisibleStringVar

try:
    import unittest2 as unittest
except ImportError:
    import unittest  # NOQA


class TestToothBasicNamespace(unittest.TestCase):
    """
    Unit test for the ToothBasicNamespace class.
    """

    def test_repr_without_default(self):
        tooth = ToothBasicNamespace('name')
        template_dir = 'templates/tooth_nested_namespace'
        self.failUnless(tooth._template_dir == template_dir)
        self.failUnless(tooth.summary == "A custom basic Python project")
        self.failUnless(tooth.help == """
This creates a Tooth Python project.
""")
        self.failUnless(tooth.required_templates == [])
        self.failUnless(tooth.use_cheetah == True)

    def test_check_vars(self):
        class DummyOptions:
            options = []
            templates = []
            no_interactive = True
        class DummyCmd:
            _deleted_once = 0
            options = DummyOptions
            interactive = False
        cmd = DummyCmd()
        tooth = ToothBasicNamespace('name')
        vars = {'project':'project'}
        tooth.check_vars(vars, cmd)
        

class TestInvisibleStringVar(unittest.TestCase):
    """
    Unit test for the InvisibleStringVar class.
    """

    def test_repr_without_default(self):
        invisible = InvisibleStringVar('name', 'description')
        self.failUnless(invisible.__repr__() == '')

    def test_repr_with_default(self):
        invisible = InvisibleStringVar('name', 'description', default="default")
        self.failUnless(invisible.__repr__() == 'default')
