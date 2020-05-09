import os

path = "./"
file_list = os.listdir(path)
len = len(file_list)
print(len)

for i in range(0, len-1):
    file = path + '/' + file_list[i] 
    os.system('scp %s root@192.168.31.115:/root/home/test' % file)

