import cv2
import numpy as np

class ImageBits:
    def __init__(self, image_path):
        self.image = cv2.imread(image_path)
        self.image = np.array(self.image)

        self.height = self.image.shape[0]
        self.width = self.image.shape[1]
        self.depth = self.image.shape[2]

        self.max_bit_size = self.height * self.width * self.depth * 2
        self.used_bits = 0

    def get_formatted_max_bit_size(self):
        gb = 1_000_000_000_000
        mb = 1_000_000_000
        kb = 1_000_000
        b =  1_000
        
        max_size = self.max_bit_size
        gb_size = max_size // gb
        max_size -= gb_size * gb

        mb_size = max_size // mb
        max_size -= mb_size * mb

        kb_size = max_size // kb
        max_size -= kb_size * kb
        
        byte_size = max_size // b
        max_size -= byte_size * b
        
        b_size = max_size
        
        return f'{gb_size} GB {mb_size} MB {kb_size} KB {byte_size} B {b_size} b'