import numpy as np
import cv2
from random import randint as rnd

from image_bits import ImageBits
from bitstream import bitstream
from bit_writer import BitWriter
from bit_reader import BitReader

import time

def main():
    start = time.time()
    bit_writer = BitWriter('./conveyer/to_convey.txt', ['./images/5G5hW9j.jpg'])

    bit_writer.write_files()

    bit_reader = BitReader(['image0.png'])
    
    bit_reader.retrieve('out.file')
    end = time.time()
    
    print(f'total: {round((end - start) * 1000)} ms')

if __name__ == '__main__':
    main()