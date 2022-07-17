def typeA(inst) -> list:
    '''returns a list of inst and regs in type A format \n
        Type A format = [instruction,reg1,reg2,reg3]'''
    # Number of bits = Inst(5bits) + Unused(2) + Reg1(3) + Reg2(3) + Reg3(3)
    return [inst[0:5],inst[7:10],inst[10:13],inst[13:16]]

def typeB(inst) -> list:
    '''returns a list of inst and regs in type B format \n
        Type B format = [instruction,reg1,imm]'''
    # Number of bits = Inst(5bits) + Reg1(3) + Imm(8)
    return [inst[0:5],inst[5:8],inst[8:16]]

def typeC(inst) -> list:
    '''returns a list of inst and regs in type C format \n
        Type C format = [instruction,reg1,reg2]'''
    # Number of bits = Inst(5bits) + Unused(5) + Reg1(3) + Reg2(3)
    return [inst[0:5],inst[10:13],inst[13:16]]

def typeD(inst) -> list:
    '''returns a list of inst and regs in type D format \n
        Type D format = [instruction,reg1,MemAddr]'''
    # Number of bits = Inst(5bits) + Reg1(3) + MemAddr(8)
    return [inst[0:5],inst[5:8],inst[8:16]]

def typeE(inst) -> list:
    '''returns a list of inst and regs in type E format \n
        Type E format = [instruction,MemAddr]'''
    # Number of bits = Inst(5bits) + Unused(3) + MemAddr(8)
    return [inst[0:5],inst[7:16]]

def typeF(inst) -> list:
    '''returns a list of inst and regs in type f format \n
        Type f format = [instruction]'''
    # Number of bits = Inst(5bits) + Unused(11)
    return [inst[0:5]]

# def index(binarystr) -> int:
#     '''returns the index of the instruction in the dictionary'''
#     return int(binarystr,2)