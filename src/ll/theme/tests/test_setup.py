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

    def test_cssregistry__jquerytools_dateinput__title(self):
        resource = self.get_css_resource('++resource++plone.app.jquerytools.dateinput.css')
        self.assertIsNone(resource.getTitle())

    def test_cssregistry__jquerytools_dateinput__authenticated(self):
        resource = self.get_css_resource('++resource++plone.app.jquerytools.dateinput.css')
        self.assertFalse(resource.getAuthenticated())

    def test_cssregistry__jquerytools_dateinput__compression(self):
        resource = self.get_css_resource('++resource++plone.app.jquerytools.dateinput.css')
        self.assertEqual(resource.getCompression(), 'safe')

    def test_cssregistry__jquerytools_dateinput__conditionalcomment(self):
        resource = self.get_css_resource('++resource++plone.app.jquerytools.dateinput.css')
        self.assertEqual(resource.getConditionalcomment(), '')

    def test_cssregistry__jquerytools_dateinput__cookable(self):
        resource = self.get_css_resource('++resource++plone.app.jquerytools.dateinput.css')
        self.assertTrue(resource.getCookable())

    def test_cssregistry__jquerytools_dateinput__enabled(self):
        resource = self.get_css_resource('++resource++plone.app.jquerytools.dateinput.css')
        self.assertTrue(resource.getEnabled())

    def test_cssregistry__jquerytools_dateinput__expression(self):
        resource = self.get_css_resource('++resource++plone.app.jquerytools.dateinput.css')
        self.assertEqual(resource.getExpression(), '')

    def test_cssregistry__jquerytools_dateinput__media(self):
        resource = self.get_css_resource('++resource++plone.app.jquerytools.dateinput.css')
        self.assertEqual(resource.getMedia(), 'screen')

    def test_cssregistry__jquerytools_dateinput__rel(self):
        resource = self.get_css_resource('++resource++plone.app.jquerytools.dateinput.css')
        self.assertEqual(resource.getRel(), 'stylesheet')

    def test_cssregistry__jquerytools_dateinput__rendering(self):
        resource = self.get_css_resource('++resource++plone.app.jquerytools.dateinput.css')
        self.assertEqual(resource.getRendering(), 'link')

    def test_cssregistry__jquerytools_dateinput__applyPrefix(self):
        resource = self.get_css_resource('++resource++plone.app.jquerytools.dateinput.css')
        self.assertTrue(resource.getApplyPrefix())

    def test_cssregistry__main__title(self):
        resource = self.get_css_resource('++theme++ll.theme/css/main.css')
        self.assertIsNone(resource.getTitle())

    def test_cssregistry__main__authenticated(self):
        resource = self.get_css_resource('++theme++ll.theme/css/main.css')
        self.assertFalse(resource.getAuthenticated())

    def test_cssregistry__main__compression(self):
        resource = self.get_css_resource('++theme++ll.theme/css/main.css')
        self.assertEqual(resource.getCompression(), 'safe')

    def test_cssregistry__main__conditionalcomment(self):
        resource = self.get_css_resource('++theme++ll.theme/css/main.css')
        self.assertEqual(resource.getConditionalcomment(), '')

    def test_cssregistry__main__cookable(self):
        resource = self.get_css_resource('++theme++ll.theme/css/main.css')
        self.assertTrue(resource.getCookable())

    def test_cssregistry__main__enabled(self):
        resource = self.get_css_resource('++theme++ll.theme/css/main.css')
        self.assertTrue(resource.getEnabled())

    def test_cssregistry__main__expression(self):
        resource = self.get_css_resource('++theme++ll.theme/css/main.css')
        self.assertEqual(resource.getExpression(), 'request/HTTP_X_THEME_ENABLED | nothing')

    def test_cssregistry__main__media(self):
        resource = self.get_css_resource('++theme++ll.theme/css/main.css')
        self.assertIsNone(resource.getMedia())

    def test_cssregistry__main__rel(self):
        resource = self.get_css_resource('++theme++ll.theme/css/main.css')
        self.assertEqual(resource.getRel(), 'stylesheet')

    def test_cssregistry__main__rendering(self):
        resource = self.get_css_resource('++theme++ll.theme/css/main.css')
        self.assertEqual(resource.getRendering(), 'link')

    def test_cssregistry__main__applyPrefix(self):
        resource = self.get_css_resource('++theme++ll.theme/css/main.css')
        self.assertTrue(resource.getApplyPrefix())

    def test_metadata__dependency__plone_app_theming(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('plone.app.theming'))

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
            setup.getVersionForProfile('profile-ll.theme:default'), u'1')

    def get_theme(self):
        from plone.app.theming.interfaces import IThemeSettings
        from plone.registry.interfaces import IRegistry
        from zope.component import getUtility
        return getUtility(IRegistry).forInterface(IThemeSettings)

    def test_them__currentTheme(self):
        theme = self.get_theme()
        self.assertEqual(theme.currentTheme, u'll.theme')

    def test_theme__enabled(self):
        theme = self.get_theme()
        self.assertTrue(theme.enabled)

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

    def test_uninstall__cssregistry_main(self):
        self.uninstall_package()
        resources = set(getToolByName(self.portal, 'portal_css').getResourceIds())
        self.assertNotIn('++theme++ll.theme/css/main.css', resources)
