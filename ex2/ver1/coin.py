'''
학번: 12121527
이름: 이성온

컴퓨터 응용확률 homework 2

변수 설명
'''
import random
import numpy as np
import scipy.stats as stats

head = 0
tail = 0

# file_1_a = open("1_a.txt", "w")
# for attempt in range(0, 101):
#     for x in range(0, 101):
#         result_toss = random.randint(0, 1)
#         if result_toss == 1:
#             head += 1
#
#     row = '{0}\t{1}\n'.format(attempt, head)
#     file_1_a.write(row)
#     head = 0
# file_1_a.close()
#
# file_1_b = open("1_b.txt", "w")
# for attempt in range(0, 101):
#     for x in range(0, 101):
#         result_toss = random.randint(1, 10)
#         if result_toss >= 5:
#             # head 5, 6, 7, 8, 9, 10
#             # tali 1, 2, 3, 4
#             head += 1
#
#     row = '{0}\t{1}\n'.format(attempt, head)
#     file_1_b.write(row)
#     head = 0
# file_1_b.close()

# file_1_c_50 = open("1_c_50.txt", "w")
# for attempt in range(0, 10000):
#     for x in range(0, 101):
#         result_toss = random.randint(1, 10)
#         if result_toss > 5:
#             # head 6, 7, 8, 9, 10
#             # tali 1, 2, 3, 4, 5
#             head += 1
#
#     row = '{0}\t{1}\n'.format(attempt, head)
#     file_1_c_50.write(row)
#     head = 0
# file_1_c_50.close()

# file_1_c_60 = open("1_c_60.txt", "w")
# for attempt in range(0, 10000):
#     for x in range(0, 101):
#         result_toss = random.randint(1, 10)
#         if result_toss >= 5:
#             # head 5, 6, 7, 8, 9, 10
#             # tali 1, 2, 3, 4
#             head += 1
#
#     row = '{0}\t{1}\n'.format(attempt, head)
#     file_1_c_60.write(row)
#     head = 0
# file_1_c_60.close()

file = open("test.txt", "w")
for k in range(1, 101):
    uniform_result = stats.uniform.rvs(size=k, loc=1, scale=10)
    for result_toss in uniform_result:
        if result_toss > 5:
            head += 1
    proportion_of_head = head/k
    row = '{0}\t{1}\n'.format(k, proportion_of_head)
    file.write(row)
    head = 0
file.close()

n = 10
p = 0.5
k = np.arange(0, 21)

