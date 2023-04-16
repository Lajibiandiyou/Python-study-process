# coding=gbk
### ModuleMaster
def say():
    print('HELLO but in ModuleMaster')
### 导入整个模块函数
import ModuleSlave as slave # 给模块起别名 使得代码更加简洁 
### module_name.function_name(parameters)
ModuleSlave.say(); # 要调用被导入模块的函数, 需要指定导入模块名称和函数名(防止重写和重载发生)

### 导入特定函数
### from module_name import function_name1, function_name2
from ModuleSlave import say # 这时候就不同指定导入模块名称了
say();

### 给函数起别名
from ModuleSlave import say as say_something # 防止函数覆盖
say_something(); # 调用ModuleSlave的say
say(); # 调用ModuleMaster的say

### 导入所有函数
from ModuleSlave import *
