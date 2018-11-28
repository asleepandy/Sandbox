
import itertools
import pprint

params = {'a': [1, 3, 4], 'b': [22, 33], 'c': ['v1', 'v2']}

cases = []


def merge_vals(obj=[]):
    return ['/'.join(map(str, vals)) for vals in obj]


for k, val in sorted(params.items()):
    cases = val if cases == [] else merge_vals(itertools.product(cases, val))

res = [dict(zip(sorted(params.keys()), val.split('/'))) for val in cases]
# print(res)
pprint.pprint(res)
