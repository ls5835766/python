# 将用户的输入保存为新的文件

def file_write(file_name):
    # x和w`均为“可写入的状态”，其中x:路径存在，会抛出异常，而w:直接覆盖原文件
    f = open(file_name, 'w')
    print('请输入内容【单独输入\':w\'保存退出】:')

    while True:
        write_some = input()
        if write_some != ':w':
            f.write("%s \n" % write_some)
        else:
            break
    f.close()


file_name = input("请输入文件名：")
file_write(file_name)
