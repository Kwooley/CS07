# File 1.py : the module name is File1

import file2

print('File 1: __name__ is set to ', __name__)
if __name__ == '__main__':
    print('File 1 is executed directly')
else:
    print('File 1 executed when imported')
