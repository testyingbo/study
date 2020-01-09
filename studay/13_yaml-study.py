#!/usr/bin/python
# -*- coding: UTF-8 -*-
import yaml
import os

# 获取当前脚本所在文件夹路径
curpath = os.path.dirname(os.path.realpath(__file__))
# 获取yaml文件路径
yamlpath = os.path.join(curpath, 'study_yaml.yaml')
# open 方法打开直接读取内容
f = open('study_yaml.yaml', 'r')
text = f.read()

print text

d = yaml.safe_load(text)   # 用load方法转为字典类型
print d


