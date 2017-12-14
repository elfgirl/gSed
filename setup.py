#from distutils.core import setup
from setuptools import setup, find_packages

files = ["gSed/*"]

setup(
    name='gSed',
    version='0.1',
    packages=find_packages(),
    url='',
    license='Apache Software License',
    author='Adrianne Mulvaney',
    author_email='amulvaney@gmail.com',
    description='Gender text stream editor',

    package_data= {'': ['data/*.xml', 'data/*.json', 'doc/*.rst', 'doc/*.txt', 'lib/*.py']},

    include_package_data=True,

    scripts=['scripts/gSed.py'],

    keywords='Gender',

    classifiers=[
         'Programming Language :: Python',
         'Programming Language :: Python :: 2',
         'Development Status :: 4 - Beta',
         'Intended Audience :: Developers',
         'Intended Audience :: System Administrators',
         'Intended Audience :: Other Audience',
         'License :: OSI Approved :: Apache Software License',
         'Operating System :: OS Independent',
         'Topic :: Security',
         'Topic :: Software Development :: Libraries :: Application '
         'Frameworks',
     ],
    zip_safe=True

)
