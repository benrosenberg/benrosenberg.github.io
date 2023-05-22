from matplotlib import pyplot as plt
import math_pi, sympy
import math
import numpy as np
from matplotlib.collections import LineCollection

N = 10000

def first_n_fib(n):
    a, b = 0, 1
    out = []
    for _ in range(n):
        out.append(a)
        a,b = b,a+b
    return out

def first_n_lucas(n):
    a, b = 2, 1
    out = []
    for _ in range(n):
        out.append(a)
        a,b = b,a+b
    return out

def first_n_pi_digits(n):
    return [int(d) for d in math_pi.pi(b=n).replace('.', '')]

def first_n_primes(n):
    out = [2]
    while len(out) < n:
        out.append(sympy.nextprime(out[-1]))
    return out

def first_n_naturals(n):
    return range(n)

def first_n_squares(n):
    return [i**2 for i in range(n)]
        
def first_n_cubes(n):
    return [i**3 for i in range(n)]

def first_n_fourth_powers(n):
    return [i**4 for i in range(n)]

def first_n_fifth_powers(n):
    return [i**5 for i in range(n)]

def first_n_palindromes(n):
    out = []
    i = 1
    while len(out) < n:
        if str(i) == str(i)[::-1]:
            out.append(i)
        i += 1
    return out

def first_n_palindromes_base_2(n):
    out = []
    i = 1
    while len(out) < n:
        bin_i = bin(i)[2:]
        if bin_i == bin_i[::-1]:
            out.append(i)
        i += 1
    return out

def apply(direction, point):
    dx, dy = direction
    x, y = point
    return (x + dx, y + dy)

def get_dir_knight_lr(last_dir):
    if last_dir is None:
        return None
    mapping = {
        (-1, 2) : [(-2, 1), (1, 2)],
        (1, 2)  : [(-1, 2), (2, 1)],
        (2, 1)  : [(1, 2), (2, -1)],
        (2, -1) : [(2, 1), (1, -2)],
        (1, -2) : [(2, -1), (-1, -2)],
        (-1, -2): [(1, -2), (-2, -1)],
        (-2,-1) : [(-1, -2), (-2, 1)],
        (-2,1)  : [(-2, -1), (-1, 2)]
    }
    return mapping[last_dir]
    
def plot_knight_progression(THIS_MOD_N, seq):
    def next_dir(n, seq, last_dir=None):
        this_num = seq[n]
        dir_knight_lr = get_dir_knight_lr(last_dir)
        out = this_num % THIS_MOD_N
        out = out % 2
        return dir_knight_lr[out]

    def next_point(current_point, i, seq, last_dir=None):
        if last_dir is None:
            return apply(next_dir(i, seq), current_point)
        else:
            dir_next = next_dir(i, seq, last_dir=last_dir)
            return dir_next, apply(dir_next, current_point)

    start = (0,0)
    progression = [start]
    last_dir = (1,2)
    for i in range(N):
        last_dir, next = next_point(progression[-1], i, seq, last_dir=last_dir)
        progression.append(next)

    x = [x for x,_ in progression]
    y = [y for _,y in progression]

    return x, y

if __name__ == '__main__':
    i,j=0,0
    list_of_mod_n_to_plot = range(3, 4, 1)
    PLOTS_PER_ROW = 1
    # list_of_mod_n_to_plot = range(1, 50, 2)
    # PLOTS_PER_ROW = 5
    # list_of_mod_n_to_plot = range(1, 12, 2)
    # PLOTS_PER_ROW = 3
    # list_of_mod_n_to_plot = range(151, 200, 2)
    # PLOTS_PER_ROW = 5
    fig, axs = plt.subplots(math.ceil(len(list_of_mod_n_to_plot)/PLOTS_PER_ROW),PLOTS_PER_ROW, figsize=(60, 60))
    axs = [[axs]]
    fig.tight_layout(pad=10.0)
    cmap = 'cool'
    seq = first_n_palindromes_base_2(N)
    for mod_n_to_plot in list_of_mod_n_to_plot:
        x, y = plot_knight_progression(mod_n_to_plot, seq)
        color_arg = range(N)
        points = np.array([x, y]).T.reshape(-1, 1, 2)
        segments = np.concatenate([points[:-1], points[1:]], axis=1)
        lc = LineCollection(segments, cmap=cmap)
        lc.set_array(color_arg)
        lc.set_linewidth(0.5)
        line = axs[i][j].add_collection(lc)
        axs[i][j].set_title('mod {}'.format(mod_n_to_plot))
        axs[i][j].set_xticks([])
        axs[i][j].set_yticks([])
        axs[i][j].set_xlim(min(x), max(x))
        axs[i][j].set_ylim(min(y), max(y))
        j+=1
        if j%PLOTS_PER_ROW==0:
            i+=1
            j=0

    plt.show()