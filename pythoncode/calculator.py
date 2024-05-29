


class Calculater():
    def add(self, a, b):
        return a+b

    def div(self, a, b):

        if(b== 0):
            return 0
        return a/b


    def add_for(self):
        user_input= int(input())
        sum = 0
        for i in range(user_input+1):
            if i % 2 == 0:
                continue
            sum = sum + i
        return sum

    def demo(self):
        for i in range(5):
            res = yield i
            print("send传进来的参数{}".format(res))


class Add(Calculater):
    def add(self, a, b):
        return ("这个是测试demo",a+b)

import threading

class MyRunnable:
    def run(self):
        print("MyThread is running!")


class YourRunnable:
    def run(self):
        print("YourThread is running!")





if __name__ == '__main__':

    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    # nums2 = [2, 5, 6, 5, 9, 10]
    # n = 5
    count = 0
    for i in range(len(nums)):
        if nums[i] == val:
            temp = nums[count]
            nums[count] = nums[i]
            nums[i] = temp
            count += 1
    print(nums)

    print(nums)












