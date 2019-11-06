import os
import random

member_list = ["吉田", "高橋", "舞鶴", "中野",
               "田中", "柴田", "兼松", "徳田",
               "下川", "熊谷", "山田", "塚田",
               "望月", "速水"]


# リストを改行入りの文字列にする
def list_to_string(list):
    string = ''
    for i in list:
        string += f'{i}\n'
    return string


path = "./test.txt"

if os.path.exists(path):
    shuffle_completed = False
    while shuffle_completed == False:
        f = open('test.txt', 'rt')
        previous_string = [i[:-1] for i in f.readlines()]
        f.close()
        print(previous_string)
        random.shuffle(member_list)
        print(member_list)

        for i in range(len(member_list)):
            if member_list[i] == previous_string[i]:
                print("かぶってるよ！")
                break
        else:
            shuffle_completed = True

        shuffled_String = list_to_string(member_list)

        f = open('test.txt', 'w')
        f.write(shuffled_String)



else:
    f = open('test.txt', 'w')
    member_string = '吉田\n高橋\n舞鶴\n中野\n田中\n柴田\n兼松\n徳田\n下川\n熊谷\n山田\n塚田\n望月\n速水'
    f.write(member_string)

f.close()

# f = open('test.txt', 'rt')
# print(f.read())
