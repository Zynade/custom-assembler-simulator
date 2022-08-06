from utils import *
from register import Register
import sys
# import matplotlib.pyplot as plt
# from sys import std

#Initialied all the registers in global context

INT_MAX = 2**16 - 1
INT_MIN = 0
PC = Register("PC",8)
RF = [Register(f"r{i}",16) for i in range(8)]
RF[7].name = "FLAGS"
Hltflag = False
Jmpflag = False
JmpVal = PC.value
CMPflag = False
t = 0
Time = []
MemoryAccessed = []


# MEM = ""

def setFlags(index, value) -> None:
    '''sets The flag for overflow(V), less than(L), greater than(G), equals(E). Also used to reset them \n
        index = 3 for V, 2 for L, 1 for G, 0 for E'''
    global CMPflag
    tmp = list(str(RF[7]))[12:]
    #done index abs(index - 3) because of we are storing wrt to LSB (given in guidelines) so it will be opposite of tradional indexing
    index = abs(index - 3)
    tmp[index] = str(value)
    RF[7].value = int("".join(tmp),2)
    CMPflag = True

def getFlag(index) -> int:
    '''Returns the value of the flag at index'''
    index = abs(index - 3)
    # print(f"The flag is {int(list(str(RF[7]))[12+index])}")
    return int(list(str(RF[7]))[12+index])

#Type A instructions

def add(inst) -> None:
    '''Perfoms the add inst : r3 = r2 + r1 if add r1 r2 r3'''
    components = typeA(inst)
    RF[int(components[3],2)].value = (RF[int(components[2],2)].value + RF[int(components[1],2)].value)
    # print(f"The value of register {RF[int(components[3],2)].name} is {RF[int(components[3],2)].value}")
    if RF[int(components[3],2)].value > INT_MAX:
        # print(f"Overflow occured in add instruction. R3 = {RF[int(components[3],2)].value}")
        RF[int(components[3],2)].value %= (INT_MAX + 1)
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
    if RF[int(components[3],2)].value > INT_MAX :
        RF[int(components[3],2)].value %= INT_MAX
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
    '''Perfoms the rightshift inst : r1 = r1 >> 45 if rs r1 45'''
    components = typeB(inst)
    RF[int(components[1],2)].value = int((RF[int(components[1],2)].value >> int(components[2], 2)))
    if RF[int(components[1],2)].value > INT_MAX : 
        RF[int(components[1],2)].value %= INT_MAX

def leftShift(inst) -> None:
    '''Perfoms the leftshift inst : r1 = r1 << 45 if rs r1 45'''
    components = typeB(inst)
    RF[int(components[1],2)].value = (RF[int(components[1],2)].value << int(components[2], 2))
    if RF[int(components[1],2)].value > INT_MAX :
        RF[int(components[1],2)].value = 0

#Type C instructions

def movRegister(inst) -> None:
    '''Perfoms the mov inst : r3 = r2 if mov r2 r3'''
    components = typeC(inst)
    RF[int(components[2],2)].value = RF[int(components[1],2)].value

