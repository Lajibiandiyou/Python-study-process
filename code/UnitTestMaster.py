# coding=gbk

import unittest # �����ģ��
from UnitTestSlave import get_fomatted_name # Ҫ���Եĺ���

class NamesTestCase(unittest.TestCase): # �̳�unittest.TestCase��
    """����UnitTestSlave��get_fomatted_name����"""

    def test_first_last_name(self): # ��test_��ͷ�ķ��������Զ�����
        
        formatted_name = get_fomatted_name('janis', 'joplin');
        self.assertEqual(formatted_name, 'Janis Joplin'); # ����, 
        pass;

    pass;

unittest.main();