# Реализуйте reducer в задаче подсчета среднего времени, проведенного пользователем на странице.

# Mapper передает в reducer данные в виде key / value, где key - адрес страницы, value - число секунд, проведенных пользователем на данной странице.

# Среднее время на выходе приведите к целому числу.

# Sample Input:

# www.facebook.com	100
# www.google.com	10
# www.google.com	5
# www.google.com	15
# www.stepic.org	60
# www.stepic.org	100
# Sample Output:

# www.facebook.com	100
# www.google.com	10
# www.stepic.org	80

from collections import defaultdict
import sys
h = defaultdict(list)
for line in sys.stdin:
    key, value = line.strip().split()
    h[key] += [int(value)]
for item in h.items():
    print(f'{item[0]}\t{round(sum(item[1])/len(item[1]))}')