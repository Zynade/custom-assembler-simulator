const verification = require('./verify')

// Todo need to complete regs
const registers = {
  R0: '000',
}

//Todo need to complete opcode
const opcode = {
  mult: {
    verify: verification.verifyTypeA(instruction) 
    binaryeq: ['1011000']
  }
}

// Todo need to make memory space

//temp function for testing
function dicttemp (regist) {
  return registers[regist]
}
