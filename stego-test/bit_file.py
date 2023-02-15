from bitstream import bitstream

class BitFile:
    def __init__(self, file_path):
        file_bytes = open(file_path, 'rb').read()
        self.bitstream = bitstream(len(file_bytes) // 8, file_bytes)
    