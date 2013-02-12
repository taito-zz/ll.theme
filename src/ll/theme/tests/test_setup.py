from Products.CMFCore.utils import getToolByName
from ll.theme.tests.base import IntegrationTestCase


class TestCase(IntegrationTestCase):
    """TestCase for Plone setup."""

    def setUp(self):
        self.portal = self.layer['portal']

    def test_installed__package(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.assertTrue(installer.isProductInstalled('ll.theme'))

    def test_browserlayer(self):
        from ll.theme.browser.interfaces import ILlThemeLayer
        from plone.browserlayer import utils
        self.assertIn(ILlThemeLayer, utils.registered_layers())

    def get_css_resource(self, name):
        return getToolByName(self.portal, 'portal_css').getResource(name)

    def test_cssregistry__Montserrat_400_700__title(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Montserrat:400,700')
        self.assertIsNone(resource.getTitle())

    def test_cssregistry__Montserrat_400_700__authenticated(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Montserrat:400,700')
        self.assertFalse(resource.getAuthenticated())

    def test_cssregistry__Montserrat_400_700__cacheable(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Montserrat:400,700')
        self.assertFalse(resource.getCacheable())

    def test_cssregistry__Montserrat_400_700__compression(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Montserrat:400,700')
        self.assertEqual(resource.getCompression(), 'none')

    def test_cssregistry__Montserrat_400_700__conditionalcomment(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Montserrat:400,700')
        self.assertEqual(resource.getConditionalcomment(), '')

    def test_cssregistry__Montserrat_400_700__cookable(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Montserrat:400,700')
        self.assertFalse(resource.getCookable())

    def test_cssregistry__Montserrat_400_700__enabled(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Montserrat:400,700')
        self.assertTrue(resource.getEnabled())

    def test_cssregistry__Montserrat_400_700__expression(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Montserrat:400,700')
        self.assertEqual(resource.getExpression(), '')

    def test_cssregistry__Montserrat_400_700__media(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Montserrat:400,700')
        self.assertEqual(resource.getMedia(), 'screen')

    def test_cssregistry__Montserrat_400_700__rel(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Montserrat:400,700')
        self.assertEqual(resource.getRel(), 'stylesheet')

    def test_cssregistry__Montserrat_400_700__rendering(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Montserrat:400,700')
        self.assertEqual(resource.getRendering(), 'link')

    def test_cssregistry__Montserrat_400_700__applyPrefix(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Montserrat:400,700')
        self.assertTrue(resource.getApplyPrefix())

    def test_cssregistry__Montserrat_Alternates_400_700__title(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Montserrat+Alternates:400,700')
        self.assertIsNone(resource.getTitle())

    def test_cssregistry__Montserrat_Alternates_400_700__authenticated(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Montserrat+Alternates:400,700')
        self.assertFalse(resource.getAuthenticated())

    def test_cssregistry__Montserrat_Alternates_400_700__cacheable(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Montserrat+Alternates:400,700')
        self.assertFalse(resource.getCacheable())

    def test_cssregistry__Montserrat_Alternates_400_700__compression(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Montserrat+Alternates:400,700')
        self.assertEqual(resource.getCompression(), 'none')

    def test_cssregistry__Montserrat_Alternates_400_700__conditionalcomment(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Montserrat+Alternates:400,700')
        self.assertEqual(resource.getConditionalcomment(), '')

    def test_cssregistry__Montserrat_Alternates_400_700__cookable(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Montserrat+Alternates:400,700')
        self.assertFalse(resource.getCookable())

    def test_cssregistry__Montserrat_Alternates_400_700__enabled(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Montserrat+Alternates:400,700')
        self.assertTrue(resource.getEnabled())

    def test_cssregistry__Montserrat_Alternates_400_700__expression(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Montserrat+Alternates:400,700')
        self.assertEqual(resource.getExpression(), '')

    def test_cssregistry__Montserrat_Alternates_400_700__media(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Montserrat+Alternates:400,700')
        self.assertEqual(resource.getMedia(), 'screen')

    def test_cssregistry__Montserrat_Alternates_400_700__rel(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Montserrat+Alternates:400,700')
        self.assertEqual(resource.getRel(), 'stylesheet')

    def test_cssregistry__Montserrat_Alternates_400_700__rendering(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Montserrat+Alternates:400,700')
        self.assertEqual(resource.getRendering(), 'link')

    def test_cssregistry__Montserrat_Alternates_400_700__applyPrefix(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Montserrat+Alternates:400,700')
        self.assertTrue(resource.getApplyPrefix())

    def test_cssregistry__Droid_Sans_400_700__title(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Droid+Sans:400,700')
        self.assertIsNone(resource.getTitle())

    def test_cssregistry__Droid_Sans_400_700__authenticated(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Droid+Sans:400,700')
        self.assertFalse(resource.getAuthenticated())

    def test_cssregistry__Droid_Sans_400_700__cacheable(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Droid+Sans:400,700')
        self.assertFalse(resource.getCacheable())

    def test_cssregistry__Droid_Sans_400_700__compression(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Droid+Sans:400,700')
        self.assertEqual(resource.getCompression(), 'none')

    def test_cssregistry__Droid_Sans_400_700__conditionalcomment(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Droid+Sans:400,700')
        self.assertEqual(resource.getConditionalcomment(), '')

    def test_cssregistry__Droid_Sans_400_700__cookable(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Droid+Sans:400,700')
        self.assertFalse(resource.getCookable())

    def test_cssregistry__Droid_Sans_400_700__enabled(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Droid+Sans:400,700')
        self.assertTrue(resource.getEnabled())

    def test_cssregistry__Droid_Sans_400_700__expression(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Droid+Sans:400,700')
        self.assertEqual(resource.getExpression(), '')

    def test_cssregistry__Droid_Sans_400_700__media(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Droid+Sans:400,700')
        self.assertEqual(resource.getMedia(), 'screen')

    def test_cssregistry__Droid_Sans_400_700__rel(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Droid+Sans:400,700')
        self.assertEqual(resource.getRel(), 'stylesheet')

    def test_cssregistry__Droid_Sans_400_700__rendering(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Droid+Sans:400,700')
        self.assertEqual(resource.getRendering(), 'link')

    def test_cssregistry__Droid_Sans_400_700__applyPrefix(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Droid+Sans:400,700')
        self.assertTrue(resource.getApplyPrefix())

    def test_cssregistry__Droid_Serif_400_700_700italic_400italic__title(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Droid+Serif:400,700,700italic,400italic')
        self.assertIsNone(resource.getTitle())

    def test_cssregistry__Droid_Serif_400_700_700italic_400italic__authenticated(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Droid+Serif:400,700,700italic,400italic')
        self.assertFalse(resource.getAuthenticated())

    def test_cssregistry__Droid_Serif_400_700_700italic_400italic__cacheable(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Droid+Serif:400,700,700italic,400italic')
        self.assertFalse(resource.getCacheable())

    def test_cssregistry__Droid_Serif_400_700_700italic_400italic__compression(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Droid+Serif:400,700,700italic,400italic')
        self.assertEqual(resource.getCompression(), 'none')

    def test_cssregistry__Droid_Serif_400_700_700italic_400italic__conditionalcomment(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Droid+Serif:400,700,700italic,400italic')
        self.assertEqual(resource.getConditionalcomment(), '')

    def test_cssregistry__Droid_Serif_400_700_700italic_400italic__cookable(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Droid+Serif:400,700,700italic,400italic')
        self.assertFalse(resource.getCookable())

    def test_cssregistry__Droid_Serif_400_700_700italic_400italic__enabled(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Droid+Serif:400,700,700italic,400italic')
        self.assertTrue(resource.getEnabled())

    def test_cssregistry__Droid_Serif_400_700_700italic_400italic__expression(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Droid+Serif:400,700,700italic,400italic')
        self.assertEqual(resource.getExpression(), '')

    def test_cssregistry__Droid_Serif_400_700_700italic_400italic__media(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Droid+Serif:400,700,700italic,400italic')
        self.assertEqual(resource.getMedia(), 'screen')

    def test_cssregistry__Droid_Serif_400_700_700italic_400italic__rel(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Droid+Serif:400,700,700italic,400italic')
        self.assertEqual(resource.getRel(), 'stylesheet')

    def test_cssregistry__Droid_Serif_400_700_700italic_400italic__rendering(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Droid+Serif:400,700,700italic,400italic')
        self.assertEqual(resource.getRendering(), 'link')

    def test_cssregistry__Droid_Serif_400_700_700italic_400italic__applyPrefix(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Droid+Serif:400,700,700italic,400italic')
        self.assertTrue(resource.getApplyPrefix())

    def test_cssregistry__Archivo_Black__title(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Archivo+Black')
        self.assertIsNone(resource.getTitle())

    def test_cssregistry__Archivo_Black__authenticated(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Archivo+Black')
        self.assertFalse(resource.getAuthenticated())

    def test_cssregistry__Archivo_Black__cacheable(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Archivo+Black')
        self.assertFalse(resource.getCacheable())

    def test_cssregistry__Archivo_Black__compression(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Archivo+Black')
        self.assertEqual(resource.getCompression(), 'none')

    def test_cssregistry__Archivo_Black__conditionalcomment(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Archivo+Black')
        self.assertEqual(resource.getConditionalcomment(), '')

    def test_cssregistry__Archivo_Black__cookable(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Archivo+Black')
        self.assertFalse(resource.getCookable())

    def test_cssregistry__Archivo_Black__enabled(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Archivo+Black')
        self.assertTrue(resource.getEnabled())

    def test_cssregistry__Archivo_Black__expression(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Archivo+Black')
        self.assertEqual(resource.getExpression(), '')

    def test_cssregistry__Archivo_Black__media(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Archivo+Black')
        self.assertEqual(resource.getMedia(), 'screen')

    def test_cssregistry__Archivo_Black__rel(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Archivo+Black')
        self.assertEqual(resource.getRel(), 'stylesheet')

    def test_cssregistry__Archivo_Black__rendering(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Archivo+Black')
        self.assertEqual(resource.getRendering(), 'link')

    def test_cssregistry__Archivo_Black__applyPrefix(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Archivo+Black')
        self.assertTrue(resource.getApplyPrefix())

    def test_cssregistry__Crete_Round_400_400italic__title(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Crete+Round:400,400italic')
        self.assertIsNone(resource.getTitle())

    def test_cssregistry__Crete_Round_400_400italic__authenticated(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Crete+Round:400,400italic')
        self.assertFalse(resource.getAuthenticated())

    def test_cssregistry__Crete_Round_400_400italic__cacheable(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Crete+Round:400,400italic')
        self.assertFalse(resource.getCacheable())

    def test_cssregistry__Crete_Round_400_400italic__compression(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Crete+Round:400,400italic')
        self.assertEqual(resource.getCompression(), 'none')

    def test_cssregistry__Crete_Round_400_400italic__conditionalcomment(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Crete+Round:400,400italic')
        self.assertEqual(resource.getConditionalcomment(), '')

    def test_cssregistry__Crete_Round_400_400italic__cookable(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Crete+Round:400,400italic')
        self.assertFalse(resource.getCookable())

    def test_cssregistry__Crete_Round_400_400italic__enabled(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Crete+Round:400,400italic')
        self.assertTrue(resource.getEnabled())

    def test_cssregistry__Crete_Round_400_400italic__expression(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Crete+Round:400,400italic')
        self.assertEqual(resource.getExpression(), '')

    def test_cssregistry__Crete_Round_400_400italic__media(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Crete+Round:400,400italic')
        self.assertEqual(resource.getMedia(), 'screen')

    def test_cssregistry__Crete_Round_400_400italic__rel(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Crete+Round:400,400italic')
        self.assertEqual(resource.getRel(), 'stylesheet')

    def test_cssregistry__Crete_Round_400_400italic__rendering(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Crete+Round:400,400italic')
        self.assertEqual(resource.getRendering(), 'link')

    def test_cssregistry__Crete_Round_400_400italic__applyPrefix(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Crete+Round:400,400italic')
        self.assertTrue(resource.getApplyPrefix())

    def test_cssregistry__Cambo__title(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Cambo')
        self.assertIsNone(resource.getTitle())

    def test_cssregistry__Cambo__authenticated(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Cambo')
        self.assertFalse(resource.getAuthenticated())

    def test_cssregistry__Cambo__cacheable(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Cambo')
        self.assertFalse(resource.getCacheable())

    def test_cssregistry__Cambo__compression(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Cambo')
        self.assertEqual(resource.getCompression(), 'none')

    def test_cssregistry__Cambo__conditionalcomment(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Cambo')
        self.assertEqual(resource.getConditionalcomment(), '')

    def test_cssregistry__Cambo__cookable(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Cambo')
        self.assertFalse(resource.getCookable())

    def test_cssregistry__Cambo__enabled(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Cambo')
        self.assertTrue(resource.getEnabled())

    def test_cssregistry__Cambo__expression(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Cambo')
        self.assertEqual(resource.getExpression(), '')

    def test_cssregistry__Cambo__media(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Cambo')
        self.assertEqual(resource.getMedia(), 'screen')

    def test_cssregistry__Cambo__rel(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Cambo')
        self.assertEqual(resource.getRel(), 'stylesheet')

    def test_cssregistry__Cambo__rendering(self):
        resource = self.get_css_resource('http://fonts.googleapis.com/css?family=Cambo')
        self.assertEqual(resource.getRendering(), 'link')

    def test_cssregistry__main__title(self):
        resource = self.get_css_resource('++resource++ll.theme/css/main.css')
        self.assertIsNone(resource.getTitle())

    def test_cssregistry__main__authenticated(self):
        resource = self.get_css_resource('++resource++ll.theme/css/main.css')
        self.assertFalse(resource.getAuthenticated())

    def test_cssregistry__main__cacheable(self):
        resource = self.get_css_resource('++resource++ll.theme/css/main.css')
        self.assertTrue(resource.getCacheable())

    def test_cssregistry__main__compression(self):
        resource = self.get_css_resource('++resource++ll.theme/css/main.css')
        self.assertEqual(resource.getCompression(), 'safe')

    def test_cssregistry__main__conditionalcomment(self):
        resource = self.get_css_resource('++resource++ll.theme/css/main.css')
        self.assertEqual(resource.getConditionalcomment(), '')

    def test_cssregistry__main__cookable(self):
        resource = self.get_css_resource('++resource++ll.theme/css/main.css')
        self.assertTrue(resource.getCookable())

    def test_cssregistry__main__enabled(self):
        resource = self.get_css_resource('++resource++ll.theme/css/main.css')
        self.assertTrue(resource.getEnabled())

    def test_cssregistry__main__expression(self):
        resource = self.get_css_resource('++resource++ll.theme/css/main.css')
        self.assertEqual(resource.getExpression(), '')

    def test_cssregistry__main__media(self):
        resource = self.get_css_resource('++resource++ll.theme/css/main.css')
        self.assertEqual(resource.getMedia(), 'screen')

    def test_cssregistry__main__rel(self):
        resource = self.get_css_resource('++resource++ll.theme/css/main.css')
        self.assertEqual(resource.getRel(), 'stylesheet')

    def test_cssregistry__main__rendering(self):
        resource = self.get_css_resource('++resource++ll.theme/css/main.css')
        self.assertEqual(resource.getRendering(), 'link')

    def test_metadata__dependency__sll_basetheme(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('sll.basetheme'))

    def test_metadata__dependency__sll_carousel(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('sll.carousel'))

    def test_metadata__dependency__sll_templates(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('sll.templates'))

    def test_metadata__version(self):
        setup = getToolByName(self.portal, 'portal_setup')
        self.assertEqual(
            setup.getVersionForProfile('profile-ll.theme:default'), u'3')

    def uninstall_package(self):
        """Uninstall package: ll.theme."""
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['ll.theme'])

    def test_uninstall__package(self):
        self.uninstall_package()
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.assertFalse(installer.isProductInstalled('ll.theme'))

    def test_uninstall__browserlayer(self):
        self.uninstall_package()
        from ll.theme.browser.interfaces import ILlThemeLayer
        from plone.browserlayer import utils
        self.assertNotIn(ILlThemeLayer, utils.registered_layers())
