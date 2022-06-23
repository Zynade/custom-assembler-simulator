
function main (instruction) {
  instruction = instruction.split(' ')
  let binary = ''
  if (!opcode[instruction[0]]) {
    // TODO: raise exception
  }
  const ahhh = opcode[instruction[0]].verify(instruction)
  if (aahh > -1) {
    binary += opcode[instruction[0]].binaryeq[ahhh]
  } else {
    // TODO: raise exception
  }
  for (let i = 1; i < instruction.length - 1; i++) {
    if (!registers[instruction[i]]) {
      binary += instruction[i]
    } else {
      // TODO raise error
    }
  }
  // TODO Verify the last operand
  return binary
}
