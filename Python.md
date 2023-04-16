

### 布尔运算符

in

not in

and

or

not

### pass语句

![img](pic\v2-59832e7ddbc7592810ebe5f27923b5e3_r.jpg)

简单而言，pass 是一种空操作（null operation），解释器执行到它的时候，除了检查语法是否合法，什么也不做就直接跳过。

还有一个优点就是使得空函数等不报错

```python
def fun_void():
    
fun_void();
```

![image-20230416093634428](pic\image-20230416093634428.png)

```python
def fun_void():
    pass # 加上pass之后, 就表示函数体有语句, 就不会报错了

fun_void();
```

### 列表

#### 创建, 访问, 添加, 删除元素

```python
# coding=gbk
names = ['James', 'Cody', 'Chris', 'Booker'];
print('init names: ');
print(names);
print('names[0]=' + names[0])
print('names[-1]=' + names[-1]) #索引为负则返回从后往前数的元素

names.append('Paul');
print('after append Paul');
print(names);
names.insert(1, 'Andy');
print('after insert Andy at index 1');
print(names);

del names[0];
print('after del index 0 ')
print(names);

poped_name = names.pop(); # 可以有参数, 即删除特定索引的元素
print('pop the last one')
print('poped name =' + poped_name);
print(names);

names.remove('Cody'); #若元素不存在则报错
print('remove Cody')
print(names);
```

<img src="pic\image-20230410095206381.png" alt="image-20230410095206381" style="zoom: 67%;" />

#### 对列表排序, 翻转, 求列表长度

```python
names.sorted(); #临时排序列表, 不会更改原列表元素顺序
print('顺序排序')
names.sort();
print(names);
print('逆序排序')
names.sort(reverse = True);
print(names);
print('反转names')
names.reverse();
print(names);
print('列表长度 = ' + str(len(names)));
```



![image-20230410100015093](pic\image-20230410100015093.png)



#### 遍历列表

```python
print('遍历names')
for name in names:
    print(name.title());
    
    print('Great!');# 在循环中, 只要有缩进, 就认为这个语句属于循环, 即使中间有空行,所以执行多次
print('end of loop');# 这里没有空行, 但是没有缩进了, 所以执行一次
```

![image-20230410102359241](pic\image-20230410102359241.png)

#### range()

```python
#coding=gbk

for value in range(1, 20, 4): 
    print(value);

numbers = list(range(1, 6));
print(numbers);

even_numbers = list(range(2, 11, 2));
print(even_numbers);

odd_numbers = list(range(1, 11, 2));
print(odd_numbers);
```

#### 统计计算

```pyhton
#统计计算
print(min(odd_numbers));
print(max(odd_numbers));
print(sum(odd_numbers));
```

#### 列表解析

将for循环和创建新元素整合在一起

```python
squares = [value ** 2 for value in range(1, 11)]; 
print(squares);
```

#### 列表切片

选定列表的一部分, 进行处理

```python
print(squares[-3:-2]); # 取倒数第三个元素

for square in squares[:4]: # 取列表前四个元素
    print(square);

print(squares);
```

#### 复制列表

```python
squares_copy_depth = squares[:]; # 深拷贝, 即将列表中所有元素重新赋值
                            #给新列表, 二者的id不相同
squares_copy_shallow = squares; # 浅拷贝, 即将列表的地址赋给新列表, 二者id相同, 且其中元素id也相同
print('origin list')
print(squares);
print('its id is ', id(squares), 'and the first element id of it is ', id(squares[0]));
print('squares_copy_depth list')
print(squares_copy_depth);
print('its id is ', id(squares_copy_depth), 'and the first element id of it is ', id(squares_copy_depth[0]));
print('squares_copy_shallow list')
print(squares_copy_shallow);
print('its id is ', id(squares_copy_shallow), 'and the first element id of it is ', id(squares_copy_shallow[0]));
```

![image-20230410131205778](pic\image-20230410131205778.png)

#### 元组

不可变的列表, 它的元素不可变, 但是可以重新对其赋值, 

```python
dimension = [50, 200]; # 一个列表
print(dimension);
dimension[0] = 1; # 更改其元素, 可以
dimension_unchangable = (50, 200); # 一个元组
print(dimension_unchangable);
dimension_unchangable[0] = 5; # 不能更改其元素 error tuple doest support item assignement 
dimension_unchangable = (2, 5); # 但是可以给变量重新赋值
print(dimension_unchangable);
```

