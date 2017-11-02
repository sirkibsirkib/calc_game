from operations import Operation

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

    def print_sols_with_min(self, min_steps, solution_predicate):
        s = ''
        for (k, v) in self.solutions.items():
            if v[0] >= min_steps and solution_predicate(k):
                s += '\t' + str(v[1]) + ' => ' + str(k) + '\n'
        return s


sentinel = object()
def derive(start_from_number, operations, max_depth, findings, depth_so_far = 1,
            operation_sequence = [], current_number=sentinel):
    if current_number == sentinel:
        # cant use another arg as default value for arg. need to use this sentinel nonsense
        current_number = start_from_number

    if depth_so_far > max_depth:
        # stop condition
        return

    for o in operations:
        # apply all possible args
        next_num = o.apply_to(current_number)
        found_in_depth = findings.depth_of_solution(next_num)
        next_seq = operation_sequence + [o]

        if found_in_depth == -1 or found_in_depth > depth_so_far:
            # update this solution
            findings.update_solution(next_num, depth_so_far, next_seq)

        derive(start_from_number, operations, max_depth, findings, depth_so_far=depth_so_far+1,
                operation_sequence = next_seq, current_number=next_num)


from operations import o_add, o_sub, o_insert, o_mult, o_div, o_map, o_flip, o_del
# USER INPUT BEGIN #################################

start_num = 14

# all printed solutions will have a shortest path with step# in this range
min_max_steps = (5, 5)

# 'solution' here refers to the number REACHABLE by operations
# use lambda x : True if you want all solutions
solution_predicate = lambda x : True


ops = [
    o_insert(6),
    o_add(9),
    o_div(8),
    o_flip,
]
# USER INPUT END #####################################

f = Findings()
derive(start_num, ops, min_max_steps[1], f)
print('depth from', start_num, ':\n', f.print_sols_with_min(min_max_steps[0], solution_predicate))
