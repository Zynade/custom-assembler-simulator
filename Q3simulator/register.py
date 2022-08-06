class Register:
    def __init__(self, name, bits) -> None:
        self.name = name
        self.value = 0
        self.bits = bits

    def __str__(self) -> str:
        '''Used bin to convert it to binary and zfill to pad the binary value to the correct length'''
        if type(self.value) == int:
            temp = bin(self.value)[2:]
            # print(f"{self.name} : {temp.zfill(self.bits)}")
            return temp.zfill(self.bits)
        if type(self.value) == float:
            # print(f"{self.name} : {temp.zfill(self.bits)}")
            return self.floatTOIEE()

    def floatTOIEE(self)->str:
        '''Converts a float to given assignment format'''
        IntPart = int(self.value)
        Intstring = bin(IntPart)[2:]
        FractionPart = self.value - IntPart
        n = 0
        Fractionstring = ''
        while FractionPart != 1:
            if n == 5:
                break
            FractionPart = FractionPart * 2
            if FractionPart >= 1:
                Fractionstring += '1'
                FractionPart -= 1
            else:
                Fractionstring += '0'
            n += 1
        Floatstring = Intstring + Fractionstring
        exponent = bin(len(Intstring)-1)[2:]
        Mantissa = Floatstring[1:6]
        return (exponent + Mantissa).zfill(16)

        
