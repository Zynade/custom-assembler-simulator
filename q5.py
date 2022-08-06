import math

def get_addr_pins(mem_space, cell_size):
    mem_space_in_bits = get_mem_space_in_bits(mem_space)
    num_addr = math.ceil( mem_space_in_bits / cell_size ) 
    addr_len = math.ceil(math.log2(num_addr))
    return addr_len

def solve_q1(mem_space, cell_size):
    if cell_size == 0:
        cell_size = 16
    instr_len = int(input("Instruction length in bits: "))
    reg_len = int(input("Register length in bits: "))

    mem_space_in_bits = get_mem_space_in_bits(mem_space)
    num_addr = math.ceil( mem_space_in_bits / cell_size ) 
    addr_len = math.ceil(math.log2(num_addr))   
    opcode_len = instr_len - addr_len - reg_len
    filler_bits = instr_len - opcode_len - 2 * reg_len

    # max_num_of_instr = mem_space_in_bits // instr_len
    max_num_of_instr = 2 ** (opcode_len)
    # max_num_of_reg = mem_space_in_bits // reg_len
    max_num_of_reg = 2 ** (reg_len)

    print("Minimum bits needed to represent an address:", addr_len)
    print("Number of bits needed by opcode: ", opcode_len)
    print("Number of filler bits in instruction type 2: ", filler_bits)
    print("Maximum number of instructions:", max_num_of_instr)
    print("Maximum number of registers:", max_num_of_reg)
    

def solve_q2_type1(mem_space, cell_size):

    # Type 1 queries:
    cpu_bits = int(input("Number of bits in CPU: "))
    if cell_size == 0:
        cell_size = cpu_bits
    print("How do you want the memory to be addressed?")
    print("1. Bit Addressable Memory")
    print("2. Nibble Addressable Memory")
    print("3. Byte Addressable Memory")
    print("4. Word Addressable Memory")
    new_mem_addr = int(input())
    if new_mem_addr == 1:
        new_cell_size = 1
    elif new_mem_addr == 2:
        new_cell_size = 4
    elif new_mem_addr == 3:
        new_cell_size = 8
    elif new_mem_addr == 4:
        new_cell_size = cpu_bits
    else:
        print("Invalid input")
        return
    if cell_size == new_cell_size:
        print("No change in memory address")
        return

    change_in_pins = get_addr_pins(mem_space, new_cell_size) - get_addr_pins(mem_space, cell_size)
    if change_in_pins < 0:
        print("Pins saved: ", -change_in_pins)
    else:
        print("Extra pins required: ", change_in_pins)

def solve_q2_type2():
    cpu_bits = int(input("Number of bits in CPU: "))
    addr_pins = int(input("Number of address pins: "))
    print("How is the memory addressed?")
    print("1. Bit Addressable Memory")
    print("2. Nibble Addressable Memory")
    print("3. Byte Addressable Memory")
    print("4. Word Addressable Memory")
    mem_addr = int(input())
    if mem_addr == 1:
        cell_size = 1
    elif mem_addr == 2:
        cell_size = 4
    elif mem_addr == 3:
        cell_size = 8
    elif mem_addr == 4:
        cell_size = cpu_bits
    else:
        print("Invalid input")
        return

    mem_size_in_bytes = cell_size * (2 ** (addr_pins - 3))
    print(f"The main memory can be {mem_size_in_bytes} bytes.") 

def get_mem_space_in_bits(mem_space):
    num, unit = mem_space.split()
    if unit[-1] == 'B':
        bits = 8
    else:
        bits = 1
    if len(unit) > 1:
        if unit[0].upper() == 'K':
            bits *= 1024
        elif unit[0].upper() == 'M':
            bits *= 1024 * 1024
        elif unit[0].upper() == 'G':
            bits *= 1024 * 1024 * 1024
    return int(num) * bits


def main():
    mem_space = input("Memory space (eg. 16 GB): ")

    print("How is the memory addressed?")
    print("1. Bit Addressable Memory")
    print("2. Nibble Addressable Memory")
    print("3. Byte Addressable Memory")
    print("4. Word Addressable Memory")
    mem_addr = int(input())
    if mem_addr == 1:
        cell_size = 1
    elif mem_addr == 2:
        cell_size = 4
    elif mem_addr == 3:
        cell_size = 8
    elif mem_addr == 4:
        cell_size = 0 # Using 0 to represent word addressable memory
    else:
        print("Invalid input")
        return

    solve_q1(mem_space, cell_size)
    solve_q2_type1(mem_space, cell_size)
    solve_q2_type2()

if __name__ == '__main__':
    main()
    