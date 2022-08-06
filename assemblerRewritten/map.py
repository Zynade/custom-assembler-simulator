import math
import verify

registers = {
  'R0' : '000',
  'R1' : '001',
  'R2' : '010',
  'R3' : '011',
  'R4' : '100',
  'R5' : '101',
  'R6' : '110'
}

opcode = {
    'add' : {
        'verify' : verify.verifyTypeA ,
        'binaryeq': ['1000000']
    },
    'sub' : {
        'verify' : verify.verifyTypeA ,
        'binaryeq': ['1000100']
    },
    'mul' : {
        'verify' : verify.verifyTypeA ,
        'binaryeq': ['1011000']
    },
    'xor' : {
        'verify' : verify.verifyTypeA ,
        'binaryeq': ['1101000']
    },
    'and' : {
        'verify' : verify.verifyTypeA ,
        'binaryeq': ['1110000']
    },
    'or' : {
        'verify' : verify.verifyTypeA ,
        'binaryeq': ['1101100']
    },
    'mov' : {
        'verify' : verify.verifyMove ,
        'binaryeq': ['1001100000', '10010']
    },
    'rs' : {
        'verify' : verify.verifyTypeB ,
        'binaryeq': ['11000']
    },
    'ls' : {
        'verify' : verify.verifyTypeB ,
        'binaryeq': ['11001']
    },
    'addf' : {
        'verify' : verify.verify_F_Add_Sub ,
        'binaryeq': ['0000000']
    },
    'subf' : {
        'verify' : verify.verify_F_Add_Sub ,
        'binaryeq' : ['0000100']
    },
    'movf' : {
        'verify' : verify.verifyMovF ,
        'binaryeq' : ['00010']
    },
    'div': {
        'verify': verify.verifyTypeC,
        'binaryeq': ['1011100000']
    },
    'not': {
        'verify': verify.verifyTypeC,
        'binaryeq': ['1110100000']
    },
    'cmp': {
        'verify': verify.verifyTypeC,
        'binaryeq': ['1111000000']
    },
    'ld': {
        'verify': verify.verifyTypeD,
        'binaryeq': ['10100']
    },
    'st': {
        'verify': verify.verifyTypeD,
        'binaryeq': ['10101']
    },
    'jmp': {
        'verify': verify.verifyTypeE,
        'binaryeq': ['11111000']
    },
    'jlt': {
        'verify': verify.verifyTypeE,
        'binaryeq': ['01100000']
    },
    'jgt': {
        'verify': verify.verifyTypeE,
        'binaryeq': ['01101000']
    },
    'je': {
        'verify': verify.verifyTypeE,
        'binaryeq': ['01111000']
    },
    'hlt': {
        'verify': verify.verifyTypeF,
        'binaryeq': ['0101000000000000']
    }
}

forbiddenKeywords = ['add', 'sub', 'mov', 'ld', 'st', 'mul', 'div', 'rs', 'ls', 'xor', 'or', 'and', 'not', 'cmp', 'jmp', 'jlt', 'jgt', 'je', 'hlt', 'R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'FLAGS']

def dictTemp(register):
    temp = registers[register]
    return temp

def optest(instruction):
    instruction = instruction.split(' ')
    temp = instruction[0]
    if temp == None:
        return -1
    # if temp
    if temp in opcode:
        res = opcode[temp]['verify'](instruction)
        if res:
            return opcode[temp]['binaryeq'][res]

def immDecToBin(imm):
    # Convert an immediate value to binary.

    # TODO: If imm is a float, parse it as per Q3 requirements. Currently, the program throws an errror if it encounters a float.

    imm = int(imm[1:])
    if imm > 255 or imm < 0 or math.isnan(imm):
        return -1
    imm = bin(imm)[2:]
    imm = imm.zfill(8)
    return imm

def immediateToFloatingPoint(imm):
    # Convert an immediate value to floating point.
    totalSize = 6
    imm = imm[1:]
    if (float(imm) < 1):
        return -1
    intNumber, floatNumber = imm.split('.')
    floatNumber = float('0.'+floatNumber)
    intBinary = bin(int(intNumber))[2:]
    totalSize -= len(intBinary)
    # convert floating part to binary
    floatingBinary = ''
    while floatNumber != 0:
        if len(floatingBinary) > totalSize:
            return -1
        floatNumber = floatNumber * 2
        if floatNumber >= 1:
            floatingBinary += '1'
            floatNumber -= 1
        else:
            floatingBinary += '0'
    mentisa = (intBinary + floatingBinary)[1:6]
    exponent = len(intBinary[1:])
    while len(mentisa) < 5:
        mentisa += '0'
    finalBinary = (bin(exponent)[2:] + mentisa)
    return finalBinary.zfill(8)
