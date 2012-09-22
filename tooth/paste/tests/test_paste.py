from tooth.paste.tooth_basic_namespace import InvisibleStringVar

try:
    import unittest2 as unittest
except ImportError:
    import unittest  # NOQA

        
class TestInvisibleStringVar(unittest.TestCase):

    def test_repr_without_default(self):
        invisible = InvisibleStringVar('name', 'description')
        self.failUnless(invisible.__repr__() == '')

    def test_repr_with_default(self):
        invisible = InvisibleStringVar('name', 'description', default="default")
        self.failUnless(invisible.__repr__() == 'default')
