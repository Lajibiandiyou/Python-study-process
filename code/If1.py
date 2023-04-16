# coding=gbk


cars = ['audi', 'bmw', 'toyota'];

for car in cars:
    if(car != 'audi'): # bool 表达式 检查相等时会检查大小写, 因为大写和小写字母的ASCII码不一样
        print('car is ' + car.upper()); # 一样的, python以缩进来判断if和else的条件是不是同一个
    else: 
        print('car is :{}\t'.format(car.upper()) + car.title());
        # format 格式化将花括号内字段进行替换
        print(f'car is :{car.upper()}\t'+ car.title());
        # 同上, 只是语法更加简单了

print('for loop ends');
print(car); # 这里for循环应该结束了吧, 但是仍然可以打印输出
# 

## 检查多个条件

if(not 1 > 0 and 1 > -1): # 多个条件用 and or 连接
    print('Yeah');
else:
    print('Wrong');

# in 和 not in 
list1 = ['A', 'B', 'C'];
if('A' in list1):
    print('A is in list1');
if('D' not in list1):
    print('D isnot in list1');