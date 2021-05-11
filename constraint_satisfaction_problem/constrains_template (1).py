from random import shuffle


class CSP:
    def __init__(self, variables, domains, neighbours, constraints):
        self.variables = variables
        self.domains = domains
        self.neighbours = neighbours
        self.constraints = constraints

    def backtracking_search(self):
        return self.recursive_backtracking({})

    def recursive_backtracking(self, assignment):
        if self.is_complete(assignment):
            return assignment
        unassigned = self.select_unassigned_variable(assignment)
        for value in self.order_domain_values(unassigned, assignment):
            if self.is_consistent(unassigned, value, assignment):
                        assignment[unassigned] = value
                        result = self.recursive_backtracking(assignment)
                        if result is not None:
                            return result
                        assignment.pop(unassigned)

        return None

    def select_unassigned_variable(self, assignment):
        for variable in self.variables:
            if variable not in assignment:
                return variable

    def is_complete(self, assignment):
        for variable in self.variables:
            if variable not in assignment:
                return False
        return True

    def order_domain_values(self, variable, assignment):
        all_values = self.domains[variable][:]
        # shuffle(all_values)
        return all_values

    def is_consistent(self, variable, value, assignment):
        if not assignment:
            return True

        for constraint in self.constraints.values():
            for neighbour in self.neighbours[variable]:
                if neighbour not in assignment:
                    continue

                neighbour_value = assignment[neighbour]
                if not constraint(variable, value, neighbour, neighbour_value):
                    return False
        return True


def create_australia_csp():
    wa, q, t, v, sa, nt, nsw = 'WA', 'Q', 'T', 'V', 'SA', 'NT', 'NSW'
    values = ['Red', 'Green', 'Blue']
    variables = [wa, q, t, v, sa, nt, nsw]
    domains = {
        wa: values[:],
        q: values[:],
        t: values[:],
        v: values[:],
        sa: values[:],
        nt: values[:],
        nsw: values[:],
    }
    neighbours = {
        wa: [sa, nt],
        q: [sa, nt, nsw],
        t: [],
        v: [sa, nsw],
        sa: [wa, nt, q, nsw, v],
        nt: [sa, wa, q],
        nsw: [sa, q, v],
    }

    def constraint_function(first_variable, first_value, second_variable, second_value):
        return first_value != second_value

    constraints = {
        wa: constraint_function,
        q: constraint_function,
        t: constraint_function,
        v: constraint_function,
        sa: constraint_function,
        nt: constraint_function,
        nsw: constraint_function,
    }

    return CSP(variables, domains, neighbours, constraints)


def create_south_america_csp():
    ve, co, gua, su, gue, ec, pe, br, bo, pa, ch, ar, ur = 'VE', 'CO', 'QUA', 'SU', 'QUE', 'EC', 'PE', 'BR', 'BO', 'PA', 'CH', 'AR', 'UR'
    values = ['Red', 'Green', 'Blue', 'Yellow']
    variables = [ve, co, gua, su, gue, ec, pe, br, bo, pa, ch, ar, ur]
    domains = {
        ve: values[:],
        co: values[:],
        gua: values[:],
        su: values[:],
        gue: values[:],
        ec: values[:],
        pe: values[:],
        br: values[:],
        bo: values[:],
        pa: values[:],
        ch: values[:],
        ar: values[:],
        ur: values[:]
    }
    neighbours = {
        ve: [co, gua, br],
        co: [ve, ec, br, pe],
        gua: [ve, su, br],
        su: [gua, br, gue],
        gue: [br, su],
        ec: [pe, co],
        pe: [ec, co, br, bo, ch],
        br: [gue, su, gua, ve, co, pe, bo, pa, ur, ar],
        bo: [pe, br, pa, ar, ch],
        pa: [bo, br, ar],
        ch: [pe, bo, ar],
        ar: [ch, ur, pa, bo],
        ur: [ar, br]
    }

    def constraint_function(first_variable, first_value, second_variable, second_value):
        return first_value != second_value

    constraints = {
        ve: constraint_function,
        co: constraint_function,
        gua: constraint_function,
        su: constraint_function,
        gue: constraint_function,
        ec: constraint_function,
        pe: constraint_function,
        br: constraint_function,
        bo: constraint_function,
        pa: constraint_function,
        ch: constraint_function,
        ar: constraint_function,
        ur: constraint_function
    }

    return CSP(variables, domains, neighbours, constraints)

if __name__ == '__main__':
    australia = create_australia_csp()
    result = australia.backtracking_search()
    for area, color in sorted(result.items()):
        print("{}: {}".format(area, color))

    print('************SOUTH AMERICA********************')
    south_america = create_south_america_csp()
    result_2 = south_america.backtracking_search()
    for area, color in sorted(result_2.items()):
        print("{}: {}".format(area, color))
    # Check at https://mapchart.net/australia.html