当对元组添加元素时, 会生成一个新的元组

```python
arr = (1 ,'d', 'ss');
print(id(arr));
print(id(arr + (1, 'AA')))
```

![image-20230416090818352](pic\image-20230416090818352.png)

### If 语句

#### 语法格式 if/if-else/if-elif-else

```python
#if condition_is_right: #if语句, 当条件成立时执行
#    statements;

#if condition_is_right: #if-else语句, 当if条件成立时执行statements1, 不成立则执行statements2
#    statements1;
#else:
#    statements2;

#if condition1_is_right: #if-elif-else语句, 当条件成立时执行对应语句, 不成立的话则判断下一个,若所有条件都不成立, 则执行else后的语句
#    statements;
#elif condition2_is_right:
#    statements;
#elif condition3_is_right:
#    statements;
#else: 
#    statements;
```

```python
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
```

![image-20230411123846446](pic\image-20230411123846446.png)

#### 检查多个条件

```python
if(not 1 > 0 and 1 > -1): # 多个条件用 and or 连接
    print('Yeah');
else:
    print('Wrong');
```

and, 所有条件同时成立

or, 任何一个条件成立

not, 条件取反

in 和 not in, 判断元素是否在列表中

```python
list1 = ['A', 'B', 'C'];
if('A' in list1):
    print('A is in list1');
if('D' not in list1):
    print('D isnot in list1');
```

![image-20230411124231867](pic\image-20230411124231867.png)

#### 判断列表为空

当列表非空时执行特定操作, 而当列表为空时报错/打印出错误信息

```python
list1 = [];

if len(list1) == 0: # if not list1: is also right to judge whether the List is empty
    print('empty list');
else:
    for element in list1:
        print(element);
        print('end of loop')
print('end of if')
```

![image-20230411130633306](pic\image-20230411130633306.png)

### 字典

类似于map, 里面存储了Key和Value, Key不能重复, Value可重复. 

我们可根据Key得到Value, 获取字典大小, 或者直接打印字典

```python
alien_0 = {'color': 'green',
          'points': 5
          }; # 缩进格式
print(alien_0); # 打印该字典
print(alien_0['color']); # 根据Key 'color' 访问字典中的Value 'green'
print(alien_0['points']); # 根据Key 'points' 访问字典中的Value 5
print(len(alien_0));# 字典大小(即键值对个数)
```

![image-20230414081038504](pic\image-20230414081038504.png)

#### 向字典添加KV对/修改字典中的KV对

1. 向已经存在的字典中添加KV对

```python
alien_0['x_position'] = 0;
alien_0['y_position'] = 25; # 添加键值对 最后字典中键值对的顺序和添加顺序一致吗? 不一致
# 翻找字典这一过程对应着哈希算法, 对Key进行Hash%TableSize后找到Value, 所以print它就是无序输出
print(alien_0);
```

![image-20230414081320076](pic\image-20230414081320076.png)

2. 向空字典中添加KV对

```python
alien_empty = {};
alien_empty['color'] = 'green';
alien_empty['points'] = 5;
print(alien_empty); # 先创建空字典, 之后向其中添加Key, Value
```

3. 修改字典中的KV对

```python
alien_empty['color'] = 'red';
alien_empty['points'] = 10; # 修改字典中的值, 其实和添加一个原理
# 先对Key做Hash%TableSize之后, 如果发现为空, 则是添加操作, 如果不为空则发生了Hash冲突现象, 
# 此时判断两个Key是否相等, 不相等的话仍然是添加操作, 相等的话是修改操作
```

#### 删除字典中的KV对

```python
del alien_empty['color']; # 删除字典中的KV(KeyValue)对
```

#### 遍历字典的三种方式

```python
person = {
    'first_name': 'Andy',
    'last_name': 'Loos',
    'age': 24,
    };
```

1. 元组遍历

```python
for i in person.items(): # items()返回可遍历的KV元组数组 元组是不可更改的
    print('元组为: ', i);
```

![image-20230414082000448](\pic\image-20230414082000448.png)

2. entry遍历

```python
for entry in person.items():
    print('Key = ' + str(entry[0]) + ', Value = '+ str(entry[1]));
```

