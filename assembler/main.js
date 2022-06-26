<<<<<<< HEAD
const map = require('./map')

=======
// Does not work at the moment.
>>>>>>> 4fb6b449a2c040ad62dd66b42b2af5749fcba89a
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
  // TODO Verify the last operand
  return binary
}
