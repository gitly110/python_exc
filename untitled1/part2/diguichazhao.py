#二分查找，递归法
def mid_search(source,n):
    source.sort()
    mid=len(source)//2
    if len(source)>=1:
        print(source)
        if n>source[mid]:
            mid_search(source[mid+1:],n)
            print(source.index(n))
        elif n<source[mid]:
            mid_search(source[:mid],n)
            print(source.index(n))
        # else:
        #     print(source[mid])
    else:
        print('no found!')

test_source=[2,3,1,5,23,66,32]
mid_search(test_source,32)


