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

// Todo need to complete opcode
const opcode = {
  add: {
    verify: (instruction) => {
      return verification.verifyTypeA(instruction)
    },
    binaryeq: ['1000000']
  },
  sub: {
    verify: (instruction) => {
      return verification.verifyTypeA(instruction)
    },
    binaryeq: ['1000100']
  },
  mul: {
    verify: (instruction) => {
      return verification.verifyTypeA(instruction)
    },
    binaryeq: ['1011000']
  },
  rs: {
    verify: (instruction) => {
      return verification.verifyTypeB(instruction)
    },
    binaryeq: ['11000']
  },
  ls: {
    verify: (instruction) => {
      return verification.verifyTypeB(instruction)
    },
    binaryeq: ['11001']
  },

  xor: {
    verify: (instruction) => {
      return verification.verifyTypeA(instruction)
    },
    binaryeq: ['1101000']
  },
  or: {
    verify: (instruction) => {
      return verification.verifyTypeA(instruction)
    },
    binaryeq: ['1101100']
  },
  and: {
    verify: (instruction) => {
      return verification.verifyTypeA(instruction)
    },
    binaryeq: ['1110000']
  },
  mov: {
    verify: (instruction) => {
      return verification.verifyMov(instruction)
    },
    binaryeq: (verify) => verify === 1 ? ['1001000'] : ['1001100']
  // if verify returns 1 then it's a immediate instruction set, 0 for register,
  // -1 for wrong instruction.
  },
  cmp: {
    verify: (instruction) => {
      return verification.verifyCmp(instruction)
    },
    binaryeq: ['1111000']
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
  if (!tmp) {
    return -1
  }
  //   console.log(tmp.verify(instruction))
  if (tmp.verify(instruction) > -1) {
    return opcode[instruction[0]].binaryeq[tmp.verify(instruction)]
  }
  return -1
}

function immtest (intermediate) {
  intermediate = intermediate.slice(1) // remove the $
  if (Number(intermediate) > 255 || Number(intermediate) < 0) {
    return -1
  }
  return ch(Number(intermediate).toString(2), '0', 8)
}

function ch (word, charToAdd, length) {
  const initial = word.length
  for (let i = 0; i < length - initial; i++) {
    word = charToAdd + word
  }
  return word
}

optest('add R1 R2 R3')

module.exports = { registers, opcode, variables, dicttemp, optest, forbiddenKeywords, immtest }
