import math
import cv2
import numpy as np

from bitstream import bitstream

class ImageBits:
    def __init__(self, image_path):
        self.image = cv2.imread(image_path)
        self.image = np.array(self.image)

        self.height = self.image.shape[0]
        self.width = self.image.shape[1]
        self.depth = self.image.shape[2]

        self.max_bit_size = self.height * self.width * self.depth * 2
        
    def get_formatted_max_bit_size(self):
        gb = 1_000_000_000
        mb = 1_000_000
        kb = 1_000
        b =  1
        
        max_size = self.max_bit_size / 8
        
        gb_size = int(max_size // gb)
        max_size -= gb_size * gb

        mb_size = int(max_size // mb)
        max_size -= mb_size * mb

        kb_size = int(max_size // kb)
        max_size -= kb_size * kb
        
        byte_size = int(max_size // b)
        max_size -= byte_size * b
        
        b_size = int(max_size)
        
        return f'{gb_size} GB {mb_size} MB {kb_size} KB {byte_size} B {b_size} b'

    def write_image(self, file_name: str):
        cv2.imwrite(file_name, self.image)

def test_image_bits():
    file = ImageBits('./images/5G5hW9j.jpg')
    
    assert file.max_bit_size == 12441600
    assert file.get_formatted_max_bit_size() == '0 GB 1 MB 555 KB 200 B 0 b'

if __name__ == '__main__':
    test_image_bits()