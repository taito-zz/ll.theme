from Products.CMFCore.utils import getToolByName

import logging


PROFILE_ID = 'profile-ll.theme:default'


def install_packages(context, names, logger=None):
    """Installs packages."""
    if logger is None:
        logger = logging.getLogger(__name__)

    installer = getToolByName(context, 'portal_quickinstaller')
    if not isinstance(names, list):
        names = [names]
    for name in names:
        logger.info('Installing {}.'.format(name))
        installer.installProduct(name)


def upgrade_0_to_1(context, logger=None):
    """Installs Products.PloneFormGen and collective.cropimage."""
    packages = ['collective.folderlogo', 'Products.PloneFormGen']
    install_packages(context, packages, logger)
