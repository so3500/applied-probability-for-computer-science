'''
Sungon Lee

변수 설명
fluctuation_rate: 석유 생산량의 변화 비율
fluctuation_rate_sum: 석유 생산량의 변화총량
fluctuation_rate_avg: 석유 생산량의 변화총량의 평균
year_before: 이전 연도
mbbl_before: 이전 연도 석유 생산량
year_after: 이후 연도
mbbl_after: 이후 연도 석유 생산량
mbbl_differ: 이전 연도와 이후 연도 간 석유 생산량의 차이
'''

read_file = open("OilProduction.txt", "r")
write_file = open("OilProduction_trans.txt", "w")

fluctuation_rate = 0
fluctuation_rate_sum = 0
fluctuation_rate_avg = 0
year_before = 0
mbbl_before = 0
year_after = 0
mbbl_after = 0
mbbl_differ = 0

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
        year_after, mbbl_after = (int(x) for x in line.split())

        # 첫 연도 차(1880) 데이터
        if year_cnt == 0:
            mbbl_before = mbbl_after
        year_cnt += 1

        # 이후 연도(e.g. 1974)와 이전 연도(e.g. 1972)의 석유 생산량의 차이, 차이 비율, 차이의 합 등을 구함
        mbbl_differ = round(mbbl_after - mbbl_before, 3)
        fluctuation_rate = round((mbbl_after - mbbl_before) / mbbl_before, 3)
        fluctuation_rate_sum += fluctuation_rate
        fluctuation_rate_avg = round(fluctuation_rate_sum / year_cnt, 3)
        # print('mbbl_before {}, mbbl_after {}, mbbl_differ {}'.format(mbbl_before, mbbl_after, mbbl_differ))
        print('fluct_rate_avg {},'.format(fluctuation_rate_avg))

        if mbbl_differ >= 0:
            pass

        # 이후 연도(e.g. 1974)와 이전 연도(e.g. 1972)의 석유 생산량에서 이후 연도의 석유 생산량이 더 많을 경우
        # 지금까지 구해왔던 석유 생산 변화량을 이용하여 이후 연도의 석유 생산량 데이터를 변환
        else:
            print('mbbl_differ minus!')
            mbbl_after = round(mbbl_before + (mbbl_before * fluctuation_rate_avg), 3)

        row = '{}\t{}\n'.format(year_after, mbbl_after)

        # 새로 변형 된, 혹은 기존의 생산량 데이터를 파일에 씀
        write_file.write(row)

        year_before = year_after
        mbbl_before = mbbl_after

read_file.close()
write_file.close()

