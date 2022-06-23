const main = require('./main')

test('Verify valid type C: not R0 R1', () => {
  expect(main.verifyTypeC(['not', 'R0', 'R1'])).toBe(0)
})

test('Verify invalid type C: not R0', () => {
  expect(main.verifyTypeC(['not', 'R0'])).toBe(-1)
})

test('Verify invalid type C: cmp R0 $100', () => {
  expect(main.verifyTypeC(['cmp', 'R0', '$100'])).toBe(-1)
})

test('Verify invalid type C: cmp R0 X', () => {
  expect(main.verifyTypeC(['cmp', 'R0', 'X'])).toBe(-1)
})

test('Verify valid type D: ld R1 X', () => {
  expect(main.verifyTypeD(['ld', 'R1', 'X'])).toBe(0)
})

test('Verify invalid type D: ld R1', () => {
  expect(main.verifyTypeD(['ld', 'R1'])).toBe(-1)
})

test('Verify invalid type D: ld X', () => {
  expect(main.verifyTypeD(['ld', 'X'])).toBe(-1)
})
test('Verfying valid TypeA reg using: mul reg0 reg1 reg2', () => {
  expect(main.verifyTypeA(['mul', 'R0', 'R1', 'R2'])).toBe(0)
})

test('Verfying invalid TypeA reg using: mul reg0 reg1', () => {
  expect(main.verifyTypeA(['mul', 'R0', 'R1'])).toBe(-1)
})

test('Verfying invalid TypeA reg using: mul reg0 reg1 $30', () => {
  expect(main.verifyTypeA(['mul', 'R0', 'R1', '$30'])).toBe(-1)
})

test('Verfying invalid TypeA reg using: mul reg0 reg1 X', () => {
  expect(main.verifyTypeA(['mul', 'R0', 'R1', 'X'])).toBe(-1)
})

test('Verfying valid TypeB reg using: ls reg0 $30', () => {
  expect(main.verifyTypeB(['ls', 'R0', '$30'])).toBe(0)
})

test('Verfying invalid TypeB reg using: ls $30', () => {
  expect(main.verifyTypeB(['ls', '$30'])).toBe(-1)
})

test('Verfying invalid TypeB reg using: ls reg1 reg2', () => {
  expect(main.verifyTypeB(['ls', 'R1', 'R2'])).toBe(-1)
})

test('Verfying invalid TypeB reg using: mul reg0 X', () => {
  expect(main.verifyTypeB(['mul', 'R0', 'X'])).toBe(-1)
})

// type E
test('verifying memory address type E', () => {
  expect(main.verifyTypeE(['jmp', 'mem_addr'])).toBe(0)
})

test('verifying invalid memory address type E', () => {
  expect(main.verifyTypeE(['jmp', '$30'])).toBe(-1)
})

test('verifying invalid memory address type E', () => {
  expect(main.verifyTypeE(['jmp', 'R0'])).toBe(-1)
})

test('Verifying invalid memory address type E', () => {
  expect(main.verifyTypeE(['jmp'])).toBe(-1)
})

test('Verifying type F', () => {
  expect(main.verifyTypeF(['hlt'])).toBe(0)
})

test('Verifying invalid type F', () => {
  expect(main.verifyTypeF(['hlt', 'R0'])).toBe(-1)
})
