import argparse

parser = argparse.ArgumentParser()

parser.add_argument('integers', type=int)

args = parser.parse_args()  # запустить функцию парсинга

'''
for t in our_time_axioms.keys():
    time_type, value = t, getattr(args, t)
    
if sys.argv[1:]:
    parser.add_argument('pars', nargs='+')
    args = parser.parse_args()  # запустить функцию парсинга
    pars = args.pars
'''
