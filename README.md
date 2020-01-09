# SockPairs

Evolution of the number of paired socks one has when picking them randomly one by one from a heap of laudry.

Multiple trials on the same number of socks in the pile

![trials](https://github.com/sagitta42/SockPairs/blob/master/img/npairs20_ntrials300.png?raw=true)

Comparison of the evolution for the different initial number of sock pairs

![nums](https://github.com/sagitta42/SockPairs/blob/master/img/npairs20_ntrials1.png?raw=true)


## Usage

### Multiple trials

```console
python sock_pairing.py npairs=20 ntrials=300
```

Pair 20 pairs of socks 300 times and show the resulting evolution steps.

### One trial

```console
python sock_pairing.py npairs=20 ntrials=1
```

Pair 1, 2, ..., 20 pairs of socks one time and show the comparison.

Optional argument ```save``` will save the .png plot (see [myplot](https://github.com/sagitta42/myplot) documentation)
