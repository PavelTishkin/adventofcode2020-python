class HandheldGameConsole:
    """
    Class used to hold logic for executing Handheld Game Console code
    """

    def __init__(self):
        """
        Initialize HGC data
        """
        self.instructions_list = []
        self.instructions = []
        self.ip = 0
        self.ip_called = set()
        self.acc = 0
        self.termination = ""

    def load_instructions(self, instructions_list):
        """
        Parse individual instructions from a string
        :param instructions_list: List of instruction strings
        """
        self.instructions_list = instructions_list
        self.instructions = []
        for instruction_str in instructions_list:
            inst = Instruction()
            inst.parse_instruction(instruction_str)
            self.instructions.append(inst)

    def run(self):
        """
        Execute compiler code
        """
        self.termination = ""
        while True:
            self.ip_called.add(self.ip)
            next_instruction = self.instructions[self.ip]
            # NOP operation
            if next_instruction.get_action() == 'nop':
                self.ip += 1
            # ACC operation
            elif next_instruction.get_action() == 'acc':
                self.acc += next_instruction.get_parameter1()
                self.ip += 1
            # JMP operation
            elif next_instruction.get_action() == 'jmp':
                self.ip += next_instruction.get_parameter1()

            # Reached end of instructions set
            if self.ip == len(self.instructions):
                self.termination = "standard"
                break

            # Detected infinite loop
            if self.ip in self.ip_called:
                self.termination = "inf_loop"
                break

    def reset(self):
        """
        Reset console internal data for a new execution
        """
        self.load_instructions(self.instructions_list)
        self.ip = 0
        self.ip_called = set()
        self.acc = 0
        self.termination = ""

    def get_instructions(self):
        return self.instructions

    def get_acc(self):
        return self.acc

    def get_termination(self):
        return self.termination


class Instruction:
    """
    Holds data for a single instruction
    """

    def __init__(self):
        """
        Initialize instruction data
        """
        self.action = ""
        self.parameter1 = 0

    def parse_instruction(self, inst_str):
        """
        Parse instruction from instruction string
        :param inst_str: Instruction string
        """
        inst_data = inst_str.split()
        self.action = inst_data[0]
        self.parameter1 = int(inst_data[1])

    def get_action(self):
        return self.action

    def set_action(self, action):
        self.action = action

    def get_parameter1(self):
        return self.parameter1

    def set_parameter1(self, parameter):
        self.parameter1 = parameter

    def __repr__(self):
        return f'{self.action} {self.parameter1}'
