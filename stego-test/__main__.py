import cv2

from image_bits import ImageBits

def main():
    file = ImageBits('./images/5G5hW9j.jpg')
    # cv2.imshow('test image', file.image)    
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    print(file.max_bit_size)
    size_fmt = file.get_formatted_max_bit_size()
    print(size_fmt)

if __name__ == '__main__':
    main()