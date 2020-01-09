#!/usr/bin/python
# -*- coding: UTF-8 -*-
# os.walk遍历当前目录下所有文件，输出元组（文件夹路径，文件夹名称，文件名）
import os
# path = r'D:\AI\LinkDoc.Ai.ClientViewer-Release-0130'
# for fpath, dirname,fnames in os.walk(path):
#     print fpath
#     print dirname
#     print fnames


def get_files(path, rule='.py'):
    file_names = []
    for fpath, dirs, fn in os.walk(path):
        for f in fn:
            filename = os.path.join(fpath, f)
            if filename.endswith(rule):
                file_names.append(filename)

    return file_names


if __name__ == '__main__':

    b = get_files('C:\\Users\\yingbojia\\PycharmProjects\\study')
    for i in b:
        print i
