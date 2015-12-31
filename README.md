# Making Python Barcode Reader Extension on Linux

The sample demonstrates how to make Python barcode reader extension on Ubuntu with DBR (Dynamsoft Barcode Reader for Linux).

## Downloads
* [v4.0.0-pre-alpha.tar.gz][1]

## Install DBR
1. Extract dbr package

    ```
    tar -xzf v4.0.0-pre-alpha.tar.gz
    ```

2. Create a symbolic link of barcode shared library:

    ```
    sudo ln -s $(DynamsoftBarcodeReader)/Redist/libDynamsoftBarcodeReaderx64.so /usr/lib/libDynamsoftBarcodeReaderx64.so
    ```

## Getting Started
1. Build the Python barcode extension **dbr.so**:

    ```
    python setup.py build
    ```

2. Install the extension:

    ```
    sudo python setup.py install
    ```

3. Run **test.py**

    ```
    python test.py
    ```

![Python barcode extension](http://www.codepool.biz/wp-content/uploads/2015/12/python-barcode-extension.png)


[1]:http://labs.dynamsoft.com/linux-barcode-reader-overview.htm


