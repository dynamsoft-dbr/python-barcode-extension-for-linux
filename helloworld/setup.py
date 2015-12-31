from distutils.core import setup, Extension

module_helloworld = Extension('helloworld', sources = ['helloworld.c'])

setup (name = 'Dynamsoft',
        version = '1.0',
        description = 'First module',
        ext_modules = [module_helloworld])
