const map = require('./map')
const fs = require('fs')
const FileI = fs.readFileSync('./assembler/input.txt', 'utf8')

function processInstruction (instruction) {
  instruction = instruction.split(' ')
  let binary = ''
  // console.log(instruction)
  if (instruction[0] === 'hlt') {
    return -1 // check
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
  // console.log(binary)
  for (let i = 1; i < instruction.length - 1; i++) {
    if (map.registers[instruction[i]] !== undefined) {
      binary += map.registers[instruction[i]]
    } else {
      throw Error("Invalid register encountered")
    }
  }
  // const a = instruction[instruction.length - 1]
  // console.log(a)
  // console.log(typeof (a))
  // console.log(map.registers[a])
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
  // console.log(binary)
  return binary
}

function main () {
  // let numInstructions
  const instructions = FileI.split('\n')
  let result
  let output = ''
  for (let i = 0; i < instructions.length; i++) {
    // console.log(instructions[i])
    result = processInstruction(instructions[i].trim())
    // result += '\n'
    if (result === -1) { // condition checking for hlt case
      result = '0101000000000000' // opcode for hlt instruction
      output += result + '\n'
      break
    }
    output += result + '\n'
  }
  fs.writeFileSync('./assembler/output.txt', output)
  //
}
// console.log(processInstruction(''))
main()
module.exports = { processInstruction }
