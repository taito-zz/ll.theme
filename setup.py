from setuptools import find_packages
from setuptools import setup


setup(
    name='ll.theme',
    version='0.0',
    description="LL site theme.",
    long_description=open("README.rst").read(),
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7"],
    keywords='',
    author='Taito Horiuchi',
    author_email='taito.horiuchi@abita.fi',
    url='http://www.ll.fi/',
    license='None-free',
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'': 'src'},
    namespace_packages=['ll'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Products.CMFPlone>=4.2',
        'Products.PloneFormGen',
        'collective.contentleadimage',
        'collective.cropimage',
        'five.grok',
        'hexagonit.testing',
        'plone.app.theming',
        'plone.app.themingplugins',
        'setuptools'],
    entry_points="""
    # -*- Entry points: -*-

    [z3c.autoinclude.plugin]
    target = plone
    """)