def divide(inst) -> None:
    '''Perfoms the divide inst : r0 = r3 / r4 and r1 = r3 % r4 if div r3 r4'''
    components = typeC(inst)
    RF[0].value = (RF[int(components[1],2)].value // RF[int(components[2],2)].value)
    RF[1].value = (RF[int(components[1],2)].value % RF[int(components[2],2)].value)

def invert(inst) -> None:
    '''Perfoms the invert inst : r3 = ~r1 if not r1 r3'''
    components = typeC(inst)
    tmp = list(str(RF[int(components[1],2)]))
    # print(tmp)
    for i in range(len(tmp)):
        if tmp[i] == "0":
            tmp[i] = "1"
        else:
            tmp[i] = "0"
    # print(tmp)
    RF[int(components[2],2)].value = int("".join(tmp),2)

def compare(inst) -> None:
    '''Perfoms the compare inst  if cmp r1 r2'''
    components = typeC(inst)
    # print(f"Comparing {components}")
    if RF[int(components[1],2)].value > RF[int(components[2],2)].value :
        setFlags(1,1)
    elif RF[int(components[1],2)].value < RF[int(components[2],2)].value :
        setFlags(2,1)
    elif RF[int(components[1],2)].value == RF[int(components[2],2)].value :
        # print(f"{RF[int(components[1],2)].value} == {RF[int(components[2],2)].name}")
        setFlags(0,1)

#Type D instructions

def load(inst) -> None:
    '''Perfoms the load inst : r3 = MEM[45] if load r3 $45'''
    global MEM
    global Time
    global MemoryAccessed
    global t
    Time.append(t)
    components = typeD(inst)
    try:
        RF[int(components[1],2)].value = int(MEM[int(components[2],2)],2)
    except IndexError:
        RF[int(components[1],2)].value = 0
    MemoryAccessed.append(int(components[2],2))

def store(inst) -> None:
    '''Perfoms the store inst : MEM[45] = r3 if store r3 $45'''
    global MEM
    global Time
    global MemoryAccessed
    global t
    Time.append(t)
    components = typeD(inst)
    if int(components[2],2) > len(MEM) - 1 :
        MEM.extend(['0'*16] * (int(components[2],2) - len(MEM) + 1))
    MEM[int(components[2],2)] = bin(RF[int(components[1],2)].value)[2:].zfill(16)
    MemoryAccessed.append(int(components[2],2))

#Type E instructions
def jmp(inst) -> None:
    global Jmpflag
    global JmpVal
    '''Perfoms the jmp inst : PC = 45 if jmp $45'''
    components = typeE(inst)
    JmpVal = int(components[1],2)
    # print(f"PC is set to {PC.value}")
    Jmpflag = True
    # print(f"Jmpflag is set to {Jmpflag}")

def jlt(inst) -> None:
    '''Perfoms the jlt inst : PC = 45 if jlt $45'''
    global Jmpflag
    global JmpVal
    components = typeE(inst)
    if getFlag(2) == 1:
        JmpVal = int(components[1],2)
        Jmpflag = True

def jgt(inst) -> None:
    '''Perfoms the jgt inst : PC = 45 if jgt $45'''
    global Jmpflag
    global JmpVal
    components = typeE(inst)
    if getFlag(1) == 1 :
        JmpVal = int(components[1],2)
        Jmpflag = True
    
def je(inst) -> None:
    '''Perfoms the jle inst : PC = 45 if jle $45'''
    global Jmpflag
    global JmpVal
    components = typeE(inst)
    # print(f"{getFlag(0)}")
    if getFlag(0) == 1 :
        # print(f"{getFlag(0)}")
        JmpVal = int(components[1],2)
        # print(f"PC is set to {PC.value}")
        Jmpflag = True

#type F instructions
def halt(inst) -> None:
    '''Perfoms the halt inst : halt'''
    global Hltflag
    components = typeF(inst)
    Hltflag = True

ExecuteEngine = {
    "10000" : add ,
    "10001" : sub ,
    "10010" : movIntermediate ,
    "10011" : movRegister ,
    "10100" : load ,
    "10101" : store ,
    "10110" : multiply ,
    "10111" : divide ,
    "11000" : rightShift ,
    "11001" : leftShift ,
    "11010" : xor ,
    "11011" : bitOr ,
    "11100" : bitAnd , 
    "11101" : invert , 
    "11110" : compare , 
    "11111" : jmp , 
    "01100" : jlt , 
    "01101" : jgt , 
    "01111" : je , 
    "01010" : halt
}

def dump(f):
    print(f"{PC}", end = " ")
    # f.write(f"{PC.value} ")
    f.write(f"{PC} ")
    for i in range(len(RF)-1):
        print(f"{RF[i]}", end = " ")
        f.write(f"{RF[i]} ")
    print(f"{RF[len(RF)-1]}")
    f.write(f"{RF[len(RF)-1]}")
    f.write("\n")
    # print()

def main():
    global PC
    global RF
    global Hltflag 
    global MEM
    global Jmpflag
    global JmpVal
    global CMPflag
    global Time
    global MemoryAccessed
    global t
    MEM = sys.stdin.read()
    MEM = MEM.split("\n")
    # with open("input.txt") as f:
    #     MEM = f.read().split("\n")
    #the last input is EOF which is getting read by MEM so popping it incase of error
    while MEM[-1] == "" or MEM[-1] == "\n":
        MEM.pop()
    # print(MEM)
    with open("output.txt", "w") as f:
        t = 1
        while(not Hltflag):
            Time.append(t)
            MemoryAccessed.append(PC.value)
            inst = MEM[PC.value]
            ExecuteEngine[inst[:5]](inst)
            if(CMPflag):
                CMPflag = False
            else:
                setFlags(0,0)
                setFlags(1,0)
                setFlags(2,0)
                setFlags(3,0)
            dump(f)
            # print(f"flag : {Jmpflag}")
            if(Jmpflag):
                PC.value = JmpVal
            else:
                PC.value += 1
            Jmpflag = False
            if PC.value >= len(MEM) :
                Hltflag = True
                # print(f"Halt flag is set to {Hltflag}")
            t += 1
        MEM.extend(['0'*16] * (256 - len(MEM)))
        for i in range(len(MEM)):
            print(f"{MEM[i]}")
            f.write(f"{MEM[i]}\n")
        # f.write("0"*16 + "\n")
    # print("0"*16)
    # print()
    # print(f"Time taken : {Time}")
    # print(f"Memory accessed : {MemoryAccessed}")
    # plt.scatter(x=Time,y=MemoryAccessed)
    # plt.xlabel("Time")
    # plt.ylabel("Memory accessed")
    # plt.title("Memory accessed vs time")
    # plt.show()

# Hltflag = False
main()
