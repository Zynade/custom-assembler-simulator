class Register:
    def __init__(self, name, bits) -> None:
        self.name = name
        self.value = 0
        self.bits = bits

    def __str__(self) -> str:
        '''Used bin to convert it to binary and zfill to pad the binary value to the correct length'''
        temp = bin(self.value)[2:]
        # print(f"{self.name} : {temp.zfill(self.bits)}")
        return temp.zfill(self.bits)