![image-20230414082103057](pic\image-20230414082103057.png)

3. KV遍历

```python
for key, value in person.items(): 
    print('Key = ' + str(key));
    print('Value = ' + str(value));
```

![image-20230414082142067](pic\image-20230414082142067.png)

#### 遍历字典的Key和Value

```python
for key in person.keys(): # 写成 in person 也可以, 因为 字典遍历默认遍历Key 它返回一个列表
    print('Key = ' + key + ', Value = ' + str(person[key])); # 通过Key访问Value

for key in sorted(person.keys()): # 对字典的Key排序
    print('Key = ' + key);

for value in person.values(): # 遍历字典Value 结果中可能会有重复
    print('Value = ' + str(value));

for value in set(person.values()): # 这样子就不会有重复了, 因为Set是集合, 集合中不会有重复元素
    print('Value = ' + str(value));
```

![image-20230414082342644](pic\image-20230414082342644.png)

#### 字典和列表的嵌套

在列表中存储字典

```python
fruit_1 = {'category': 'apple', 'price': 5};
fruit_2 = {'category': 'banana', 'price': 11};
fruit_3 = {'category': 'watermelon', 'price': 1};
fruits = [fruit_1, fruit_2, fruit_3];
print(fruits)
```

![image-20230414082549360](pic\image-20230414082549360.png)

在字典中存储列表

```python
pizza = {
    'curst': 'thick',
    'toppings': ['mushroom', 'cheese'],
    };
print(pizza);
```

![image-20230414082657001](pic\image-20230414082657001.png)

在字典中存储字典

```python
users = {
    'james' : {
        'first': 'lay',
        'last': 'james'
        },
    'cody': {
        'first': 'cody',
        'last': 'Q'
        }
    };
print(users)
```

![image-20230414082731952](pic\image-20230414082731952.png)

### 用户输入

input()函数, 用于读取用户键盘输入

```python
message = input('Waiting User Command.....'); # 取得用户输入键盘后, 将其存入变量message中
print(message + '\t' + str(type(message))); # 获取的message是str类型
```

![image-20230414174400452](pic\image-20230414174400452.png)

如果需要将input()读取的输入转换为int的话, 则需要类型转换

```python
age = input('How old are you?');
age_int = int(age);
print('Your age is ' + age + str(type(age))); # 这时候希望age是int型, 方便后续计算, 此时可以
#通过用int类型转换来将str类型转换为int类型
print('Your age_int is ' + str(age_int) + str(type(age_int)));
```

![image-20230414174527753](pic\image-20230414174527753.png)

变量名甚至可以为中文

```python
年龄 = int(input('你的年龄是?')); # 可以用中文作为变量名, 反正都会用gbk转换为编码
if 年龄 > 16:
    print('年龄为: ' + str(年龄) + ', 合法')
else:
    print('年龄为: ' + str(年龄) + ', 非法');
```

![image-20230414174630761](pic\image-20230414174630761.png)

```python
number = int(input('Even Or Odd? '));
if number & 1 == 0: # 也可以写为 number % 2 == 0
    print(str(number) + ', its even');
else:
    print(str(number) + ', its odd');
```

### while 循环

一个循环由循环条件, 循环体组成, 当循环条件满足时, 就执行循环体内的语句, 否则跳出循环

```python
current_num = 1;
while current_num <= 5: # 循环条件
    print(current_num); # 以下两行是循环体
    current_num += 1; 
```

![image-20230414174834477](pic\image-20230414174834477.png)

```python
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
```

#### 用标志位处理循环条件

通常情况下, 很多因素(条件)都会使得程序跳出循环, 比如说用户想要退出的时候, 可以输入'no'也同样可以输入'quit', 还可能输入'exit', '\q'等, 那总不能while的循环条件把这些都用 OR 或起来吧, 所以就可以用一个标志位, 当用户的输入符合退出条件时, 就可以将标志位置False, 退出循环

有没有发现这和STM32的中断很像呢? 比如STM32的ADC中断标志位有EOC, JEOC和AWD, 当以上三个任意一个中断发生时, 都会进入ADC_IRQHandler函数处理中断, 在中断中我可以根据不同的中断标志位进行不同的处理了

