import zipfile
from random import choice


def get_zip_text(domain):
    s = ""
    with zipfile.ZipFile(domain) as z:
        for filename in z.namelist():
            for f in z.open(filename):
                str += f.decode("utf-8").strip() + ' '
    return str


def eval_text(str=''):
    data = str.split(' ')
    data = [d for d in data if d is not '']
    d = {}
    for i in range(0, len(data) - 2):
        K = data[i] + ' ' + data[i + 1]
        N = data[i + 2]
        if K not in d.keys():
            d[K] = [(N, 1)]
        else:
            c = False
            for item in d[K]:
                if item[0] is N:
                    d[K].append((N, item[1] + 1))
                    d[K].remove(item)
                    c = True
                    break
            if c is False:
                d[K].append((N, 1))
    return d


def generate_new_text(length=100):
    words = choice(list(d.keys())).split()
    for _ in range(length - 2):
        pop = []
        for item in d[words[-2] + ' ' + words[-1]]:
            for _ in range(item[1]):
                pop.append(item[0])
        words.append(choice(pop))
    string = ' '.join(words)
    return string[0].upper() + string[1:]


d = eval_text(get_zip_text('commencement_speeches.zip'))
string = generate_new_text(1000)

for c in string:
    print((c, c + '\n')[c is '.'], end='')
