from Products.CMFCore.utils import getToolByName
from ll.theme.tests.base import IntegrationTestCase

import mock


class TestCase(IntegrationTestCase):
    """TestCase for Upgrade Step"""

    def setUp(self):
        self.portal = self.layer['portal']

    def test_install_package(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['collective.cropimage'])
        self.assertFalse(installer.isProductInstalled('collective.cropimage'))

        from ll.theme.upgrades import install_packages
        install_packages(self.portal, 'collective.cropimage')

        self.assertTrue(installer.isProductInstalled('collective.cropimage'))

    def test_install_packages(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['collective.cropimage'])
        self.assertFalse(installer.isProductInstalled('collective.cropimage'))

        from ll.theme.upgrades import install_packages
        logger = mock.Mock()
        install_packages(self.portal, ['collective.cropimage'], logger)

        self.assertTrue(installer.isProductInstalled('collective.cropimage'))
        logger.info.assert_called_with('Installing collective.cropimage.')

    @mock.patch('ll.theme.upgrades.logging')
    @mock.patch('ll.theme.upgrades.install_packages')
    def test_upgrade_0_to_1_with_logger(self, install_packages, logging):
        from ll.theme.upgrades import upgrade_0_to_1
        logger = logging.getLogger()
        upgrade_0_to_1(self.portal, logger)
        install_packages.assert_called_with(self.portal, ['collective.folderlogo', 'Products.PloneFormGen'], logger)

    @mock.patch('ll.theme.upgrades.reimport_profile')
    def test_reimport_cssregistry(self, reimport_profile):
        from ll.theme.upgrades import reimport_cssregistry
        reimport_cssregistry(self.portal)
        reimport_profile.assert_called_with(self.portal, 'profile-ll.theme:default', 'cssregistry')
