"""
文件处理排序
"""

import datetime
import os


def order_by_time(file_path):
    """
    根据数据的时间，对数据进行排序
    :param file_path: 文件路径
    :return: 排序后结果
    """
    f = open(file_path, encoding='utf-8')
    data = f.readlines()
    lis = []
    for i in range(len(data)):
        s = data[i].split(' ')
        s1 = [j.replace('\n', '') for j in s]
        s1[3] = str(datetime.datetime.strptime(s1[3], '%Y-%m-%d'))
        lis.append(s1)
    count = sorted(lis, key=lambda x: x[3])
    f.close()
    return count


def get_file_list(file_path):
    """
    对执行文件夹的文件根据文件修改时间对文件名进行排序
    :param file_path:
    :return:
    """
    dir_list = os.listdir(file_path)
    if not dir_list:
        return
    else:
        # 注意，这里使用lambda表达式，将文件按照最后修改时间顺序升序排列
        # os.path.getmtime() 函数是获取文件最后修改时间
        # os.path.getctime() 函数是获取文件最后创建时间
        dir_list = sorted(dir_list, key=lambda x: os.path.getmtime(os.path.join(file_path, x)))
        # print(dir_list)
        return dir_list


"""
1 test 100 2012-04-18
2 aaa 12 2012-04-19
3 bbb 333 2012-04-18
4 ccc 211 2012-04-17
5 ddd 334 2012-04-16
"""
