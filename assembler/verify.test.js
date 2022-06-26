const verify = require('./verify')

test('Verfying valid TypeA reg using: mul reg0 reg1 reg2', () => {
  expect(
    verify.verifyTypeA(['mul', 'R0', 'R1', 'R2'])
  ).toBe(0)
})

test('Verfying invalid TypeA reg using: mul reg0 reg1', () => {
  expect(verify.verifyTypeA(['mul', 'R0', 'R1'])).toBe(-1)
})

test('Verfying invalid TypeA reg using: mul reg0 reg1 $30', () => {
  expect(verify.verifyTypeA(['mul', 'R0', 'R1', '$30'])).toBe(-1)
})

test('Verfying invalid TypeA reg using: mul reg0 reg1 X', () => {
  expect(verify.verifyTypeA(['mul', 'R0', 'R1', 'X'])).toBe(-1)
})

test('Verfying valid TypeB reg using: ls reg0 $30', () => {
  expect(verify.verifyTypeB(['ls', 'R0', '$30'])).toBe(0)
})

test('Verfying invalid TypeB reg using: ls $30', () => {
  expect(verify.verifyTypeB(['ls', '$30'])).toBe(-1)
})

test('Verfying invalid TypeB reg using: ls reg1 reg2', () => {
  expect(verify.verifyTypeB(['ls', 'R1', 'R2'])).toBe(-1)
})

test('Verfying invalid TypeB reg using: mul reg0 X', () => {
  expect(verify.verifyTypeB(['mul', 'R0', 'X'])).toBe(-1)
})

test('Verifying valid type C: not R0 R1', () => {
  expect(verify.verifyTypeC(['not', 'R0', 'R1'])).toBe(0)
})

test('Verifying invalid type C: not R0', () => {
  expect(verify.verifyTypeC(['not', 'R0'])).toBe(-1)
})

test('Verifying invalid type C: cmp R0 $100', () => {
  expect(verify.verifyTypeC(['cmp', 'R0', '$100'])).toBe(-1)
})

test('Verifying invalid type C: cmp R0 X', () => {
  expect(verify.verifyTypeC(['cmp', 'R0', 'X'])).toBe(-1)
})

test('Verifying valid type D: ld R1 X', () => {
  expect(verify.verifyTypeD(['ld', 'R1', 'X'])).toBe(0)
})

test('Verifying invalid type D: ld R1', () => {
  expect(verify.verifyTypeD(['ld', 'R1'])).toBe(-1)
})

test('Verifying invalid type D: ld X', () => {
  expect(verify.verifyTypeD(['ld', 'X'])).toBe(-1)
})

// type E
test('Verifying valid memory address type E', () => {
  expect(verify.verifyTypeE(['jmp', 'mem_addr'])).toBe(0)
})

test('Verifying invalid memory address type E', () => {
  expect(verify.verifyTypeE(['jmp', '$30'])).toBe(-1)
})

test('Verifying invalid memory address type E', () => {
  expect(verify.verifyTypeE(['jmp', 'R0'])).toBe(-1)
})

test('Verifying invalid memory address type E', () => {
  expect(verify.verifyTypeE(['jmp'])).toBe(-1)
})

test('Verifying type F', () => {
  expect(verify.verifyTypeF(['hlt'])).toBe(0)
})

test('Verifying invalid type F', () => {
  expect(verify.verifyTypeF(['hlt', 'R0'])).toBe(-1)
})
