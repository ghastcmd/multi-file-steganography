import numpy as np
import cv2
from random import randint as rnd

from image_bits import ImageBits

import time
from bitstream import bitstream

def main():
    file = ImageBits('./images/5G5hW9j.jpg')
    # cv2.imshow('test image', file.image)    
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    print(file.max_bit_size)
    print(file.get_formatted_max_bit_size())
    
    test_bitstream = bitstream(file.height * file.width * file.depth * 8)
    test_bitstream.byte_array = np.random.randint(0, 255, (test_bitstream.max_byte_size))
    
    start = time.time()
    indices = np.arange(file.image.size).reshape(file.image.shape) * 2
    reduce_func = lambda x: test_bitstream.get_two(x)
    random_values = reduce_func(indices)
    conv_random_values = random_values.astype(np.uint8)
    file.image ^= (-conv_random_values ^ file.image) & (0b11 & conv_random_values)
    end = time.time()
    
    print(f'{round((end-start) * 1_000)} ms')
    
    file.write_image('image3.png')

if __name__ == '__main__':
    main()