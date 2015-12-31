from distutils.core import setup, Extension

module_dbr = Extension('dbr', 
                        sources = ['dbr.c'], 
                        include_dirs=['/home/xiao/Dynamsoft/BarcodeReader4.0/Include'],
                        library_dirs=['/home/xiao/Dynamsoft/BarcodeReader4.0/Redist'],
                        libraries=['DynamsoftBarcodeReaderx64'])

setup (name = 'DynamsoftBarcodeReader',
        version = '1.0',
        description = 'Python barcode extension',
        ext_modules = [module_dbr])
