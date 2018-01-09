'''
Sungon Lee
'''
# import random
# import numpy as np
import collections
import scipy.stats as stats


'''
문제 1- a
uniform distribution을 따르는 결과 도출, 결과로써 실수가 나온다.
size: 시도 횟수
loc: 최소 값
scale: 최대 값

1에서 10 사이의 실수인 경우 6을 기준으로 6이상일 경우 HEAD가 나올 확률이 50%라고 간주하였다.
'''
head = 0
file_1_a = open("1_a.txt", "w")
for k in range(1, 101):
    uniform_result = stats.uniform.rvs(size=k, loc=1, scale=10)
    for result_toss in uniform_result:
        if result_toss >= 6:
            head += 1
    proportion_of_head = head/k
    row = '{0}\t{1}\n'.format(k, round(proportion_of_head, 3))
    file_1_a.write(row)
    head = 0
file_1_a.close()

'''
문제 1- b
uniform distribution을 따르는 결과 도출, 결과로써 실수가 나온다.
size: 각 시도마다 던지는 동전의 수(독립적임)
loc: 최소 값
scale: 최대 값

1에서 10 사이의 실수인 경우 5을 기준으로 5이상일 경우 HEAD가 나올 확률이 60%라고 간주하였다.
'''
file_1_b = open("1_b.txt", "w")
#  k: 시도 횟수
for k in range(1, 101):
    uniform_result = stats.uniform.rvs(size=k, loc=1, scale=10)
    for result_toss in uniform_result:
        if result_toss >= 5:
            head += 1
    proportion_of_head = head/k
    row = '{0}\t{1}\n'.format(k, round(proportion_of_head, 3))
    file_1_b.write(row)
    head = 0
file_1_b.close()

'''
문제 1- c
uniform distribution을 따르는 결과 도출, 결과로써 실수가 나온다.
size: 각 시도마다 던지는 동전의 수(독립적임)
loc: 최소 값
scale: 최대 값

1에서 10 사이의 실수인 경우 6을 기준으로 6이상일 경우 HEAD가 나올 확률이 50%라고 간주하였다.
1에서 10 사이의 실수인 경우 6을 기준으로 6이상일 경우 HEAD가 나올 확률이 60%라고 간주하였다.

문제 1-a, 1-b와의 차이: 시도횟수가 많다.
'''
file_1_c_50 = open("1_c_50.txt", "w")
#  k: 시도 횟수
for k in range(1, 10001):
    uniform_result = stats.uniform.rvs(size=k, loc=1, scale=10)
    for result_toss in uniform_result:
        if result_toss >= 6:
            head += 1
    proportion_of_head = head/k
    row = '{0}\t{1}\n'.format(k, round(proportion_of_head, 3))
    file_1_c_50.write(row)
    head = 0
file_1_c_50.close()

file_1_c_60 = open("1_c_60.txt", "w")
#  k: 시도 횟수
for k in range(1, 10001):
    uniform_result = stats.uniform.rvs(size=k, loc=1, scale=10)
    for result_toss in uniform_result:
        if result_toss >= 5:
            head += 1
    proportion_of_head = head/k
    row = '{0}\t{1}\n'.format(k, round(proportion_of_head, 3))
    file_1_c_60.write(row)
    head = 0
file_1_c_60.close()

'''
문제 2 - a, b
binomial distribution을 따르는 결과 도출, 결과로써 실수가 나온다.
n: 각 시도마다 던지는 동전의 수(독립적임)
p: 성공 확률(= HEAD가 나올 확률)
size: 시도 횟수

1에서 10 사이의 실수인 경우 6을 기준으로 6이상일 경우 HEAD가 나올 확률이 50%라고 간주하였다.
'''
file_2_a = open("2_a.txt", "w")
binom_result_list = stats.binom.rvs(n=10,
                                    p=0.5,
                                    size=1024)
binom_result_dict = collections.Counter(binom_result_list)
# k: 각 사건 (e.g. k==1인 경우 HEAD가 한번 나온 경우의 수)
for k in range(0, 11):
    row = '{0}\t{1}\n'.format(k, binom_result_dict[k])
    file_2_a.write(row)
file_2_a.close()

'''
문제 2 - b
p_hat을 구하는 코드

각 성공 event의 수 마다의 확률을 구한다.
'''
file_2_a = open("2_a.txt", "r")
p_hat_5 = 0
print('k\tp_hat')
while True:
    line = file_2_a.readline()
    if not line:
        break
    else:
        k, occur = (int(x) for x in line.split())
        p_hat = round(occur / 1024, 3)
        print('{0}\t{1}'.format(k, p_hat))
        if k == 5:
            p_hat_5 = p_hat

print('\nP(p_hat=0.5) is {0}'.format(p_hat_5))
file_2_a.close()


'''
문제 2 - c
binomial distribution을 따르는 결과 도출, 결과로써 실수가 나온다.
n: 각 시도마다 던지는 동전의 수(독립적임)
p: 성공 확률(= HEAD가 나올 확률)
size: 시도 횟수

'''
file_2_c = open("2_c.txt", "w")
binom_result_list = stats.binom.rvs(n=1000,
                                    p=0.01,
                                    size=1024)
binom_result_dict = collections.Counter(binom_result_list)
for k in range(0, 1025):
    row = '{0}\t{1}\n'.format(k, binom_result_dict[k])
    file_2_c.write(row)
file_2_c.close()

'''
문제 2 - d
poisson distribution을 따르는 결과 도출, 결과로써 실수가 나온다.
mu: 성공 확률(= HEAD가 나올 확률)
size: 시도 횟수

'''
file_2_d = open("2_d.txt", "w")
file_2_d_prob = open("2_d_prob.txt", "w")
poisson_result_list = stats.poisson.rvs(mu=10,
                                        size=1024)
poisson_result_dict = collections.Counter(poisson_result_list)
for k in range(0, 1025):
    row = '{0}\t{1}\n'.format(k, poisson_result_dict[k])
    file_2_d.write(row)

    row = '{0}\t{1}\n'.format(k, round(poisson_result_dict[k]/1024, 3))
    file_2_d_prob.write(row)

file_2_d.close()
file_2_d_prob.close()