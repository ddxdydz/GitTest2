import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--barbie', nargs='?', type=int, default=50, )
parser.add_argument('--cars', nargs='?', type=int, default=50)
parser.add_argument('--movie', nargs='?', type=str, default='other',
                    choices=['melodrama', 'football', 'other'])

args = parser.parse_args()  # запустить функцию парсинга

wt_movie_dict = {'melodrama': 0, 'football': 100, 'other': 50}
cars = args.cars if args.cars in range(0, 101) else 50
barbie = args.barbie if args.barbie in range(0, 101) else 50
movie = wt_movie_dict[args.movie]

boy = int((100 - barbie + cars + movie) / 3)
girl = 100 - boy  # вероятность мужского и женского пола

print(f'boy: {boy}', f'girl: {girl}', sep='\n')
