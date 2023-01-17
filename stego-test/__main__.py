import cv2
from random import randint as rnd

from image_bits import ImageBits

def main():
    file = ImageBits('./images/5G5hW9j.jpg')
    # cv2.imshow('test image', file.image)    
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    print(file.max_bit_size)
    size_fmt = file.get_formatted_max_bit_size()
    print(size_fmt)
    
    # for i, line in enumerate(file.image):
    #     for j, pixel in enumerate(line):
    #         for k, channel in enumerate(pixel):
    #             byte_value = file.image[i, j, k]
    #             file.image[i, j, k] = byte_value & (rnd(0, 9) & 0b11)
    
    cv2.imwrite('image2.png', file.image)

if __name__ == '__main__':
    main()