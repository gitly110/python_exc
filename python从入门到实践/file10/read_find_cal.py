file = 'test.txt'
with open(file) as f:
    lines = f.readlines()
status_list = []
ip_list = []
for line in lines:
    # 把每行分成一个list，便于取值
    line_list = line.split()
    # 获取状态为200的
    if line_list[3] == '200':
        status_list.append(line_list)
    # 获取ip
    ip_list.append(line_list[0])

# 求响应时间平均值
total_time = 0
for res_time in status_list:
    total_time += int(res_time[2])
avg_time = total_time / len(status_list)
print('avg_time=%d' % avg_time)

# 剔除重复的ip，再求出个数
count_ip = len(set(ip_list))
print('count_ip=%d' % count_ip)
