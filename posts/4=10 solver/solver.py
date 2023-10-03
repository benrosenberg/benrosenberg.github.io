from itertools import product, permutations
import sys

numbers = list('5585')
number_arrangements = list(permutations(numbers))
operator_arrangements = list(product(['+', '-', '*', '/'], repeat=3))

# print(operator_arrangements)

# sys.exit()
paren_arrangements = [(0,4), (1,4), (2,4), (0,3), (0,2), (1,3)]

def attempt(joined):
    try:
        if abs(eval(joined) - 10.0) < 0.1:
            print('Answer:', ''.join(slots).replace('/', '÷'))
            print(eval(joined))
            return True
        else:
            return False
    except ZeroDivisionError:
        return False

for number_arrangement in number_arrangements:
    for operator_arrangement in operator_arrangements:
        for paren_arrangement in paren_arrangements:
            # P N O P N (O P) (P O) N P O N P -> 12 slots
            slots = [''] * (3 + 4 + 5)
            a, b, c, d = number_arrangement
            f, g, h = operator_arrangement
            p, q = paren_arrangement
            # first paren
            if p == 2: slots[6] = '('
            elif p == 0: slots[0] = '('
            else: slots[3] = '('
            # second paren
            if q == 2: slots[5] = ')'
            elif q == 3: slots[8] = ')'
            elif q == 4: slots[11] = ')'
            # numbers
            slots[1] = a
            slots[4] = b
            slots[7] = c
            slots[10] = d
            # operators
            slots[2] = f
            slots[9] = h
            if slots[5] == '':
                slots[5] = g
            else:
                slots[6] = g
            joined = ''.join(slots)
            # if attempt(joined):
            #     sys.exit(0)
            attempt(joined)

# print('not found')
# sys.exit(1)
