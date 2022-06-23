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
      verification.verifyTypeA(instruction)
    },
    binaryeq: ['1000000']
  },
  sub: {
    verify: (instruction) => {
      verification.verifyTypeA(instruction)
    },
    binaryeq: ['1000100']
  },
  mult: {
    verify: (instruction) => {
      verification.verifyTypeA(instruction)
    },
    binaryeq: ['1011000']
  },
  rs: {
    verify: (instruction) => {
      verification.verifyTypeB(instruction)
    },
    binaryeq: ['1100000']
  },
  ls: {
    verify: (instruction) => {
      verification.verifyTypeB(instruction)
    },
    binaryeq: ['1100100']
  },

  xor: {
    verify: (instruction) => {
      verification.verifyTypeA(instruction)
    },
    binaryeq: ['1101000']
  },
  or: {
    verify: (instruction) => {
      verification.verifyTypeA(instruction)
    },
    binaryeq: ['1101100']
  },
  and: {
    verify: (instruction) => {
      verification.verifyTypeA(instruction)
    },
    binaryeq: ['1110000']
  }

}

// Todo need to make memory space object . Also raise error if the memory space added is a keyword
// Todo add a forbidden keyword list

// temp function for testing
function dicttemp (regist) {
  return registers[regist]
}

module.exports = { opcode, registers, dicttemp }
