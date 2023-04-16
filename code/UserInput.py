# coding=gbk
 
message = input('Waiting User Command.....'); # 取得用户输入键盘后, 将其存入变量message中
print(message + '\t' + str(type(message))); # 获取的message是str类型

age = input('How old are you?');
age_int = int(age);
print('Your age is ' + age + str(type(age))); # 这时候希望age是int型, 方便后续计算, 此时可以
#通过用int类型转换来将str类型转换为int类型
print('Your age_int is ' + str(age_int) + str(type(age_int)));

年龄 = int(input('你的年龄是?')); # 可以用中文作为变量名, 反正都会用gbk转换为编码
if 年龄 > 16:
    print('年龄为: ' + str(年龄) + ', 合法')
else:
    print('年龄为: ' + str(年龄) + ', 非法');

number = int(input('Even Or Odd? '));
if number & 1 == 0: # 也可以写为 number % 2 == 0
    print(str(number) + ', its even');
else:
    print(str(number) + ', its odd');