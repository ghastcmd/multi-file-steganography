import os

os.system('clang -O3 -shared -o create_byte_func.so create_byte_func.c')
os.system('del create_byte_func.exp create_byte_func.lib')