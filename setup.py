from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(name='sparc.common',
      version=version,
      description="Common utilities used within SPARC platform",
      long_description=open("README.md").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords=['zca'],
      author='David Davis',
      author_email='davisd50@gmail.com',
      url='https://github.com/davisd50/sparc.common',
      download_url = '',
      license='MIT',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['sparc'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'zope.interface',
          'zope.component',
          'zope.configuration',
          'zope.security',
          'zope.i18nmessageid'
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
