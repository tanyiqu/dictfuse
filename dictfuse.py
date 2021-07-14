import sys
import os


# 判断文件是否存在
def exist(filename):
    print(sys.argv)
    pass


# 接收命令行参数
def get_args():
    argv = sys.argv
    if len(argv) != 4:
        print('usage: python dictfuse.py dict1 dict2 new_dict')
        exit(0)
        pass
    return {
        'dict1': argv[1],
        'dict2': argv[2],
        'new_dict': argv[3],
    }
    pass


# 判断元素是否在集合中
def inlist(e, l):
    for element in l:
        if element == e:
            return True
        pass
    return False
    pass


# 融合函数
def fuse(dict1, dict2, new_dict):
    # 先判断两个文件都存在
    if not os.path.exists(dict1):
        print('error: file [%s] is not exist!' % dict1)
        exit(0)
        pass
    if not os.path.exists(dict2):
        print('error: file [%s] is not exist!' % dict2)
        exit(0)
        pass

    # 读取两个文件的密码
    dict1 = open(dict1, 'r', encoding='utf-8')
    d1 = []
    for line in dict1:
        if(line[-1] == '\n'):
            line = line[0:-1]
        d1.append(line)
        pass
    dict1.close()

    dict2 = open(dict2, 'r', encoding='utf-8')
    for line in dict2:
        if(line[-1] == '\n'):
            line = line[0:-1]
        d1.append(line)
        pass
    dict2.close()
    
    total = len(d1)
    print('total : %d' % total)

    # print(d1)

    d2 = []
    # 创建新文件
    new_dict = open(new_dict, 'w', encoding='utf-8')

    # 遍历d1
    n = 0
    for pas in d1:
        if(inlist(pas, d2)):
            continue
        d2.append(pas)
        # print(pas)
        new_dict.write(pas)
        new_dict.write('\n')
        n += 1

        print(n / total)
        pass

    # print(d2)

    new_dict.close()
    pass


# 主函数
if __name__ == '__main__':
    files = get_args()
    # f1 = open()

    fuse(files['dict1'], files['dict2'], files['new_dict'])
    pass
