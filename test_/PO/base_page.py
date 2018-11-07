class Action(object):
    #初始化
    def __init__(self, se_driver):
        self.driver = se_driver

    #重写元素定位的方法

    #重写id定位
    def find_by_id(self, loc):
        try:
            return self.driver.find_element_by_id(loc)
        except Exception as e:
            print("未找到%s"%(self, loc))

    #重写