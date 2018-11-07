import xlrd


class XlsRead:

    def __init__(self, xlspath, sheetname):
        self.data = xlrd.open_workbook(xlspath)
        self.table = self.data.sheet_by_name(sheetname)
        # 第一行作为key值
        self.keys = self.table.row_values(0)
        self.rownum = self.table.nrows
        self.colnum = self.table.ncols

    def dict_data(self):
        if self.rownum > 1:
            r = []
            for i in range(1, self.rownum):
                s = {}
                values = self.table.row_values(i)
                for x in range(self.colnum):
                    s[self.keys[x]] = values[x]
                r.append(s)
        return r


if __name__ == '__main__':
    filepath = 'userdata.xlsx'
    sheetname = 'Sheet1'
    data = XlsRead(filepath, sheetname)
    print(data.dict_data())
