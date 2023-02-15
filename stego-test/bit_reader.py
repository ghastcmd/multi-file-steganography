import numpy as np

class BitReader:
    def __init__(self, files: list[str]):
        self.files = files
    
        self.data = np.arange(10, dtype=np.byte)
    
    def retrieve(self, out_path: str):
        with open(out_path, 'wb') as file:
            file.write(self.data)