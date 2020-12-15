import operator
import collections
from os import listdir
from os.path import isfile, join

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = {'arm': 4, 'head': 1, 'body': 2, 'leg': 3}
d = {'arm2': 5, 'head2': 9, 'body2': 8, 'leg2': 6}
dict_val = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
spisok_4isel = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
]
numba = [15, 20, 25, 30, 35, 40, 45, 55, 60, 37, 100, 105, 220]


def less_printer(wenig_aus):  # 1
    for cv in wenig_aus:
        if cv < 5:
            return cv

    # return list


def similar(a, b):  # 2
    return set(a) - set(b)


def sort_dict(c):  # 3
    return dict(sorted(c.items(), key=operator.itemgetter(1)))


def merger(c, d):  # 4
    return {**c, **d}


def highest(dict_val):  # 5
    return sorted(dict_val, key=dict_val.get, reverse=True)[:3]


def str_maker(e: int):  # 6
    return str(e)


def pascal_triangle(n):  # 7
    row = [1]
    y = [0]
    for x in range(max(n, 0)):
        print(row)
        row = [left + right for left, right in zip(row + y, y + row)]


def palindrome(string: str):  # 8
    return string == ''.join(reversed(string))


def transform(seconds):  # 9

    # datetime.strptime


    days = seconds // (24 * 3600)
    seconds %= 24 * 3600
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    print(f'{days}:{hours}:{minutes}:{seconds}')


def list_tuple_maker(numbers):  # 10
    coma_rem = numbers.split(',')
    num_gen = map(int, coma_rem)
    spisok = list(num_gen)
    cortej = tuple(spisok)
    return spisok, cortej


def edge_cutter(b: list):  # 11
    print(b[0], b[-1])


def get_extension(filename):  # 12 скомуниздил
    filename_parts = filename.split('.')
    if len(filename_parts) < 2:  # filename has no dots
        raise ValueError('the file has no extension')
    first, *middle, last = filename_parts
    if not last or not first and not middle:
        # example filenames: .filename, filename., file.name.
        raise ValueError('the file has no extension')
    return filename_parts[-1]


def n_sum(n):  # 13
    n1 = n
    n2 = int(str(n) + str(n))
    n3 = int(str(n) + str(n) + str(n))
    print(n1 + n2 + n3)

    return n ** 2


def even_num_iter(spisok_4isel: list):  # 14
    for x in spisok_4isel:
        if x == 237:
            break
        elif x % 2 == 0:
            print(x)


def not_similar(a, b):  # 15
    return set(a) - set(b)


def file_spisok():  # 16
    return [f for f in listdir('/documents') if isfile(join('/documents', f))]


def summa(q):  # 17
    digits = [int(d1) for d1 in str(q)]
    print(sum(digits))


def sentence(q: str):  # 18
    symbol = 'abcdefghijklmnopqrstuvwxyz'
    for key in symbol:
        print(key, q.count(key))


def switch_num(x, y):  # 19
    y, x = x, y
    return x, y


def div15(numba):  # 20
    result6 = list(filter(lambda li: not li % 15, numba))
    print(result6)


def unique(numbrs):  # 21
    return numbrs == set(numbrs)


def word_counter(text: str):  # 22
    # dodelat'
    # slovnyk = collections.defaultdict(int)
    # for word in text.split():
    #     slovnyk[word] += 1
    #
    # print(slovnyk)
    slovnyk = text.split()
    counter = collections.Counter(slovnyk)
    most_common, occurrences = counter.most_common()[0]

    longest = max(slovnyk, key=len)

    return most_common, longest
