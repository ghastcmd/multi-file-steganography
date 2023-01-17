import numpy as np
import math

class bitstream:
    def __init__(self, bit_array_length):
        self.max_bit_size = bit_array_length
        self.max_byte_size = math.ceil(bit_array_length / 8)

        self.byte_array = np.zeros((self.max_byte_size), np.byte)
    
    def __getitem__(self, index):
        byte_value = self.byte_array[index // 8]
        rest = index % 8
        ret_value = (byte_value & (0b1 << (7 - rest))) >> (7 - rest)
        return ret_value

    def __setitem__(self, index, value):
        set_value = self.byte_array[index // 8]
        rest = index % 8
        self.byte_array[index // 8] ^= (-bool(value) ^ set_value) & (1 << (7 - rest))

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