import numpy as np

from image_bits import ImageBits
from bitstream import bitstream

class BitWriter:
    def __init__(self, bistream_in: bitstream, container_list: list[ImageBits]):
        self.containers = container_list
        self.bitstream = bistream_in

        self.written_bits = 0
    
    def write_single_file(self, cur_image: ImageBits, start: int, end: int):
        indices = np.arange(start, end, 2).reshape(cur_image.image.shape)
        reduce_func = lambda x: self.bitstream.get_two(x)
        
        bits_values = reduce_func(indices)
        
        conv_bits_values = bits_values.astype(np.uint8)
        cur_image.image ^= (-conv_bits_values ^ cur_image.image) & (0b11 & conv_bits_values)
    
        self.written_bits += end - start
    
    def write_all(self):
        for image in self.containers:
            self.write_single_file(image, self.written_bits, image.max_bit_size)
            if self.written_bits >= self.bitstream.max_bit_size:
                break