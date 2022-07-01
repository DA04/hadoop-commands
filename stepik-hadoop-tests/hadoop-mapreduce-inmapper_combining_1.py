# Напишите программу, которая реализует In-mapper combining v.1 для задачи WordCount в Hadoop Streaming.
# Sample Input:

# aut Caesar aut nihil
# aut aut
# de mortuis aut bene aut nihil
# Sample Output:

# nihil	1
# aut	2
# Caesar	1
# aut	2
# nihil	1
# aut	2
# de	1
# bene	1
# mortuis	1

import sys
for doc in sys.stdin:
    for line in doc.strip().split("\t"):
        H = {}
        for word in line.split(" "):
            H[word] = H.get(word,0) + 1
    for key, value in H.items():
        print(f'{key}\t{value}')