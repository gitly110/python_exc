from random import choice


class RandomWalk():
    def __init__(self, num_points=5000):
        self.num_points = num_points
        # 存储x 和y 值的列表，并且所有随机漫步都始于(0, 0)
        self.x_values = [0]
        self.y_values = [0]

        # 决定前进方向以及沿这个方向前进的距
    def get_step(self):
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
        step = direction * distance
        return step

    def fill_walk(self):
        while len(self.x_values) < self.num_points:

            # 决定前进方向以及沿这个方向前进的距
            x_step = self.get_step()
            y_step = self.get_step()

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 下一个点的x和y值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
