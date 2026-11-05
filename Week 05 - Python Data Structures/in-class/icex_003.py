# in-class/icex_003.py

def compute_results():
    s = 0 # Summator
    c = 0 # Counts numbers entered
    n = int(input('Please, enter an integer or <=0 to terminate: '))
    while n > 0:
        s += n # Update summator
        c += 1 # Update counter
        n = int(input('Please, enter an integer or <=0 to terminate: '))
    avg = 0
    if c > 0:
        avg = s / c # avg = sum / count
    return s, avg # A python function can return as many values as we want (a tuple)


def print_results(n_sum, n_avg):
    print(
        f'Total sum: {n_sum}\n'
        f'Average  : {n_avg}'
    )


def main():
    s, c = compute_results()
    print_results(s, c)


if __name__ == '__main__':
    main()