# coding=gbk

import unittest # 导入该模块
from UnitTestSlave import get_fomatted_name # 要测试的函数

class NamesTestCase(unittest.TestCase): # 继承unittest.TestCase类
    """测试UnitTestSlave的get_fomatted_name函数"""

    def test_first_last_name(self): # 以test_打头的方法都将自动运行
        
        formatted_name = get_fomatted_name('janis', 'joplin');
        self.assertEqual(formatted_name, 'Janis Joplin'); # 断言, 
        pass;

    pass;

unittest.main();