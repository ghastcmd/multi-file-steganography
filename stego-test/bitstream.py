import math
import time
import ctypes

import numpy as np

from image_bits import ImageBits

class bitstream:
    def __init__(self, name: str, bit_array_length: int, content):
        self.max_bit_size = bit_array_length
        self.max_byte_size = math.ceil(bit_array_length / 8)

        self.byte_array = np.frombuffer(content, dtype=np.uint8)

        print(np.uint8(np.int32(len(name))))

        name_string_len = np.frombuffer(np.int32(len(name)), np.uint8)
        print(name_string_len)
        name_string = np.frombuffer(name.encode('utf-8'), np.uint8)
        content_len = np.frombuffer(np.int32(len(self.byte_array)), np.uint8)

        self.byte_array = np.concatenate((
            name_string_len,
            name_string,
            content_len,
            self.byte_array
        ), dtype=np.uint8)
        
        print('byte_array:\n', self.byte_array)
    
    def __getitem__(self, index):
        byte_value = self.byte_array[index // 8]
        rest = index % 8
        ret_value = (byte_value & (0b1 << (7 - rest))) >> (7 - rest)
        return ret_value

    def get_two(self, index):
        byte_value = self.byte_array[(index // 8) % self.max_bit_size]
        rest = index % 8
        ret_value = (byte_value & (0b11 << (6 - rest))) >> (6 - rest)
        return ret_value

    def __setitem__(self, index, value):
        set_value = self.byte_array[index // 8]
        rest = index % 8
        self.byte_array[index // 8] ^= (-bool(value) ^ set_value) & (1 << (7 - rest))


def conv_bitimage_bistream(image_bits: ImageBits) -> np.ndarray:
    image_sep = image_bits.image.reshape((-1, 4))
    
    lib = ctypes.CDLL('./create_byte_func.so')
    lib.get_byte.argtypes = [ctypes.POINTER(ctypes.c_uint8)]
    lib.get_byte.restype = ctypes.c_byte
    
    volve_func = lambda x: lib.get_byte(x.ctypes.data_as(ctypes.POINTER(ctypes.c_uint8)))
    
    vectorize_func = np.vectorize(volve_func, signature='(n)->()')

    print('image_sep:\n', image_sep.flatten()[:8])

    start = time.time()
    ret_val = vectorize_func(image_sep).astype(np.uint8)
    end = time.time()
    print(f'vectorization: {round((end - start) * 1000)} ms')

    print('ret_val:\n', ret_val.flatten()[:8])

    print(type(ret_val))
    print(ret_val.shape)
    return ret_val

def test_bitstream():
    test_bitstream = bitstream(16)
    assert len(test_bitstream.byte_array) == 2
    
    test_bitstream.byte_array[0] = 0b00011001
    test_bitstream.byte_array[1] = 0b01101001
    test_bitstream[2] = 1
    test_bitstream[8] = 1
    test_bitstream[9] = 0
    check_string = ''
    for i in range(16):
        check_string += f'{test_bitstream[i]}'
        if i == 7:
            check_string += ' '
    
    assert check_string == '00111001 10101001'
    print('Test Passed')

if __name__ == '__main__':
    test_bitstream()