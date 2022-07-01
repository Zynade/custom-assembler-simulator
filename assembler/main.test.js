const assembler = require('./main')

test('assembler: mul R3 R1 R2', () => {
  expect(assembler.processInstruction('mul R3 R1 R2')).toBe('1011000011001010')
})

test('assembler: mov R1 $10', () => {
  expect(assembler.processInstruction('mov R1 $10')).toBe('1001000100001010')
})

test('assembler: mov R2 $100', () => {
  expect(assembler.processInstruction('mov R2 $100')).toBe('1001001001100100')
})

test('assembler: mov R2 R1', () => {
  expect(assembler.processInstruction('mov R2 R1')).toBe('1001100000010001')
})

test('hlt', () => {
  // expect(assembler.processInstruction('hlt')).toBe('0101000000000000')
  expect(assembler.processInstruction('hlt')).toBe(-1)
})
