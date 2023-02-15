import numpy as np
import cv2
from random import randint as rnd

from image_bits import ImageBits
from bitstream import bitstream
from bit_writer import BitWriter

import time

def main():
    file = ImageBits('./images/5G5hW9j.jpg')
    
    print(file.max_bit_size)
    print(file.get_formatted_max_bit_size())
    
    test_bitstream = bitstream(file.height * file.width * file.depth * 8)
    test_bitstream.byte_array = np.random.randint(0, 255, (test_bitstream.max_byte_size))
    
    writer = BitWriter(test_bitstream, [file])
    writer.write_all()

    file.write_image('image3.png')

    writer.containers[0].write_image('image4.png')

if __name__ == '__main__':
    main()