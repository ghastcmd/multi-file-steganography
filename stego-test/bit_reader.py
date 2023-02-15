import time
import struct

import numpy as np

from image_bits import ImageBits
from bitstream import conv_bitimage_bistream

class BitReader:
    def __init__(self, files: list[str]):
        self.datas = []
        self.containers = []
        for file in files:
            self.containers.append(ImageBits(file))
    
        self.current_byte = 0
    
    def get_data(self):
        data_list = []
        start = time.time()
        for container in self.containers:
            data_list.append(conv_bitimage_bistream(container))
        end = time.time()
        
        print(f'container: {round((end - start) * 1000)} ms')
        
        print('bin data_list:\n', bin(data_list[0][0]))
        
        start = time.time()
        self.data = np.concatenate(tuple(data_list), dtype=np.uint8)
        end = time.time()
        
        print(f'concat: {round((end - start) * 1000)} ms')
        
    def parse_data(self):
        print('data:\n', self.data)
        string_length = int.from_bytes(self.data[:4], byteorder='little', signed=True)
        print(self.data[:4])
        print(string_length)
        
    def retrieve(self, out_file: str):
        self.get_data()
        self.parse_data()
        self.out = out_file

def test_bit_reader():
    return

if __name__ == '__main__':
    test_bit_reader()