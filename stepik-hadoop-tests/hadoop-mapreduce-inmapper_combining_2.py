# Напишите программу, которая реализует In-mapper combining v.2 для задачи WordCount в Hadoop Streaming.
# Sample Input:

# aut Caesar aut nihil
# aut aut
# de mortuis aut bene aut nihil
# Sample Output:

# aut	6
# mortuis	1
# bene	1
# Caesar	1
# de	1
# nihil	2

import sys
H = {}
for doc in sys.stdin:
    for line in doc.strip().split("\t"):
        for word in line.split(" "):
            H[word] = H.get(word,0) + 1
for key, value in H.items():
    print(f'{key}\t{value}')