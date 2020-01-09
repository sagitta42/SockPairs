import random

class Socks():
    '''
    Class of a heap of socks
    '''
    def __init__(self, npairs):
        self.n_pairs = npairs
        ## create heap of socks
        # half the socks
        self.socks = range(npairs)
        # double and shuffle
        self.socks += self.socks
        random.shuffle(self.socks)

        ## initialize variables
        # socks currently picked
        self.picked_socks = []
        # number of pairs of socks
        self.n_paired = 0
        self.pairs_array = [0]


    def pick_sock(self):
        ''' Pick one sock out of the heap and try to pair it '''

        # pick first sock
        pick = self.socks[0]

        # if we have a pair
        if pick in self.picked_socks:
            # remove the pair from pool
            self.picked_socks.remove(pick)
            # inc number of pairs
            self.n_paired += 1

        # if we don't, or we have no socks picked at all
        else:
            # add sock to picked socks
            self.picked_socks.append(pick)

        # remove picked sock from pool of socks
        self.socks = self.socks[1:]
        # update array
        self.pairs_array.append(self.n_paired)


    def pair_socks(self):
        ''' Pair all the socks '''
        for i in range(self.n_pairs * 2):
            self.pick_sock()

        return self.pairs_array
