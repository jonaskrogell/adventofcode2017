import sys


class myProgram:
    queues = {}

    def __init__(self, instructions, id):
        self.instructions = instructions
        self.registry = {'p': id}
        self.id = id
        self.pos = 0
        self.queues[id] = []
        self.sent_values = 0

    def execute(self):
        if self.pos < 0 or self.pos >= len(self.instructions):
            return False
        instruction = self.instructions[self.pos].split(' ')
        op = instruction[0]
        reg = instruction[1]
#        print('Executing:', self.pos, op, reg, instruction)
        try:
            value1 = int(reg)
        except ValueError:
            if reg not in self.registry:
                self.registry[reg] = 0
            value1 = self.registry[reg]

        if len(instruction) > 2:
            try:
                value2 = int(instruction[2])
            except ValueError:
                value2 = self.registry[instruction[2]]
        else:
            value2 = None

        if op == 'snd':
#            print(self.id, 'Send reg value:', reg, value1)
            for queue in self.queues:
                if queue != self.id:
                    self.queues[queue].append(value1)
            self.sent_values += 1
        elif op == 'rcv':
            if len(self.queues[self.id]) == 0:
#                print(self.id, 'Queue empty')
                return False
            self.registry[reg] = self.queues[self.id].pop(0)
#            print(self.id, 'Received:', self.registry[reg])
        elif op == 'set':
            self.registry[reg] = value2
        elif op == 'add':
            self.registry[reg] += value2
        elif op == 'mul':
            self.registry[reg] *= value2
        elif op == 'mod':
            self.registry[reg] = self.registry[reg] % value2
        elif op == 'jgz':
            if value1 > 0:
                self.pos += value2 - 1
        else:
            raise Exception('Unknown operator "%s"' % op)

#        print(self.id, 'After:', self.registry)
        self.pos += 1
        return True


instructions = []
for row in sys.stdin.read().strip().split('\n'):
    instructions.append(row)


programs = []
programs.append(myProgram(instructions, id=0))
programs.append(myProgram(instructions, id=1))

while True:
    status = []
    for program in programs:
        status.append(program.execute())
    if True not in status:
        break

for program in programs:
    print(program.id, program.registry, program.sent_values)
