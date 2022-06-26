const map = require('./map')

function main (instruction) {
  instruction = instruction.split(' ')
  let binary = ''
  if (!map.opcode[instruction[0]]) {
    // TODO: raise exception
  }
  const ISA = map.opcode[instruction[0]].verify(instruction)
  if (ISA > -1) {
    binary += map.opcode[instruction[0]].binaryeq[ISA]
  } else {
    // TODO: raise exception
  }
  for (let i = 1; i < instruction.length - 1; i++) {
    if (!map.registers[instruction[i]]) {
      binary += map.registers[instruction[i]]
    } else {
      // TODO raise error
    }
  }
  if (!map.registers[instruction[instruction.length - 1]]) {
    binary += map.registers[instruction[instruction.length - 1]]
  } else if (instruction[instruction.length - 1][0] === '$') {
    const immb = map.immtest(instruction[instruction.length - 1])
    if (immb !== -1) {
      binary += immb
    } else {
      // TODO raise error
    }
  } else {
    // Todo labels and variables
  }
  return binary
}
