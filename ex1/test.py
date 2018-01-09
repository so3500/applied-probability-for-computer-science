val_list = [20389, 28065.66303250578, 37906.11597897322,
            49969.15092786309, 64012.3377122856, 79602.40520387432]
rate_list = [0.3765100315123734, 0.35062250035105824, 0.31823452858059426,
             0.28103713038261663, 0.2435478541911865]
idx = 0
for rate in rate_list:
    val = val_list[idx]
    act = val + val * rate
    print('mbbl_before {}, rate_avg {}, mbbl_after {}'.
          format(val, rate, act))
    idx += 1