'''
Sungon Lee

변수 설명
year: 연도
mbbl_before: data transformation 이전 연도 석유 생산량
mbbl_after: data transformation 이후 연도 석유 생산량
'''

import math

read_file = open("OilProduction.txt", "r")
write_file = open("OilProduction_trans_log.txt", "w")

year = 0
mbbl_before = 0
mbbl_after = 0

year_cnt = 0

while True:
    line = read_file.readline()

    # OilProduction.txt 에서 더 이상 읽을 line 이 없을 경우 프로그램 종료
    if not line:
        break

    # '#' 으로 시작하는 주석은 그대로 복사
    if line.split(' ')[0] == '#':
        write_file.write(line)

    else:
        # file 로부터 year, mbbl 값을 추출
        year, mbbl_before = (int(x) for x in line.split())
        # 이전 년도 석유 생산량에 대해 자연로그를 취함, 소수 3째 자리에서 반올림
        mbbl_after = round(math.log(mbbl_before), 3)

        # 새로 변형 된, 혹은 기존의 생산량 데이터를 파일에 씀
        row = '{}\t{}\n'.format(year, mbbl_after)
        write_file.write(row)

read_file.close()
write_file.close()

