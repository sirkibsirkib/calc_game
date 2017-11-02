
class Operation:
    def __init__(self, printable, func):
        self.printable = printable;
        self.func = func

    def apply_to(self, x):
        return self.func(x)

    def __repr__(self):
        return self.printable


# class stores dict of solutions
# solution -> (depth, op_sequence)
class Findings:
    def __init__(self):
        self.solutions = dict();

    def depth_of_solution(self, number):
        if number not in self.solutions:
            return -1
        return self.solutions[number][0]

    def update_solution(self, number, depth, solution_sequence):
        self.solutions[number] = (depth, solution_sequence)

    def __repr__(self):
        s = ''
        for (k, v) in self.solutions.items():
            s += '\t' + str(v[1]) + ' => ' + str(k) + '\n'
        return s


sentinel = object()
def derive(start_from_number, operations, max_depth, findings, depth_so_far = 1,
            operation_sequence = [], current_number=sentinel):
    if current_number == sentinel:
        # this is stupid
        current_number = start_from_number

    if depth_so_far > max_depth:
        return

    for o in operations:
        next_num = o.apply_to(current_number)
        found_in_depth = findings.depth_of_solution(next_num)
        next_seq = operation_sequence + [o]
        if found_in_depth == -1 or found_in_depth > depth_so_far:
            # update this solution
            findings.update_solution(next_num, depth_so_far, next_seq   )

        derive(start_from_number, operations, max_depth, findings, depth_so_far=depth_so_far+1,
                operation_sequence = next_seq, current_number=next_num)

ops = [
    Operation('+5', lambda x : x+5),
    Operation('-2', lambda x : x-2),
    Operation('/2', lambda x : x/2),
    Operation('<0>', lambda x : x*10),
]

f = Findings()

start_num = 4
max_steps = 3
derive(start_num, ops, max_steps, f)
print('depth from', start_num, ':\n', f)