```python
flag = True;
while flag:
    message = input('Continue? ');

    if message.lower() == 'no':
        flag = False;
    elif message.lower() == 'quit':
        flag = False;
    else:
        print(message);
```

#### break和continue

循环中的break和continue, break是跳出当前循环, 执行循环后的语句

而continue则是跳过本次循环, 执行下一次循环

```python
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
```

<img src="pic\image-20230414175351643.png" alt="image-20230414175351643" style="zoom: 67%;" />

#### 利用循环移动和删除列表元素

```python
### 移动列表元素
unused_fruits = ['apple', 'banana', 'graph', 'apple', 'apple', 'graph'];
used_fruits = [];

while unused_fruits: # 类似于Interceptor, 对列表元素进行过滤, 只留下非重复元素
    cur_fruit = unused_fruits.pop(); # 类似于set操作
    if cur_fruit not in used_fruits:
        used_fruits.append(cur_fruit);

print(used_fruits);
```

![image-20230414175456280](pic\image-20230414175456280.png)

```python
### 删除列表元素
fruits = ['apple', 'banana', 'graph', 'apple', 'apple', 'graph'];

while 'apple' in fruits: # 类似于Interceptor, 对列表元素进行过滤
    fruits.remove('apple');

print(fruits);
```

![image-20230414175516247](pic\image-20230414175516247.png)

### 函数

```python
### 语法规范
def function_name(parameters_list): #parameters_list可有可无, 有的函数不需要参数
    """函数注释(文档字符串)"""
    # statements
    return value1, value2; # 可选的, 函数可以有返回值, 也可以没有返回值
```

#### 位置实参, 关键字实参

1. 位置实参

```python
def get_pet(type, name):
    """得到宠物信息"""
    print('type: ' + type + ', name: ' + name);
get_pet('Dog', 'Los'); # 参数位置要和函数定义的位置相同
```

![image-20230416090113637](pic\image-20230416090113637.png)

2. 关键字实参

```python
get_pet(type = 'Cat', name = 'AA'); # 这时候参数位置就随意了, 因为形参和实参已经相互绑定了
get_pet(name = 'Cat', type = 'AA'); 
#get_pet(name = 'Cat', name = 'AA'); # 显然不行, repeat argument
#get_pet(name = 'Cat'); # 显然不行, required argument
```

![image-20230416090147070](pic\image-20230416090147070.png)

#### 默认参数

```python
### 在设置参数默认值时, 在形参列表中需要先列出没有默认值的形参, 
### 在列出有默认值的形参, 保证Python能够正确解读参数
def get_color(color = 'RED'): # 设置参数默认值
    print('The Color is ' + color);

get_color(); # 不写实参, 则color为'RED'
get_color('GREEN');# 写了实参, 则color为实参'GREEN'
```

![image-20230416090306079](pic\image-20230416090306079.png)

#### 返回字典

```python
def build_person(first_name, last_name, age = -1):
    person = {'first': first_name, 'last': last_name};
    if age >= 0:
        person['age'] = age;
    return person;

print(build_person('Python', 'C++', -222));
```

![image-20230416090414056](pic\image-20230416090414056.png)

#### 传递列表

```python
friends = ['luc', 'eee', 'ddd', 'abc'];
def greet_users(users):
    for user in users:
        print('Greeting, ' + user.title() + '!!!'); # 可以对列表进行遍历, 也可以修改它
        user = 'new'; # 修改不了的, 因为for each语句得到的是列表元素的副本, 而不是原本的列表元素

greet_users(friends);
print(friends);
```

![image-20230416090455571](pic\image-20230416090455571.png)

```python
### 当不想将作为参数的列表修改时 可以在传输参数时将列表的拷贝传递, 如
greet_users(friends[:]); # 切片, 代表创建列表的副本(深拷贝)
```

#### 任意数量的实参(列表和字典)

1. 列表

```python
def make_pizza(*toppings): # 将topping作为元组传入函数 * 表示创建一个名为toppings的元组
    print(toppings); # 元组不可修改, 任何修改, 删除, 添加元素操作都会生成一个新元组(id 变了)
### 然而, 任意数量的实参之恩那个放在函数参数列表的最后, 否则不知道参数的对应关系了
### Python先匹配位置实参和关键字实参, 之后将余下的实参都收集到最后一个形参中

make_pizza('A');
make_pizza('C', 'A', 'D');
```

