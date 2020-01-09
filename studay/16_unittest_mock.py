#!/usr/bin/python
# -*- coding: UTF-8 -*-
import mock
import unittest
import temple


# 单元测试用例mock模块
class TestZhiFuStatus(unittest.TestCase):

    def test_01(self):
        # 测试支付成功场景
        # mock一个支付成功的场景
        temple.zhifu = mock.Mock(return_value={'result': 'success', 'reson': 'null'})
        # 根据结果页面跳转
        status = temple.zhifu_statues()
        print status
        self.assertEquals(status, '支付成功')

    def test_02(self):
        '''测试支付失败场景'''
        # mock一个支付失败的数据
        temple.zhifu = mock.Mock(return_value={"result": "fail", "reason": "余额不足"})
        # 根据支付结果测试页面跳转
        statues = temple.zhifu_statues()
        self.assertEqual(statues, "支付失败")

    def test_03(self):
        temple.zhifu = mock.Mock(return_value={'result': 'wait', 'reason': 'null'})
        status = temple.zhifu_statues()
        self.assertEquals(status, '未知错误异常')

    def test_04(self):
        temple.zhifu = mock.Mock(return_value={'resultoo': 'wait', 'reason': 'null'})
        status = temple.zhifu_statues()
        self.assertEquals(status, 'Error, 服务端返回异常!')


# 单元测试用例mock.patch
class TestZhiFuPatch(unittest.TestCase):
    @mock.patch('temple.zhifu')
    def test_01(self, mock_zhifu):
        # 方法一：mock一个支付成功的数据
        # temple.zhifu = mock.Mock(return_value={"result": "success", "reason":"null"})

        # 方法二：mock.path装饰器模拟返回结果
        mock_zhifu.return_value = {"result": "success", "reason": "null"}
        # 根据支付结果测试页面跳转
        statues = temple.zhifu_statues()
        print(statues)
        self.assertEqual(statues, "支付成功")

    @mock.patch("temple.zhifu")
    def test_02(self, mock_zhifu):
        '''测试支付失败场景'''
        # mock一个支付成功的数据

        mock_zhifu.return_value = {"result": "fail", "reason": "余额不足"}
        # 根据支付结果测试页面跳转
        statues = temple.zhifu_statues()
        self.assertEqual(statues, "支付失败")


# 模拟的对象为类的时候
class Test_zhifu_statues(unittest.TestCase):
    '''单元测试用例'''

    @mock.patch("temple.Zhifu")
    def test_01(self, mock_Zhifu):
        '''测试支付成功场景'''
        a = mock_Zhifu.return_value  # 先返回实例，对类名称替换
        # 通过实例调用方法，再对方法的返回值替换
        a.zhifu.return_value = {"result": "success", "reason":"null"}
        # 根据支付结果测试页面跳转
        statues = temple.Statues().zhifu_statues()
        print(statues)
        self.assertEqual(statues, "支付成功")

    @mock.patch("temple.Zhifu")
    def test_02(self, mock_Zhifu):
        '''测试支付失败场景'''
        b = mock_Zhifu.return_value  # 先返回实例，对类名称替换
        # 通过实例调用方法，再对方法的返回值替换
        b.zhifu.return_value = {"result": "fail", "reason": "余额不足"}
        # 根据支付结果测试页面跳转
        statues = temple.Statues().zhifu_statues()
        print(statues)
        self.assertEqual(statues, "支付失败")


if __name__ == "__main__":
    unittest.main()