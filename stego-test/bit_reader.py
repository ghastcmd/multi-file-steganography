import time
import os

import numpy as np

from image_bits import ImageBits

class BitReader:
    def __init__(self, files: list[str]):
        self.datas = []
        self.containers = []
        for file in files:
            self.containers.append(ImageBits(file))
    
        self.current_byte = 0
    
    def retrieve_bitsream(self, image_bits: ImageBits) -> np.ndarray:
        image_sep = image_bits.image.reshape((-1, 4))
    
        shift_ind = np.array([6, 4, 2, 0], dtype=np.uint8)

        print('timing bits retrieval')

        start = time.time()
        ret_val = np.bitwise_and(image_sep, 0b11).astype(np.uint8)
        ret_val = np.left_shift(ret_val, shift_ind).astype(np.uint8)
        ret_val = np.bitwise_or.reduce(ret_val, axis=1).astype(np.uint8)
        end = time.time()
        
        print(f'{round((end - start) * 1000)} ms')
        
        return ret_val
    
    def get_data(self):
        data_list = []
        for container in self.containers:
            data_list.append(self.retrieve_bitsream(container))
        
        self.data = np.concatenate(tuple(data_list), dtype=np.uint8)
        
    def parse_data(self):
        self.name_string_lenth = int.from_bytes(self.data[:4], byteorder='little', signed=False)
        self.current_byte += 4
        
        self.name_string = self.data[
                self.current_byte:self.name_string_lenth + self.current_byte
            ].tostring().decode('utf-8')
        self.current_byte += self.name_string_lenth
        
        self.data_length = int.from_bytes(
            self.data[self.current_byte:self.current_byte+4],
            byteorder='little',
            signed=False
        )
        self.current_byte += 4
        
        self.file_data = np.array(self.data[self.current_byte:self.current_byte + self.data_length])
        
    def retrieve(self, out_folder: str):
        self.get_data()
        self.parse_data()
        with open(os.path.join(out_folder, self.name_string), 'wb') as file:
            file.write(self.file_data.tostring()) 

def test_bit_reader():
    return

if __name__ == '__main__':
    test_bit_reader()