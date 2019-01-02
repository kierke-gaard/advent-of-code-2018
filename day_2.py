from collections import Counter
from functools import partial, reduce
from operator import mul

def occurring_frequencies(frequencies, items):
    counts = dict(Counter(items)).values()
    return set(f for f in frequencies if f in counts)

def checksum(items_list):
    frequencies = [2, 3]
    occurrences = [f for items in items_list
                     for f in occurring_frequencies(frequencies, items)]
    counts = Counter(occurrences).values()
    return reduce(mul, counts)

items_list = [list(items) for items in str.split("abc abbccc accc aa")]
print(checksum(items_list))
# => 4