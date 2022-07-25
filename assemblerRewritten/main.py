import sys
import map
global errorLineNumber
errorLineNumber = 0
global labels, varArr, memSpace
labels = {}
memSpace = {}
varArr = []

def processInstruction(instruction):
    binary = ''
    instruction = instruction.split(' ')
    operation  = instruction[0]
    for i in range(len(operation)):
        
        if instruction[0] == 'var':
            return ''

        if operation[i] == ':':
            if len(instruction) == 1:
                return ''
            label = operation[:i]
            instruction = instruction[1:]
            operation = instruction[0]
            break
    
    if instruction[0] == 'hlt':
        return -1
    if instruction[0] not in map.opcode:
        raise Exception(f'Encountered a OP code not supported by the ISA at line number {errorLineNumber}')
    ISA = map.opcode[operation]['verify'](instruction)
    if ISA > -1:
        binary += map.opcode[operation]['binaryeq'][ISA]
    else:
        raise Exception(f'Encountered an instruction not supported by the ISA at line number {errorLineNumber}')

    for i in range(1,len(instruction)-1):
        if operation == 'mov' and instruction[1] == 'FLAGS':
            binary += '111'
        elif map.registers[instruction[i]] != None:
            binary += map.registers[instruction[i]]
        else:
            raise Exception(f'Encountered a register not supported by the ISA at line number {errorLineNumber}')
    
    if instruction[len(instruction)-1] in map.registers:
        binary += map.registers[instruction[len(instruction)-1]]
    elif instruction[len(instruction)-1] in varArr:
        binary += memSpace[instruction[len(instruction)-1]]
    elif instruction[len(instruction)-1] in memSpace:
        binary += memSpace[instruction[len(instruction)-1]]
    elif instruction[len(instruction)-1][0]=='$':
        imm = map.immDecToBin(instruction[len(instruction)-1])
        if imm == -1:
            raise Exception(f'Encountered an invalid immediate value at line number {errorLineNumber}')
        else:
            binary += imm
    else:
        raise Exception(f'Encountered an invalid intruction at line number {errorLineNumber}')
    return binary

def preProcessInstruction(instructions):     #, labels, varArr
    global errorLineNumber
    areVarsDeclared = False
    hlt = 0
    for lineNumber in range(len(instructions)):
        errorLineNumber = errorLineNumber + 1
        instruction = instructions[lineNumber]
        if instruction == '':
            continue
        for i in range(len(instruction)):
            if instruction[i] == ':':
                label = instruction[:i]
                if label in map.forbiddenKeywords:
                    raise Exception(f'Label name {label} is not allowed at line number {errorLineNumber}')
                elif label in labels:
                    raise Exception(f'Label {label} already declared at line number {errorLineNumber}')
                instruction = instruction[i+1:]
                labels[label] = lineNumber
                break
        if instruction == '':
            continue
        instruction = instruction.split()
        if instruction[0] == 'hlt':
            hlt += 1
            if hlt > 1:
                raise Exception(f'More than one HLT instruction found at line number {errorLineNumber}')
            # continue
        if instruction[0] == 'var':
            if areVarsDeclared:
                raise Exception(f'Variable must be declared before any other instruction at line number {errorLineNumber}')
            else:
                variable = instruction[1]
                if len(instruction) > 2:
                    raise Exception(f'Variable declaration must be of the form var <variable> at line number {errorLineNumber}')
                if variable in map.forbiddenKeywords:
                    raise Exception(f'Variable name is not allowed at line number {errorLineNumber}')
                if variable in varArr:
                    raise Exception(f'Variable already declared at line number {errorLineNumber}')
                variables = {}
                variables[variable] = lineNumber
                varArr.append(variables)
        else:
            areVarsDeclared = True
        
    if hlt == 0 :
        raise Exception('No HLT instruction found')

def main(instructions): #,labels, varArr, memSpace
    global errorLineNumber
    output = ''
    preProcessInstruction(instructions)
    errorLineNumber = 0
    numOfVariables = len(varArr)
    memory = len(instructions) - numOfVariables

    for key in labels:
        lineNumber = bin(labels[key] - numOfVariables)
        lineNumber = lineNumber[2:]
        memSpace[key] = lineNumber.zfill(8)

    for eachVar in varArr:
        for key in eachVar:
            lineNumber = bin(eachVar[key] + memory)
            lineNumber = lineNumber[2:]
            memSpace[key] = lineNumber.zfill(8)
    for instruction in instructions:
        errorLineNumber += 1
        result = processInstruction(instruction.strip())
        if result == -1:
            result = '0101000000000000'
            output += result + '\n'
            break
        output += result + '\n'
        if result == '':
            output = ''
    return output


try :
    instructions = sys.stdin.read()
    instructions = instructions.split('\n')
    output = main(instructions)
    sys.stdout.write(output)
except Exception as e:
    print(e)