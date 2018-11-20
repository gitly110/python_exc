import json
from data_download16.country_codes import get_country_codes

file = 'population_data.json'
# 加载数据到列表
with open(file) as f:
    pop_data = json.load(f)

# 打印每个国家2010年的人口数
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        '''
        Python不能直接将包含小数点的字符串'1127437398.85751'
        转换为整数（这个小数值可能是人口数据缺失时通过插值得到的）。
        为消除这种错误，我们先将字符串转换为浮点数，再将浮点数转换为整数
        '''
        population = int(float(pop_dict['Value']))
        # print('%-50s:%-50s' % (country_name, str(population)))
        code = get_country_codes(country_name)
        if code:
            print(code + ':' + str(population))
        else:
            print('error - ' + country_name)
       