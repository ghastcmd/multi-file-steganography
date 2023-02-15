import numpy as np
import cv2
from random import randint as rnd

from image_bits import ImageBits
from bitstream import bitstream
from bit_writer import BitWriter

import time

def main():
    bit_writer = BitWriter('./conveyer/to_convey.txt', ['./images/5G5hW9j.jpg'])

    bit_writer.write_files()

if __name__ == '__main__':
    main()