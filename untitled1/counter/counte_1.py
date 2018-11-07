class CountList:
    def single_list(self, arr):
        result = {}
        for i in set(arr):
            result[i] = arr.count(i)
        return result

    def dict_list(self, dic):
        new_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        new_dict = dict(new_dic)
        return new_dict


L = [1, 1, 2, 2, 3, 3, 3, "a", "a"]
C = CountList()
r = C.single_list(L)
print(r)
s = C.dict_list(r)
print(s)
