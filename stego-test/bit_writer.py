import numpy as np

from image_bits import ImageBits
from bitstream import bitstream

class BitWriter:
    def __init__(self, file_in_name: str, container_file_paths: list[str]):
        self.containers = []
        for file in container_file_paths:
            self.containers.append(ImageBits(file))
        
        file_bytes = open(file_in_name, 'rb').read()
        self.bitstream = bitstream(file_in_name, file_bytes)

        self.written_bits = 0
        self.image_file_count = 0
    
    def write_single_file(self, cur_image: ImageBits, start: int, end: int):
        indices = np.arange(start, end, 2, dtype=np.uint64).reshape(cur_image.image.shape)
        reduce_func = lambda x: self.bitstream.get_two(x)
        
        bits_values = reduce_func(indices).astype(np.uint8)
    
        cur_image.image = cur_image.image & ~0b11 | bits_values
    
        self.written_bits += end - start

    def write_all(self):
        for image in self.containers:
            self.write_single_file(image, self.written_bits, image.max_bit_size)
            if self.written_bits >= self.bitstream.max_bit_size:
                break
    
    def write_files(self):
        for image in self.containers:
            image.write_image(f'image{self.image_file_count}.png')
            self.image_file_count += 1

        self.image_file_count = 0