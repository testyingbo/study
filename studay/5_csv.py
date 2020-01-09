#!/usr/bin/python
# -*- coding: UTF-8 -*-
import csv
import codecs
import sys
reload(sys)   # reload是重载函数
sys.getdefaultencoding('utf-8')  # 设置默认编码为utf-8

f = codecs.open('xieru.csv', 'wb', 'gbk')
writer = csv.writer(f)
data = ["客户名称", "行业类型", "客户联系人", "职位", "联系方式", "邮箱", "地址"]
datas = [
    ["客户名称", "行业类型", "客户联系人", "职位", "联系方式", "邮箱", "地址"],
    ["客户名称", "行业类型", "客户联系人", "职位", "联系方式", "邮箱", "地址"],
    ["客户名称", "行业类型", "客户联系人", "职位", "联系方式", "邮箱", "地址"]
        ]
writer.writerow(data)
# writer.writerows(datas)

f.close()
