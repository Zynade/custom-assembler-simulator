const map = require('./map')

test('Verifying if Register obj gives correct value with R0', () => {
  expect(map.dicttemp('R0')).toBe('000')
})

test('Verifying if Register obj gives correct value with R6', () => {
  expect(map.dicttemp('R6')).toBe('110')
})

test('Verifying if Register obj handles errors FLAGS', () => {
  expect(map.dicttemp('FLAGS')).toBe(undefined)
})

test('Verifying if OPcode obj gives correct opcode in case of : add R1 R2 R3', () => {
  expect(map.optest('add R1 R2 R3')).toBe('1000000')
})

test('Verifying if OPcode obj gives correct opcode in case of : mov R1 $10', () => {
  expect(map.optest('mov R1 $10')).toBe('10010')
})

test('Verifying if OPcode obj gives correct opcode in case of : mul R1 R2 R4', () => {
  expect(map.optest('mul R1 R2 R3')).toBe('1011000')
})

test('Verifying if OPcode obj gives correct opcode in case of : add R1 R2 R3 R4', () => {
  expect(map.optest('add R1 R2 R3 R4')).toBe(-1)
})

test('Verifying if OPcode obj gives correct opcode in case of : add R1 R2 $45', () => {
  expect(map.optest('add R1 R2 $45')).toBe(-1)
})

test('Verifying if OPcode obj handles error efd R1 R2 R3', () => {
  expect(map.optest('efd R1 R2 R3')).toBe(-1)
})

test('Verifying immteger value', () => {
  expect(map.immDecToBin('$45')).toBe('00101101')
})

test('Verifying immteger value', () => {
  expect(map.immDecToBin('$0')).toBe('00000000')
})

test('Verifying immteger value', () => {
  expect(map.immDecToBin('$255')).toBe('11111111')
})

test('Verifying immteger value for incorrect value', () => {
  expect(map.immDecToBin('$256')).toBe(-1)
})

test('Verifying immteger value', () => {
  expect(map.immDecToBin('$10')).toBe('00001010')
})

test('Verifying immteger value for NaN', () => {
  expect(map.immDecToBin('$hello, world!')).toBe(-1)
})