![image-20230416090704573](pic\image-20230416090704573.png)

2. 字典

```python
def get_info(name, **info):
    profile = {};
    profile['name'] = name.title();
    for k, v in info.items():
        profile[k] = v;
    return profile;

print(get_info('cody', address = 'Tree', Tel = '123456')); # 这里千万不能用 'address' = 'Tree'
# 因为 'address' 是一个字符串, 不能对字符串赋值
```

![image-20230416090859431](pic\image-20230416090859431.png)

### 模块

通常情况下, 可以将函数放在一个单独的.py文件中, 然后在主文件中将函数文件导入并运行其中的函数

现在有两个.py文件, 分别是ModuleMaster.py和ModuleSlave.py, ModuleSlave.py和ModuleMaster.py文件中均定义了say()函数

```python
### ModuleSlave
def say():
    print('HELLO in ModuleSlave');
```

```python
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
say(); # 调用ModuleSlave的say

### 给函数起别名
from ModuleSlave import say as say_something # 防止函数覆盖
say_something(); # 调用ModuleSlave的say
say(); # 调用ModuleMaster的say

### 导入所有函数
from ModuleSlave import *
```

### 类

#### .py/.pyw文件的区别

py文件

- python最常见的文件，是python项目的源码；
- 文件执行时linux下调用python执行，windows下调用python.exe；
- 如果在终端窗口或IDE执行命令，其相关的print()，或执行结果打印在当前的窗口上；

pyw文件

- pyw文件运行的时候不会出现向pyc文件一样有闪烁的窗口，同时不会打开控制台窗口，相关的print()等输出会失效，程序在后台运行；
- 可以使用双击的办法直接运行pyw文件，系统会调用pythonw.exe来运行；
- 如果需要将相关的信息输出，可以：

```python
pythonw \path\xxx.pyw 1>\path\stdout.txt 2>\path\stderr.txt

# 1代表标准输出，将标准输出重定向到stdout.txt中
# 2代表错误输出，将错误输出重定向到stderr.txt中
```

#### 创建类

```python
class Dog(object): # 这个object表示Dog的父类是什么(在这里是object)
    """Dog类"""
     
    def __init__(self, name, age): # 每当创建Dog实例时, 都会自动调用这个方法, 类似于Java中的构造器
        # 和C++中的构造函数
        """初始化"""
        self.name = name; # 以self为前缀的变量可以供类中所有方法使用
        self.age = age; # 且通过该类创建的任何实例都可访问该变量/修改变量值
        pass;

    def sit(self): # 为Dog类创建的方法, 需要手动Dog实例调用
        print(self.name.title() + ' is sitting');
        pass;

    def roll_over(self): # 为Dog类创建的方法, 需要手动Dog实例调用
        print(self.name.title() + ' rolled over');
        pass;

    def print(self):
        print('This dog is called ' + self.name + ' ,and it\'s ' + str(self.age) + ' years old.');
        pass;

    pass;
```

```python
dog = Dog('willie', 6);
print(dog); # 将打印类名和实例地址
dog.print(); # 一个类方法, 将打印实例信息
dog.sit();
```

![image-20230416095657698](pic\image-20230416095657698.png)

#### self

1. self只有在类的方法中才会有, 在调用时不必传入相应的参数
2. 在类的方法中第一参数永远是self，表示创建的类实例本身，而不是类本身
3. self代表当前对象的地址, 等价于C++中的self指针和Java中的this参数
4. 如果不加self, 表示是类的一个属性(可以通过"类名.变量名"的方式引用), 加了self表示是类的实例的一个属性(可以通过"实例名.变量名"的方式引用)

#### 修改实例属性值

```python
class Car(object): # 这个object表示Car的父类是什么(在这里是object)

    def __init__(self, make, model ,year):
        self.make = make;
        self.model = model;
        self.year = year;
        self.odometer_reading = 0; # __init__里面需要将所有变量全部设置, 即使它对用户不可见/用户不可修改
        pass;

    def read_odometer(self):
        print('This car has ' + str(self.odometer_reading) + ' miles on it.');
        pass;

    def update_odometer(self, mileage):
        self.odometer_reading = mileage;
        pass;

    pass;

car = Car('audi', 'a4', 2016);
### 修改属性值
car.odometer_reading = 12; # 直接访问属性
car.update_odometer(122); # 用方法实现封装, 避免直接怼实例属性修改, 但是python有访问修饰符吗?
### 但能够访问程序的人都可以通过直接访问属性来将里程表修改为任何值。要确保安全，除了进行基本检查外，还需特别注意细节。
car.read_odometer();
```

