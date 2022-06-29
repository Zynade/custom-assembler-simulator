const verification = require('./verify')

// Todo need to complete regs
const registers = {
  R0: '000',
  R1: '001',
  R2: '010',
  R3: '011',
  R4: '100',
  R5: '101',
  R6: '110'
}

const opcode = {
  // Type A instructions:
  add: {
    verify: (instruction) => verification.verifyTypeA(instruction),
    binaryeq: ['1000000']
  },
  sub: {
    verify: (instruction) => verification.verifyTypeA(instruction),
    binaryeq: ['1000100']
  },
  mul: {
    verify: (instruction) => verification.verifyTypeA(instruction),
    binaryeq: ['1011000']
  },
  xor: {
    verify: (instruction) => verification.verifyTypeA(instruction),
    binaryeq: ['1101000']
  },
  or: {
    verify: (instruction) => verification.verifyTypeA(instruction),
    binaryeq: ['1101100']
  },
  and: {
    verify: (instruction) => verification.verifyTypeA(instruction),
    binaryeq: ['1110000']
  },

  // Type B instructions:
  mov: {
    // If verify returns 1 then it's a immediate instruction set, 0 for register, 1 for wrong instruction.
    verify: (instruction) => verification.verifyMove(instruction),
    binaryeq: ['1001100000', '10010']
  },
  rs: {
    verify: (instruction) => verification.verifyTypeB(instruction),
    binaryeq: ['11000']
  },
  ls: {
    verify: (instruction) => verification.verifyTypeB(instruction),
    binaryeq: ['11001']
  },

  // Type C instructions:
  div: {
    verify: (instruction) => verification.verifyTypeC(instruction),
    binaryeq: ['1011100000']
  },
  not: {
    verify: (instruction) => verification.verifyTypeC(instruction),
    binaryeq: ['1110100000']
  },
  cmp: {
    verify: (instruction) => verification.verifyTypeC(instruction),
    binaryeq: ['1111000000']
  },

  // Type D instructions:
  ld: {
    verify: (instruction) => verification.verifyTypeD(instruction),
    binaryeq: ['10100']
  },
  st: {
    verify: (instruction) => verification.verifyTypeD(instruction),
    binaryeq: ['10101']
  },

  // Type E instructions:
  jmp: {
    verify: (instruction) => verification.verifyTypeE(instruction),
    binaryeq: ['11111000']
  },
  jlt: {
    verify: (instruction) => verification.verifyTypeE(instruction),
    binaryeq: ['01100000']
  },
  jgt: {
    verify: (instruction) => verification.verifyTypeE(instruction),
    binaryeq: ['01101000']
  },
  je: {
    verify: (instruction) => verification.verifyTypeE(instruction),
    binaryeq: ['01111000']
  },

  // Type F instructions
  hlt: {
    verify: (instruction) => verification.verifyTypeF(instruction),
    binaryeq: ['0101000000000000']
  }
}

const variables = {
}

const forbiddenKeywords = ['add', 'sub', 'mov', 'ld', 'st', 'mul', 'div', 'rs', 'ls', 'xor', 'or', 'and', 'not', 'cmp', 'jmp', 'jlt', 'jgt', 'je', 'hlt', 'R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'FLAGS']

// Todo need to make memory space object . Also raise error if the memory space added is a keyword
// Todo add a forbidden keyword list

// temp function for testing
function dicttemp (regist) {
  const tmp = registers[regist]
  return tmp
}

function optest (instruction) {
  instruction = instruction.split(' ')
  const tmp = opcode[instruction[0]]
  if (tmp === undefined) {
    return -1
  }
  //   console.log(tmp.verify(instruction))
  if (tmp.verify(instruction) > -1) {
    return opcode[instruction[0]].binaryeq[tmp.verify(instruction)]
  }
  return -1
}

function immDecToBin (intermediate) {
  // This function converts the immediate number from decimal to its 8 bit binary number. If not possible, return -1.
  intermediate = intermediate.slice(1) // remove the $
  if (Number(intermediate) > 255 || Number(intermediate) < 0 || isNaN(Number(intermediate))) {
    return -1
  }
  return extendToNBits(Number(intermediate).toString(2), '0', 8)
}

function extendToNBits (word, charToAdd, n) {
  const initialLength = word.length
  for (let i = 0; i < n - initialLength; i++) {
    word = charToAdd + word
  }
  return word
}

// optest('add R1 R2 R3')

module.exports = { registers, opcode, variables, dicttemp, optest, forbiddenKeywords, immDecToBin }
