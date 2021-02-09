import argparse

t_axs = {'year': 360, 'month': 30, 'week': 7, 'day': 1}  # in a days

parser = argparse.ArgumentParser()

# именованные аргументы с известными доходами/расходами (вещественные числа)
parser.add_argument('--per-day', type=float, default=0, dest="day", metavar='PER_DAY')
parser.add_argument('--per-week', type=float, default=0, dest='week', metavar='PER_WEEK')
parser.add_argument('--per-month', type=float, default=0, dest='month', metavar='PER_MONTH')
parser.add_argument('--per-year', type=float, default=0, dest='year', metavar='PER_YEAR')
# период времени за который требуется рассчитать итоговый результат.
parser.add_argument('--get-by', type=str, default='day',
                    choices=['day', 'month', 'year'], dest='range')

args = parser.parse_args()  # запустить функцию парсинга

print(int(sum(getattr(args, t) * t_axs[args.range] / t_axs[t] for t in t_axs.keys())))
