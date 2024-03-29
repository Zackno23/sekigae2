import os
import random

member_list = ["吉田", "高橋", "舞鶴", "中野",
               "田中", "柴田", "兼松", "徳田",
               "下川", "熊谷", "山田", "塚田",
               "望月", "速水"]
previous_list = member_list.copy()


# リストを改行入りの文字列にする
def list_to_string(list):
    string = ''
    for i in list:
        string += f'{i}\n'
    return string


# 右隣・左隣の組み合わせが前回とかぶらないようにチェック
def neighbor_check(list):
    neighbor_dict = {}
    for i in list:
        name = list.index(i)
        if name != len(list) - 1:
            neighbor_dict[i] = [list[name - 1], list[name + 1]]
        else:
            neighbor_dict[i] = [list[-2], list[0]]
    return neighbor_dict


path = "./test.txt"

# test.txtが存在する場合
if os.path.exists(path):
    shuffle_completed = False
    while not shuffle_completed:
        f = open('test.txt', 'rt')
        previous_member_list = [i[:-1] for i in f.readlines()]
        f.close()
        random.shuffle(member_list)

        for i in range(len(member_list)):
            if member_list[i] == previous_member_list[i]:
                break
        else:
            # members_lisを参照
            member_dict = neighbor_check(member_list)
            previous_dict = neighbor_check(previous_list)

            for i in member_list:
                check_neighbor = set(member_dict[i] + previous_dict[i])

                if len(check_neighbor) != 4:
                    break

            else:
                shuffle_completed = True

        shuffled_String = list_to_string(member_list)
    else:
        f = open('test.txt', 'w')
        f.write(shuffled_String)



else:
    f = open('test.txt', 'w')
    member_string = '吉田\n高橋\n舞鶴\n中野\n田中\n柴田\n兼松\n徳田\n下川\n熊谷\n山田\n塚田\n望月\n速水'
    f.write(member_string)

print("TableA:", end="")
# print(member_list[:4])
print("TableB:", end="")
# print(member_list[4:8])
print("TableC:", end="")
# print(member_list[8:])
f.close()
