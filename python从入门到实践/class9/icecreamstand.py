from class9.restaurant1 import Restaurant


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['香蕉', '苹果', '咸鱼']

    def icecream_menu(self):
        print('冰淇淋的种类：' + str(self.flavors))


if __name__ == '__main__':
    IceCreamStand = IceCreamStand('悦来客栈', '复古')
    IceCreamStand.icecream_menu()
