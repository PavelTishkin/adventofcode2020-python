from hgc_compiler.hgc import HandheldGameConsole


def main():
    input_file = open('input/day8.txt', 'r')
    file_lines = list(map(lambda l: l.strip(), input_file.readlines()))

    hgc = HandheldGameConsole()
    hgc.load_instructions(file_lines)
    hgc.run()
    print('Answer 1: {}'.format(hgc.get_acc()))

    for i in range(len(file_lines)):
        hgc.reset()
        if hgc.get_instructions()[i].get_action() == 'nop':
            hgc.get_instructions()[i].set_action('jmp')
        elif hgc.get_instructions()[i].get_action() == 'jmp':
            hgc.get_instructions()[i].set_action('nop')
        else:
            continue

        hgc.run()
        if hgc.get_termination() == 'standard':
            print('Answer 2: {}'.format(hgc.get_acc()))
            break


if __name__ == '__main__':
    main()
