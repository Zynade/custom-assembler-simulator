const map = require('./map')

function processInstruction (instruction) {
  instruction = instruction.split(' ')
  let binary = ''
  if (instruction[0]==='hlt'){
    return -1                  //check
  }
  if (!map.opcode[instruction[0]]) {
    throw Error('Encountered a OP code not supported by the ISA');
  }
  const ISA = map.opcode[instruction[0]].verify(instruction)
  if (ISA > -1) {
    binary += map.opcode[instruction[0]].binaryeq[ISA]
  } else {
    throw Error("Invalid instruction set encountered")
  }
  for (let i = 1; i < instruction.length - 1; i++) {
    if (map.registers[instruction[i]] !== undefined) {
      binary += map.registers[instruction[i]]
    } else {
      throw Error("Invalid register encountered")
    }
  }
  if (instruction.length === 1) {
    return binary
  }
  if (map.registers[instruction[instruction.length - 1]] !== undefined) {
    binary += map.registers[instruction[instruction.length - 1]]
  } else if (instruction[instruction.length - 1][0] === '$') {
      const immb = map.immDecToBin(instruction[instruction.length - 1])
      if (immb !== -1) {
        binary += immb
      } else {
        throw Error("Encountered immediate value is not allowed")
      }
  } else {
    throw Error("Encountered invalid instruction")
  }
  return binary
}

function main(){
  let numInstructions
  let instructions = []//this will be the array where we will store all the instructions
  let result

  for (let i = 0; i < numInstructions; i++){
    result = processInstruction(instructions[i])
    if (result === -1){ //condition checking for hlt case
      result = "0101000000000000" //opcode for hlt instruction
      break
    }
  }

  //
}

module.exports = { processInstruction }