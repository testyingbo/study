#!/usr/bin/python
# -*- coding: UTF-8 -*-
import yaml
import os
import unittest
from ruamel import yaml
curpath = os.path.dirname(os.path.realpath(__file__))
# 1.首先把公共数据单独抽出来，用一个文件去管理，如yaml文件
# 2.写一个读yaml文件的get_token()函数放到a.py，去读取需要的数据
# 3.其它脚本全部调用a.py里面的get_token()函数，然后传参
# 4.token动态获取可以写个登录函数放到run.py，获取到之后把token值写入到yaml文件，这样保证每次token都是最新的
# 5.run.py里面在运行所有用例之前先登录一次并写入token到yaml,然后执行所有用例，出报告结果


# 从yaml中读取token
def get_token(yamlname='token.yaml'):
    '''
    从token.yaml读取token值
    :param yamlName: 配置文件名称
    :return: token值
    '''
    yamlpath = os.path.join(curpath, yamlname)
    f = open(yamlpath)
    r = f.read()
    t = yaml.safe_load(r)
    f.close()
    return t['token']


# 单个用例获取token，创建测试类，使用中间参数关联token
class Test(unittest.TestCase):
    def setUpClass(cls):
        cls.token = get_token()
        print("获取到当前用例token值：%s" % cls.token)

    def test_get_token(self):
        '''获取token测试用例'''
        body1 = {
            "a": "111111",
            "b": "111111",
            "token": self.token  # 参数关联
        }
        print("用例body：%s" % body1)


# 多个用例脚本获取同一个token
def login(user = 'jia', psw = '1234'):
    '''
    先执行登录，传账号和密码两个参数
    :return: 返回token值
    '''
    print("登录的账号名称：%s" % user)
    print("输入的密码：**********")
    token = "xxxxxxxxx"  # 登录后获取到的token值
    return token


def write_yaml(value):
    '''
    把获取到的token值写入到yaml文件
    :param value:
    :return:
    '''
    ypath = os.path.join(curpath, 'token.yaml')
    print ypath
    # 需要写入的token
    t = {'token': value}
    # 写入到yaml文件
    with open(ypath, 'w', encoding='utf-8') as f:
        yaml.dump(t, f, Dumper=yaml.RoundTripDumper)


def all_case(rule="test*.py"):
    '''加载所有的测试用例'''
    case_path = os.path.join(curpath, 'case')
    # 定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(case_path, pattern=rule, top_level_dir=None)
    return discover


# def run_case(all_case,):
    # report_path = os.path.join(curpath, 'report')
    # # 如果用例文件夹不存在，新建一个
    # if not os.path.exists(report_path):
    #     os.mkdir(report_path)
    # suite = unittest.TestSuite()
    # suite.addTest(all_case)


if __name__ == '__main__':
    token = login('admin', '1234')
    write_yaml()
#    get_token()
    allcase = all_case()
    suite = unittest.TestSuite()
    suite.addTest(allcase)
