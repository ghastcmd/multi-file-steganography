import time

import numpy as np

from image_bits import ImageBits
from bitstream import conv_bitimage_bistream

class BitReader:
    def __init__(self, files: list[str]):
        self.datas = []
        self.containers = []
        for file in files:
            self.containers.append(ImageBits(file))
    
    def get_data(self):
        data_list = []
        start = time.time()
        for container in self.containers:
            data_list.append(conv_bitimage_bistream(container))
        end = time.time()
        
        print(f'container: {round((end - start) * 1000)} ms')
        
        start = time.time()
        self.data = np.concatenate(tuple(data_list), dtype=np.byte)
        end = time.time()
        
        print(f'concat: {round((end - start) * 1000)} ms')
        
    def retrieve(self, out_file: str):
        self.get_data()
        self.out = out_file