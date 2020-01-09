from sock import *
from myplot import *
import sys

prop_cycle = plt.rcParams['axes.prop_cycle']
COLORS = prop_cycle.by_key()['color']

def sock_pairing(num_pairs, num_trials):
    '''
    Study the evolution of the number of paired socks when picking socks
    one by one out of a heap of laudry.

    num_pairs [int]: number of pairs of socks in the heap
    num_trials [int]: how many times we simulate the picking

    If only one trial is given, sock picking will be done num_pairs times
        for the range of number of pairs between 1 and num_pairs.
    If multiple trials are given, sock picking will be done for num_pairs pairs
        of socks only.

    '''

    p = Plot((10,8))

    # one trial = plot one case 2, 3, 6, ..., num_pairs pairs
    # multiple trials = plot many cases for num_pairs pairs
    n_pairs = [num_pairs] if num_trials > 1 else range(1, num_pairs+1)

    # for each number of pairs
    for npar in n_pairs:
        # pick a colour
        color = COLORS[(npar-1) % len(COLORS)] if num_trials == 1 else 'k'
        # pick line style
        ls = '-' * (3 - (npar-1) / len(COLORS) - 1)
        if ls == '': ls = '-.'
        # many trials
        for i in range(num_trials):
            socks = Socks(npar)
            npairs = socks.pair_socks()
            plt.plot(range(len(npairs)), npairs, color=color, linestyle=ls,\
                linewidth=2, label=npar if num_trials == 1 else None)

    ## beautification
    if num_trials == 1:
        p.legend(ncol=3, title='Number of pairs')
    else:
        plt.title('{0} trials for {1} pairs of socks'.format(num_trials, num_pairs))

    plt.xlabel('Number of socks picked')
    plt.ylabel('Number of paired sock pairs')
    p.pretty()

    ## save
    imgname = 'npairs{0}_ntrials{1}.png'.format(num_pairs, num_trials)
    p.figure(imgname)


def user_dict():
    '''
    Helper function to read out user input of format variable=value
    e.g. input
        $ python sock_pairing.py npairs=20 ntrials=300
    yields
        {'ntrials': 300, 'npairs': 20}
    '''
    dct = {}
    for key, val in [x.split('=') for x in sys.argv[1:]]:
        dct[key] = int(val)
    return dct


if __name__ == '__main__':
    # get user input
    dct = user_dict()
    # pair all the socks
    sock_pairing(dct['npairs'], dct['ntrials'])

# sock_pairing(20, 300)
# sock_pairing(20, 1)
