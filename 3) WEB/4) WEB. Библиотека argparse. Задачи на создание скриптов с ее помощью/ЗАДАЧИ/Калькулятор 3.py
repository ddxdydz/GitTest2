import sys
import argparse


pars = []
parser = argparse.ArgumentParser()
if sys.argv[1:]:
    parser.add_argument('pars', nargs='+')
    args = parser.parse_args()  # запустить функцию парсинга
    pars = args.pars

try:
    if not pars:
        print('NO PARAMS')
    elif len(pars) != 2:
        print('TOO FEW PARAMS' if len(pars) == 1 else 'TOO MANY PARAMS')
    else:
        nums = [int(num) for num in pars if int(num) == float(num)]
        if len(nums) != len(pars):
            raise ValueError
        print(sum(nums))
except Exception as e:
    print(type(e).__name__)
