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
  expect(map.immtest('$45')).toBe('00101101')
})
