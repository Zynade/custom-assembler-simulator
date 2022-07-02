const map = require('./map')
const fs = require('fs')
const FileI = fs.readFileSync('./assembler/input.txt', 'utf8')

const labels = {}
const variables = {}

function processInstruction (instructionStr) {
  let binary = ''
  let instruction = removeWhitespace(instructionStr)
  let operation = instruction[0]
  // We check if the first word is a label.

  // The below code processes the instruction.
  // Process label declaration
  for (let i = 0; i < operation.length; i++) {
    if (operation[i] === ':') {
      // if the line contains only the label name, just go to the next line without appending any binary.
      if (instruction.length === 1) {
        return ''
      }
      const label = operation.slice(0, i++)
      instruction = removeWhitespace(instructionStr.slice(i))
      operation = instruction[0]
      break
    }
  }
  // console.log(instruction)
  if (instruction[0] === 'hlt') {
    return -1 // check
  }
  if (map.opcode[instruction[0]] === undefined) {
    throw Error('Encountered a OP code not supported by the ISA')
  }
  const ISA = map.opcode[operation].verify(instruction)
  if (ISA > -1) {
    binary += map.opcode[operation].binaryeq[ISA]
  } else {
    throw Error('Invalid instruction set encountered')
  }
  // console.log(binary)
  for (let i = 1; i < instruction.length - 1; i++) {
    if (map.registers[instruction[i]] !== undefined) {
      binary += map.registers[instruction[i]]
    } else {
      throw Error('Invalid register encountered')
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
      throw Error('Encountered immediate value is not allowed')
    }
  } else {
    throw Error('Encountered invalid instruction')
  }
  // console.log(binary)
  return binary
}

function removeWhitespace (string) {
  // Takes a string and trims all whitespace, replaces any instance of double space with a single space.
  return string.replace(/\s+/g, ' ').trim().split(' ')
}

function preprocessInstructions (instructions) {
  // This function loops throught the code and stores all variables and labels in their respective objects.
  let areVarsDeclared = false
  for (let lineNumber = 0; lineNumber < instructions.length; lineNumber++) {
    const instructionStr = instructions[lineNumber]
    let instruction = removeWhitespace(instructionStr)
    let operation = instruction[0]

    // Process variable declarations
    if (operation === 'var') {
      if (areVarsDeclared) {
        throw Error('Variable must be declared before any other instructions.')
      } else {
        const variable = instruction[1]
        if (instruction.length > 2) {
          throw Error('Invalid variable name: variable name cannot contain a space.')
        } else if (map.forbiddenKeywords.includes(variable)) {
          throw Error(`Invalid variable name: "${variable}" is a reserved keyword.`)
        } else if (map.variables.includes(variable)) {
          throw Error(`Invalid variable name: "${variable}" is already declared.`)
        }
        variables[variable] = null
      }
    } else {
      areVarsDeclared = true
    }

    // Process label declarations
    for (let i = 0; i < operation.length; i++) {
      if (operation[i] === ':') {
        const label = operation.slice(0, i++)
        if (map.forbiddenKeywords.includes(label)) {
          throw Error(`Invalid label: "${label}" is a reserved keyword.`)
        } else if (labels.includes(label)) {
          throw Error(`Invalid label: "${label}" is already declared.`)
        }
        instruction = removeWhitespace(instructionStr.slice(i))
        operation = instruction[0]
        labels[label] = lineNumber // TEMPORARY: will change it to the line's corresponding memory addres after memory space has beeen implemeneted.
        break
      }
    }
  }
}

function main () {
  // let numInstructions
  const instructions = FileI.split('\n')
  let result
  let output = ''

  preprocessInstructions(instructions)

  // main loop
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
