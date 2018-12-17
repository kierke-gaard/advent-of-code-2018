from collections import Counter
from functools import partial, reduce
from operator import mul

def occurring_frequencies(frequencies, items):
    counts = dict(Counter(items)).values()
    return list(set([f for f in frequencies if f in counts]))

def checksum(items_list):
    frequencies = [2, 3]
    occurrences = map(partial(occurring_frequencies, frequencies),
                      items_list)
    counts = Counter(sum(occurrences, [])).values()
    return reduce(mul, counts)

items_list = list(map(list, str.split("abc abbccc accc aa")))
checksum(items_list)
# => 4