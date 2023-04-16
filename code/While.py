# coding=gbk


### 一个循环由循环条件, 循环体组成, 当循环条件满足时, 就执行循环体内的语句, 否则跳出循环
current_num = 1;
while current_num <= 5: # 循环条件
    print(current_num); # 以下两行是循环体
    current_num += 1; 
    
prompt = "\nTell me something, and I will repeat it back to you:";
prompt += "\nEnter 'quit' to end the program. ";
message = ""; # 指定一个初始值以进入while循环
while message != 'quit':
    message = input(prompt);
    if message != 'quit':
        print(message);
    # 一开始写成了下面这样, 失败失败
    #if message == 'quit':
    #    break;
    #else: 
    #    print(message);
print('--------------------------------');

### 通常情况下, 很多因素(条件)都会使得程序跳出循环, 比如说用户想要退出的时候, 可以输入'no'
### 也同样可以输入'quit', 还可能输入'exit', '\q'等, 那总不能while的循环条件把这些都用 OR 或起来吧
### 所以就可以用一个标志位, 当用户的输入符合退出条件时, 就可以将标志位置False, 退出循环
### 有没有发现这和STM32的中断很像呢? 比如STM32的ADC中断标志位有EOC, JEOC和AWD, 当以上三个任意一个中断
### 发生时, 都会进入ADC_IRQHandler函数处理中断, 在中断中我可以根据不同的中断标志位进行不同的处理了
flag = True;
while flag:
    message = input('Continue? ');

    if message.lower() == 'no':
        flag = False;
    elif message.lower() == 'quit':
        flag = False;
    else:
        print(message);

### 循环中的break和continue, break是跳出当前循环, 执行循环后的语句
### 而continue则是跳过本次循环, 执行下一次循环
for i in range(1,30):
    if(i & 1 == 1): # 如果是奇数
        print(i);
    else:
        continue;

for i in range(1,30):
    if(i & 1 == 1): # 如果是奇数
        print(i);
    else:
        break;

### 移动列表元素
unused_fruits = ['apple', 'banana', 'graph', 'apple', 'apple', 'graph'];
used_fruits = [];

while unused_fruits: # 类似于Interceptor, 对列表元素进行过滤, 只留下非重复元素
    cur_fruit = unused_fruits.pop(); # 类似于set操作
    if cur_fruit not in used_fruits:
        used_fruits.append(cur_fruit);

print(used_fruits);

### 删除列表元素
fruits = ['apple', 'banana', 'graph', 'apple', 'apple', 'graph'];

while 'apple' in fruits: # 类似于Interceptor, 对列表元素进行过滤
    fruits.remove('apple');

print(fruits);