from math import pow, e
from random import uniform, seed

seed(0)

sigmoid = lambda x: 1 / (1 + pow(e, -x))


def print_net(net):
    for i in range(len(net[0])):
        print('\nWeights on Output Layer' if i == len(net[0]) - 1 else '\nWeights on Hidden Layer {}'.format(i + 1))
        for j in range(len(net[0][i])):
            print('neuron {}: {}'.format(j + 1, net[0][i][j]))
    for i in range(len(net[1])):
        print('\n', 'Biases for Output Layer' if i == len(net[1]) - 1 else 'Biases for Hidden Layer {}'.format(i + 1), sep='')
        print(net[1][i])
    print()


def print_net_scores(scores, target):
    for i in range(len(scores)):
        print('Final values of Output Layer neurons:' if i == len(scores) - 1 else 'Final values of Hidden Layer {} neurons:'.format(i + 1))
        print(scores[i], '\n')
    print('error:\n{}'.format(calc_error(target, t[-1])))


def create_weights(sizes=[1, 1, 1]):
    weights = []
    for i in range(1, len(sizes)):
        layer = []
        for n in range(sizes[i]):
            layer.append([uniform(-1, 1) for _ in range(sizes[i-1])])
        weights.append(layer)
    return weights


def create_biases(sizes=[1, 1, 1]):
    biases = []
    for i in range(1, len(sizes)):
        biases.append([uniform(-1, 1) for _ in range(sizes[i])])
    return biases


def calc_error(target, original):
    return sum(pow(original[i] - target[i], 2) for i in range(len(target)))


def apply_net(net, inp):
    layers = len(net[0])
    all_vals = [inp[:]]
    for i in range(layers):
        vals = []
        for j in range(len(net[0][i])):
            N = sum(net[0][i][j][x] * all_vals[i][x] for x in range(len(all_vals[i]))) + net[1][i][j]
            vals.append(sigmoid(N))
        all_vals.append(vals[:])
    return all_vals[1:]


size = [3, 5, 5, 4]

weights = create_weights(size)
biases = create_biases(size)
net = [weights, biases]

print_net(net)

inp = [1, 1, 0]
target = [0, 0, 1, 0]

t = apply_net(net, inp)

print_net_scores(t, target)


input()