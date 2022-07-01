# Реализуйте Combiner в задаче подсчета среднего времени, проведенного пользователем на странице.

# Mapper пишет данные в виде key / value, где key - адрес страницы, value - пара чисел, разделенных ";". Первое - число секунд, проведенных пользователем на данной странице, второе равно 1.

# Sample Input:

# www.facebook.com	100;1
# www.google.com	10;1
# www.google.com	5;1
# www.google.com	15;1
# stepic.org	60;1
# stepic.org	100;1
# Sample Output:

# www.facebook.com	100;1
# www.google.com	30;3
# stepic.org	160;2


from collections import defaultdict
import sys
h = defaultdict(list)
for line in sys.stdin:
    key, value = line.strip().split()
    sum, count = value.split(';')
    h[key] += [[sum, count]]
for item in h.items():
    s = c = 0
    for a in item[1]:
        s += int(a[0])
        c += int(a[1])
    print(f'{item[0]}\t{s};{c}')