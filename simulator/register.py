class Register:
    def __init__(self, bits) -> None:
        self.value = 0
        self.bits = bits

    def __str__(self) -> str:
        '''Used bin to convert it to binary and zfill to pad the binary value to the correct length'''
        temp = bin(self.value)
        return temp[2:].zfill(self.bits)