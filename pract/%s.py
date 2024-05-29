





if __name__ =='__main__':
    # dic = {"a": 1, "b": 2, "c": 3}
    # print(dic.keys())
    # print(dic.values())
    # for i, k in dic.items():
    #     print(i, k)
    # with open("测试.txt", mode="r+") as file, open("测试.bat", mode="w+") as file2:
    #     for line in file:
    #         if "加油" in line:
    #             line = line.replace("加油", "继续努力吧")
    #         file2.write(line)
    # import os
    # os.remove("测试.txt")
    # os.rename("测试.bat", "测试.txt")
    username = "admin"
    print("我的名字是%s"%username)
    print("我的名字是{}".format(username))
    print(f"我的名字是{username}")

    dict1 ={"name":"amy","age":19,"pass":"jjjj"}
    # for k ,v in dict1.items():
    #     print(k,v)
    # for k in dict1.keys():
    #     print(k)

    for index, (key, value) in enumerate(dict1.items()):
        print(index, key, value)























































































