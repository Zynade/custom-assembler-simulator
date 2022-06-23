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

function verifyTypeC (array) {
  return -1
}

function verifyTypeD (array) {
  return -1
}

function verifyTypeE (instruction) {
  return -1
}

function verifyTypeF (instruction) {
  return -1
}

// Todo need to add cmp and mov verification

module.exports = { verifyTypeA, verifyTypeB, verifyTypeC, verifyTypeD, verifyTypeE, verifyTypeF }
