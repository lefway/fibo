from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='fibo',
      version=version,
      description="ejemplo de fibonache",
      long_description="""\
este es una descrpcion mas detallada del paqute fibonache""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='fibonche paquete python',
      author='lflorez',
      author_email='lefway@gmail.com',
      url='https://github.com/lefway/fibo',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
