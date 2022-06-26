function verifyTypeA (instruction) {
  if (instruction.length === 4 && instruction[3][0] === 'R') {
    return 0
  }
  return -1
}

function verifyTypeB (instruction) {
  if (instruction.length === 3 && instruction[2][0] === '$') {
    return 0
  }
  return -1
}
function verifyTypeC (instruction) {
  if (instruction.length === 3 && instruction[2][0] === 'R') {
    return 0
  }
  return -1
}
function verifyMove (instruction) {
  if (instruction.length === 3) {
    if (instruction[2][0] === '$') return 1;
    else return 0;
  }
  return -1
}
function verifyTypeD (instruction) {
  if (instruction.length === 3) {
    // Type D instructions are like: ld reg mem_addr, st reg mem_addr. 
    // The last argument must be a variable. It cannot be an immediate value or a label.
    const mem_addr = instruction[2]
    // TODO: check to make sure mem_addr is NOT a label -- mem_addr[mem_addr.length - 1] !== ':'
    if (mem_addr[0] !== '$') return 0;
  }
  return -1
}

function verifyTypeE (instruction) {
  if (instruction.length === 2) {
    // Type E instructions are like: jmp mem_addr. Here, mem_addr must be a label. It cannot be a variable or an immediate value.
    const mem_addr = instruction[1]
    // TODO: check to make sure mem_addr is a label -- mem_addr[mem_addr.length - 1] === ':'
    if (mem_addr[0] !== '$') return 0;
  }
  return -1
}

function verifyTypeF (instruction) {
  if (instruction.length === 1) return 0;
  else return -1
}

// Todo need to add cmp and mov verification

module.exports = { verifyTypeA, verifyTypeB, verifyTypeC, verifyTypeD, verifyTypeE, verifyTypeF,verifyMove }
