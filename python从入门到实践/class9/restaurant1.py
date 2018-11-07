class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print('餐馆名字：', self.restaurant_name)
        print('风味：', self.cuisine_type)

    def open_restaurant(self):
        print('餐厅正在营业')

    def set_number_served(self, snum):
        if snum >= 0:
            self.number_served = snum
        else:
            print('客人不能是负数')
        print('客户数量：', self.number_served)

    def increment_number_served(self, innum):
        self.number_served += innum


if __name__ == "__main__":

    restaurant = Restaurant('python大酒店', '国际风味')
    print(restaurant.restaurant_name)
    print(restaurant.cuisine_type)
    restaurant.describe_restaurant()
    restaurant.open_restaurant()

    print(restaurant.number_served)
    restaurant.set_number_served(11)
    restaurant.increment_number_served(5)
    print(restaurant.number_served)