![image-20230416104402931](pic\image-20230416104402931.png)

#### 继承

Car分别多种, 汽油车, 柴油车, 电动车等. 这三类车和Car都可以表示为 is a 的关系,

所以可以用继承分别创建GasolineCar, DesselCar和ElectricCar

```python
class Battery(object):

    def __init__(self, battery = 70):
        self.battery = battery;
        pass;

    def print_battery(self):
        print(str(self.battery) + '-kWh battery');

    pass;

class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year); # 调用父类的__init__方法
        # 在子类初始化前, 肯定要调用父类__init__方法, 因为子类可以访问父类变量, 并可调用父类任意方法
        self.battery = Battery(); # 子类具有不同于父类的属性 且该属性是另一个类的实例(策略模式)
        pass;
    
    pass;

eCar = ElectricCar('d','a', 2);
print(type(eCar));
eCar.read_odometer();
eCar.battery.print_battery();
```

![image-20230416104449967](pic\image-20230416104449967.png)

#### 重写父类方法

```python
### 方法重写, 子类定义一个和父类相同(同名, 且参数列表也要相同)的方法, 
### 在子类实例调用该方法时, 将不会调用父类方法, 而是调用子类重写后的方法
class Bird(object):

    def __init__(self, name):
        self.name = name;
        pass;

    def fly(self):
        print('Flying.....');
        pass;

    pass;

class InjuredBird(Bird):

    def __init__(self, name):
        super().__init__(name);
        pass;

    def fly(self):
        print('Injured bird can not fly now.');
        pass;

    pass;

bird1 = InjuredBird('a')
bird1.fly();
```

![image-20230416104630603](pic\image-20230416104630603.png)

### 文件

#### 打开文件open()

```python
### open(filename[, mode[, buffering]]) 函数
### name 文件名 
### mode 文件打开模式
### 'r' 读 'w' 写, 会覆盖已有数据 'a' 追加, 不会覆盖已有数据
### buffering 设置文件缓冲, 磁盘不是按照字节读写的, 而是将磁盘分为很多块进行读写
### 假设一个块为4096字节, 那就意味着写入一个字节和写入4096个字节都需要一次I/O操作
### 它们的用时是相同的。在这种情况为了提高效率就要减少I/O操作的次数，使用的手段就是为#文件设立一个缓冲区
### 当需要写入的字节数不足一个块设备大小的时候，那么都放入缓冲区当中，凑够一个块的大小才调用一次系统调用。
### 全缓冲, 缓冲区有一定大小满足那个数量就进行一次系统调用
### 行缓冲, 碰到一个换行符就进行一次输出也就是一次系统调用
### 无缓冲, 希望实时写入文件，如串口设备
```

#### 读取文件

```txt
# pi_digits.txt 文件内容
3.1415926535
8979323846
2643383279
```

```python
filename = 'pi_digits.txt';
### 一次性读取文件内容
with open(filename) as file_object:
    # open(str) str是需要打开的文件名, 分为绝对路径和相对路径
    # with 不再需要访问文件后将其关闭 
    # 使用with时, open()返回的文件对象只在with代码块内可用 为什么? 因为with块结束后IO关闭, 文件无法访问
    contents = file_object.read(); # 读取文件全部内容 在到达文件末尾时返回一个空字符串
    print(contents); 
    pass;

#file_object.read(); # ValueError: I/O operation on closed file.
```

![image-20230416143511523](pic\image-20230416143511523.png)

```python
### 逐行读取文件内容
with open(filename) as file_object:
    for line in file_object:
        print(line); # 文件中每行末尾有一个换行符, Windows下是\r\n, 所以读取文件print的时候也会将换行符打印
        #print(line.rstrip()); # 这样子就不会有换行符了 他会删除空格, 换行符, 回车符, 制表符
        pass;
    pass;
```

![image-20230416143702652](pic\image-20230416143702652.png)

```python
with open(filename) as file_object:
    lines = file_object.readlines(); # 返回list[str]
    pass;

for line in lines:
    print(line.rstrip());
    pass;
```

