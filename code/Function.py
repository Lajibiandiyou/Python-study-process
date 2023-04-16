# coding=gbk


### 函数结构. 
### 文档字符串 是什么
### 有参/无参/有返回值/无返回值

### 位置实参 
def get_pet(type, name):
    """得到宠物信息"""
    print('type: ' + type + ', name: ' + name);
get_pet('Dog', 'Los'); # 参数位置要和函数定义的位置相同
### 关键字实参
get_pet(type = 'Cat', name = 'AA'); # 这时候参数位置就随意了, 因为形参和实参已经相互绑定了
get_pet(name = 'Cat', type = 'AA'); 
#get_pet(name = 'Cat', name = 'AA'); # 显然不行, repeat argument
#get_pet(name = 'Cat'); # 显然不行, required argument

### 参数默认值
### 在设置参数默认值时, 在形参列表中需要先列出没有默认值的形参, 
### 在列出有默认值的形参, 保证Python能够正确解读参数
def get_color(color = 'RED'): # 设置参数默认值
    print('The Color is ' + color);

get_color(); # 不写实参, 则color为'RED'
get_color('GREEN');# 写了实参, 则color为实参'GREEN'

### 列表和字典实参

### 具有返回值的函数 那多个返回值的怎么办?
def get_name(name, middle = ''):
    return middle + name.title();

print(get_name('ssss'))

### 返回字典
def build_person(first_name, last_name, age = -1):
    person = {'first': first_name, 'last': last_name};
    if age >= 0:
        person['age'] = age;
    return person;

print(build_person('Python', 'C++', -222));

### 传递列表 
friends = ['luc', 'eee', 'ddd', 'abc'];
def greet_users(users):
    for user in users:
        print('Greeting, ' + user.title() + '!!!'); # 可以对列表进行遍历, 也可以修改它
        user = 'new'; # 修改不了的, 因为for each语句得到的是列表元素的副本, 而不是原本的列表元素

greet_users(friends);
print(friends);

### 当不想将作为参数的列表修改时 可以在传输参数时将列表的拷贝传递, 如
greet_users(friends[:]); # 切片, 代表创建列表的副本(深拷贝)

### 任意数量的实参
def make_pizza(*toppings): # 将topping作为元组传入函数 * 表示创建一个名为toppings的元组
    print(toppings); # 元组不可修改, 任何修改, 删除, 添加元素操作都会生成一个新元组(id 变了)
### 然而, 任意数量的实参之恩那个放在函数参数列表的最后, 否则不知道参数的对应关系了
### Python先匹配位置实参和关键字实参, 之后将余下的实参都收集到最后一个形参中

make_pizza('A');
make_pizza('C', 'A', 'D');

arr = (1 ,'d', 'ss');
print(id(arr));
print(id(arr + (1, 'AA')))

def get_info(name, **info):
    profile = {};
    profile['name'] = name.title();
    for k, v in info.items():
        profile[k] = v;
    return profile;

print(get_info('cody', address = 'Tree', Tel = '123456')); # 这里千万不能用 'address' = 'Tree'
# 因为 'address' 是一个字符串, 不能对字符串赋值




