def read_files(files):
    for file in files:
        try:
            with open(file, encoding='UTF-8') as f:  # 不定义读取编码会读不出中文
                read = f.read()
        except:
            print('The file named:%s is not found' % file)
        else:
            print('{0} content:\n{1}'.format(file, read))


def count_string(string, files):
    for file in files:
        with open(file, encoding='UTF-8') as f:
            read = f.read()
            count = read.count(string)
            print('{0}在{1}中出现了{2}次'.format(string, file, count))


files = ['pi_digits.txt', 'reason.txt', 'guest.txt']
read_files(files)
count_string('ff', files)