![image-20230416143751681](pic\image-20230416143751681.png)

```python
pi_string = '';
for line in lines:
    pi_string += line.rstrip();
    pass;
print(pi_string);
print(len(pi_string));
print(pi_string[ : 10]); # 对str切片, 只得到其小数点后八位
```

![image-20230416143818998](pic\image-20230416143818998.png)

#### 写入文件

```python
filename = 'programming.txt';

with open(filename, 'w') as file_object: # 若文件不存在 则首先创建文件
    file_object.write('I Love Programming.....\r\n'); # 只能将字符串写入文件
    print('successful write');
    pass;
```

![image-20230416143920939](pic\image-20230416143920939.png)

### 异常

当出现异常而不处理时, 会导致程序停止, 所以需要对异常进行处理, 维持代码的健壮性

```python
print('Divide two numbers, and type q to quit.');

while True:
    first = input('the first number: ');
    if first == 'q':
        break;
    second = input('the second number: ');
    if second == 'q':
        break;
    try:
        answer = int(first) / int(second); # 可能引发异常的代码块
        pass;
    except BaseException: # 引起的异常类, BaseException是所有异常的父类
       # 它包括, SystemExit系统退出, KeyboardInterrupt用户中断执行 
       # GeneratorExit生成器异常 和 Exception常规异常的基类
        print('Check your input numbers');
        pass;
    else: # try中语句执行成功则执行else中语句
        print(answer);
        pass;
    
    pass;
```

![image-20230416154959608](pic\image-20230416154959608.png)

```python
filename = 'alice.txt';

try:
    with open(filename, encoding = 'gbk', errors = 'ignore') as file_object:
        contents = file_object.read();
        pass;
    pass;
except FileNotFoundError:
    msg = 'Sorry, the file ' + filename + ' does not exist.';
    print(msg);
    pass;
else:
    words = contents.split(); # 将contents根据空白分开, 返回list[LiteralString]
    num_words = len(words);
    print('The file has ' + str(num_words) + ' words.');
```

![image-20230416155055477](pic\image-20230416155055477.png)

### JSON存储数据

模块json让你能够将简单的Python数据结构转储到文件中，并在程序再次运行时加载该文件中的数据。你还可以使用json在Python程序之间分享数据。 更重要的是， JSON数据格式并非Python专用的，这让你能够将以JSON格式存储的数据与使用其他编程语言的人分享。

```python
import json
json.dump(data, f_obj); # 存储信息 参数1, 要存储的数据, 参数2, 存储数据的文件对象
json.load(f_obj); # 加载信息 参数1, 存储数据的文件对象
```

```python
numbers = [2, 3, 5, 7, 11, 13];

filename = 'numbers.json';
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj); # 存储信息 参数1, 要存储的数据, 参数2, 存储数据的文件对象
    pass;

with open(filename, 'r') as f_obj:
    numbers_from_file = json.load(f_obj); # 加载信息 参数1, 存储数据的文件对象
    pass;

print(numbers_from_file)
```

![image-20230416155325336](H:\Python学习\pic\image-20230416155325336.png)

### 代码测试

```python
### 待测试函数, 位于UnitTestSlave.py中
def get_fomatted_name(first, last):
    full_name = first + ' ' + last;
    return full_name.title();
```

```python
### 测试代码 
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
```

#### 一些断言方法

| 方法名                                     | 意义                                    |
| ------------------------------------------ | :-------------------------------------- |
| assertEqual(first, second, msg = None)     | 测试 *first* 和 *second* 是否相等。     |
| assertNotEqual(first, second, msg = None)  | 测试 *first* 和 *second* 是否不等。 如  |
| assertTrue(expr, msg = None)               | 测试 *expr* 是否为真值                  |
| assertFalse(expr, msg = None)              | 测试 *expr* 是否为假值                  |
| assertIs(first, second, msg = None)        | 测试 *first* 和 *second* 是同一个对象   |
| assertIsNot(first, second, msg = None)     | 测试 *first* 和 *second* 不是同一个对象 |
| assertIn(member, container, msg = None)    | 测试 *member* 是 *container* 的成员     |
| assertNotIn(member, container, msg = None) | 测试 *member* 不是 *container* 的成员   |

