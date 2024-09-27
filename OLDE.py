import ctypes
bt_module = ctypes.CDLL('./BT_enc.cpython-311.so')
bt_module.main()
