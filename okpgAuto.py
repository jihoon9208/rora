import os

path = "./test"
file_list = os.listdir(path)
len = len(file_list)
print(len)

for i in range(0, len-1):
    file = path + '/' + file_list[i]
    os.system('opkg install %s' % file)

