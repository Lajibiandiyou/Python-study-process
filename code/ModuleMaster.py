# coding=gbk
### ModuleMaster
def say():
    print('HELLO but in ModuleMaster')
### ��������ģ�麯��
import ModuleSlave as slave # ��ģ������� ʹ�ô�����Ӽ�� 
### module_name.function_name(parameters)
ModuleSlave.say(); # Ҫ���ñ�����ģ��ĺ���, ��Ҫָ������ģ�����ƺͺ�����(��ֹ��д�����ط���)

### �����ض�����
### from module_name import function_name1, function_name2
from ModuleSlave import say # ��ʱ��Ͳ�ָͬ������ģ��������
say();

### �����������
from ModuleSlave import say as say_something # ��ֹ��������
say_something(); # ����ModuleSlave��say
say(); # ����ModuleMaster��say

### �������к���
from ModuleSlave import *
