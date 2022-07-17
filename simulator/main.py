from utils import *
from register import Register
import sys
# from sys import std

#Initialied all the registers in global context


PC = Register("PC",8)
RF = [Register(f"r{i}",16) for i in range(8)]
RF[7].name = "FLAGS"
HLTFLAG = False

# MEM = ""

def setFlags(index, value) -> None:
    '''sets The flag for overflow(V), less than(L), greater than(G), equals(E). Also used to reset them \n
        index = 3 for V, 2 for L, 1 for G, 0 for E'''
    tmp = bin(RF[7].value)[12:]
    #done index abs(index - 3) because of we are storing wrt to LSB (given in guidelines) so it will be opposite of tradional indexing
    index = abs(index - 3)
    tmp[index] = str(value)
    RF[7].value = int(tmp,2)

#Type A instructions

def add(inst) -> None:
    '''Perfoms the add inst : r3 = r2 + r1 if add r1 r2 r3'''
    components = typeA(inst)
    RF[int(components[3],2)].value = (RF[int(components[2],2)].value + RF[int(components[1],2)].value)
    if RF[int(components[3],2)].value > 2*16 :
        RF[int(components[3],2)].value %= 2*16
        setFlags(3,1)

def sub(inst) -> None:
    '''Perfoms the sub inst : r3 = r1 - r2 if sub r1 r2 r3'''
    components = typeA(inst)
    RF[int(components[3],2)].value = RF[int(components[1],2)].value - RF[int(components[2],2)].value 
    if RF[int(components[3],2)].value < 0 :
         RF[int(components[3],2)].value = 0
         setFlags(3,1)

def multiply(inst) -> None:
    '''Perfoms the mul inst : r3 = r2 * r1 if mul r1 r2 r3'''
    components = typeA(inst)
    RF[int(components[3],2)].value = (RF[int(components[2],2)].value * RF[int(components[1],2)].value)
    if RF[int(components[3],2)].value > 2*16 :
        RF[int(components[3],2)].value %= 2*16
        setFlags(3,1)

def xor(inst) -> None:
    '''Perfoms the XOR inst : r3 = r2 XOR r1 if XOR r1 r2 r3'''
    components = typeA(inst)
    RF[int(components[3],2)].value = (RF[int(components[2],2)].value ^ RF[int(components[1],2)].value)

def bitAnd(inst) -> None:
    '''Perfoms the bitand inst : r3 = r2 & r1 if bitand r1 r2 r3'''
    components = typeA(inst)
    RF[int(components[3],2)].value = (RF[int(components[2],2)].value & RF[int(components[1],2)].value)

def bitOr(inst) -> None:
    '''Perfoms the bitor inst : r3 = r2 | r1 if bitor r1 r2 r3'''
    components = typeA(inst)
    RF[int(components[3],2)].value = (RF[int(components[2],2)].value | RF[int(components[1],2)].value)

#Type B instructions

def movIntermediate(inst) -> None:
    '''Perfoms the mov inst : r3 = 45 if mov r3 $45'''
    components = typeB(inst)
    RF[int(components[1],2)].value = int(components[2], 2)
    # print(f"Register {components[1]} is set to {RF[int(components[1],2)].value}")

def rightShift(inst) -> None:
    '''Perfoms the rightshift inst : r3 = r1 >> 45 if rs r1 45'''
    components = typeB(inst)
    RF[int(components[1],2)].value = (RF[int(components[1],2)].value >> int(components[2], 2))
    if RF[int(components[1],2)].value > 2*16 :
        RF[int(components[1],2)].value %= 2*16

def leftShift(inst) -> None:
    '''Perfoms the leftshift inst : r3 = r1 << 45 if rs r1 45'''
    components = typeB(inst)
    RF[int(components[1],2)].value = (RF[int(components[1],2)].value << int(components[2], 2))
    if RF[int(components[1],2)].value > 2*16 :
        RF[int(components[1],2)].value %= 2*16

#Type C instructions

def movRegister(inst) -> None:
    '''Perfoms the mov inst : r3 = r2 if mov r2 r3'''
    components = typeB(inst)
    RF[int(components[2],2)].value = RF[int(components[1],2)].value

def divide(inst) -> None:
    '''Perfoms the divide inst : r0 = r1 / r2 if div r1 r2 and r1 = r1 % r2'''
    components = typeB(inst)
    RF[0].value = (RF[int(components[1],2)].value // RF[int(components[2],2)].value)
    RF[1].value = (RF[int(components[1],2)].value % RF[int(components[2],2)].value)

def invert(inst) -> None:
    '''Perfoms the invert inst : r3 = ~r1 if not r1 r3'''
    components = typeB(inst)
    RF[int(components[2],2)].value = ~RF[int(components[1],2)].value

def compare(inst) -> None:
    '''Perfoms the compare inst  if cmp r1 r2'''
    components = typeB(inst)
    if RF[int(components[1],2)].value > RF[int(components[2],2)].value :
        setFlags(1,1)
    elif RF[int(components[1],2)].value < RF[int(components[2],2)].value :
        setFlags(2,1)
    else :
        setFlags(0,1)

#Type D instructions

def load(inst) -> None:
    '''Perfoms the load inst : r3 = $45 if load r3 $45'''
    pass

def store(inst) -> None:
    '''Perfoms the store inst : $45 = r3 if store r3 $45'''
    pass

#Type E instructions
def jmp(inst) -> None:
    '''Perfoms the jmp inst : PC = 45 if jmp $45'''
    components = typeB(inst)
    PC.value = int(components[1],2)

def jlt(inst) -> None:
    '''Perfoms the jlt inst : PC = 45 if jlt $45'''
    pass
    components = typeB(inst)
    if getFlag(1) == 1 :
        PC.value = int(components[1],2)

def jgt(inst) -> None:
    '''Perfoms the jgt inst : PC = 45 if jgt $45'''
    pass
    components = typeB(inst)
    if getFlag(2) == 1 :
        PC.value = int(components[1],2)
    
def je(inst) -> None:
    '''Perfoms the jle inst : PC = 45 if jle $45'''
    pass
    components = typeB(inst)
    if getFlag(1) == 1 or getFlag(0) == 1 :
        PC.value = int(components[1],2)

#type F instructions
def halt(inst) -> None:
    '''Perfoms the halt inst : halt'''
    components = typeF(inst)
    HLTFLAG = True

ExecuteEngine = {"10000" : add , "10001" : sub , "10010" : movIntermediate , "10011" : movRegister , "10100" : load , "10101" : store , "10110" : multiply , "10111" : divide , "11000" : rightShift , "11001" : leftShift , "11010" : xor , "11011" : bitOr , "11100" : bitAnd , "11101" : invert , "11110" : compare , "11111" : jmp , "01100" : jlt , "01101" : jgt , "01111" : je , "01010" : halt}

def dump():
    print(f"{PC}", end = " ")
    for i in range(len(RF)):
        print(f"{RF[i]}", end = " ")
    print()

def main():
    global PC
    global RF
    global HLTFLAG 
    global MEM
    with open("input.txt") as f:
        MEM = f.readlines()
    # while True:
    #     try:
    #         temp = input()
    #         MEM.append(temp)
    #     except EOFError:
    #         break
    # print(instructions)
    while(not HLTFLAG):
        inst = MEM[PC.value]
        ExecuteEngine[inst[:5]](inst)
        dump()
        PC.value += 1
        if PC.value >= len(MEM) :
            HLTFLAG = True

# HLTFLAG = False
main()
