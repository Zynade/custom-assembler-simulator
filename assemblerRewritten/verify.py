def verifyTypeA(instruction):
    if len(instruction)==4 and instruction[3][0]=='R':
        return 0
    return -1

def verifyTypeB(instruction):
    if len(instruction)==3 and instruction[2][0]=='$':
        return 0
    return -1

def verifyTypeC(instruction):
    if len(instruction)==3 and instruction[2][0]=='R':
        return 0
    return -1

def verifyMove(instruction):
    if len(instruction)==3 and instruction[2][0]=='$':
        return 1
    elif len(instruction)==3 :
        return 0
    return -1

def verifyTypeD(instruction):
    if len(instruction)==3:
    # Type D instructions are like: ld reg mem_addr, st reg mem_addr.
    # The last argument must be a variable. It cannot be an immediate value or a label.
        memAddr = instruction[2]
    # TODO: Add a check to ensure memAddr is NOT a label.
        if memAddr[0] != '$':
            return 0
    return -1

def verifyTypeE(instruction):
    if len(instruction)==2:
    # Type E instructions are like: jmp mem_addr. Here, mem_addr must be a label. It cannot be a variable or an immediate value.
        memAddr = instruction[1]
        # if memAddr in forbiddenKeywords and memAddr[0] != '$': #TODO|| main.labels.includes(memAddr)) {
        #     return 0 
    # // NOTE: Add a check to ensure memAddr is a label.
        if memAddr[0] != '$':
            return 0
    return -1

def verifyTypeF(instruction):
    if len(instruction)==1:
        return 0
    return -1

