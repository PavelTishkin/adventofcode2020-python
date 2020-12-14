import re


def main():
    input_file = open('input/day14.txt', 'r')
    instructions = list(map(lambda l: l.strip(), input_file.readlines()))
    input_file.close()

    memory = {}
    programs = load_instructions_into_programs(instructions)
    run_programs(programs, memory)
    print('Answer 1: {}'.format(get_memory_sum(memory)))

    memory = {}
    programs = load_instructions_into_programs(instructions)
    run_programs(programs, memory, 2)
    print('Answer 2: {}'.format(get_memory_sum(memory)))


def update_memory(mask, command, memory, version=1):

    if version == 1:
        num_binary = '{0:b}'.format(command['num']).zfill(len(mask))
        for i in range(len(num_binary)):
            if mask[i] != 'X':
                num_binary = num_binary[:i] + mask[i] + num_binary[i+1:]

        if version == 1:
            memory[command['mem']] = int(num_binary, 2)
    elif version == 2:
        mem_binary = '{0:b}'.format(command['mem']).zfill(len(mask))
        for i in range(len(mem_binary)):
            if mask[i] != '0':
                mem_binary = mem_binary[:i] + mask[i] + mem_binary[i+1:]

        mem_address_values = []
        get_quantum_memory_address_values(mem_binary, mem_address_values)

        for memory_address in mem_address_values:
            memory[memory_address] = command['num']


def get_quantum_memory_address_values(num_val, mem_values):
    bit_loc = num_val.find('X')
    if bit_loc == -1:
        mem_values.append(int(num_val, 2))
    else:
        get_quantum_memory_address_values(num_val[:bit_loc] + '0' + num_val[bit_loc+1:], mem_values)
        get_quantum_memory_address_values(num_val[:bit_loc] + '1' + num_val[bit_loc + 1:], mem_values)


def run_program(program, memory, version=1):
    for command in program['commands']:
        update_memory(program['mask'], command, memory, version)


def run_programs(programs, memory, version=1):
    for program in programs:
        run_program(program, memory, version)


def get_memory_sum(memory):
    return sum(memory.values())


def load_instructions_into_programs(instructions):
    programs = []
    program = {}
    for i, instruction in enumerate(instructions):
        if instruction.startswith('mask'):
            if len(program.keys()) > 0:
                programs.append(program)
                program = {}
            program['mask'] = instruction.strip()[7:]
            program['commands'] = []
        else:
            r = re.match(r'mem\[(\d*)] = (\d*)', instruction.strip())
            command = {'mem': int(r.group(1)), 'num': int(r.group(2))}
            program['commands'].append(command)
            if i == len(instructions) - 1:
                programs.append(program)

    return programs


if __name__ == '__main__':
    main()
