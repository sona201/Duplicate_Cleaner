# 搜索并删除目标路径下所有的重复文件以及空文件夹
# 内容会直接彻底删除，请谨慎使用

# v0.9
# 20170312
# by twocui

import hashlib
from time import clock as now
import os


def getmd5(filename):

    file_txt = open(filename, 'rb').read()
    m = hashlib.md5(file_txt)
    return m.hexdigest()


all_size = {}
total_file = 0
total_delete = 0
start = now()

path = 'F:/'  # 输入搜索路径
for root, dirs, files in os.walk(path):
    for file in files:
        total_file += 1
        real_path = os.path.join(root, file)

        if os.path.isfile(real_path) is True:
            size = os.stat(real_path).st_size
            name_and_md5 = [real_path, '']

            if size in all_size.keys():
                new_md5 = getmd5(real_path)

                if all_size[size][1] == '':
                    all_size[size][1] = getmd5(all_size[size][0])

                if new_md5 in all_size[size]:
                    try:
                        os.remove(real_path)
                        print('删除', file)
                    except:
                        continue

                    total_delete += 1

                else:
                    all_size[size].append(new_md5)

            else:
                all_size[size] = name_and_md5

    if not os.listdir(root):
        os.rmdir(root)


end = now()
time_last = end - start

print('文件总数：', total_file)
print('删除个数：', total_delete)
print('耗时：', time_last, '秒')
