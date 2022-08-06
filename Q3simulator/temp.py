def floatTOIEEE(value)->str:
    '''Converts a float to given assignment format'''
    IntPart = int(value)
    Intstring = bin(IntPart)[2:]
    FractionPart = value - IntPart
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

def float_to_decimal(float_num):
    # Parse an IEEE floating point number to it's corresponding decimal representation
    if len(float_num) != 16:
        return
    exp = int(float_num[8:11], 2)
    mant = float_num[11:]
    result = 0
    for i in range(len(mant)):
        if mant[i] == '1':
            result += (1/2)**(i+1)
    result = (1 + result) * (2 ** exp)
    return float(result)

a = floatTOIEEE(252.0)
print(a)
# print(1.5 + 0.5)
print(float_to_decimal(a))