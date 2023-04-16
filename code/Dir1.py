# coding=gbk

alien_0 = {'color': 'green',
          'points': 5
          }; # 缩进格式
print(alien_0); # 打印该字典
print(alien_0['color']); # 根据Key 'color' 访问字典中的Value 'green'
print(alien_0['points']); # 根据Key 'points' 访问字典中的Value 5
print(len(alien_0));# 字典大小(即键值对个数)


new_points = alien_0['points'];
print('You earn ' + str(new_points) + ' points');

alien_0['x_position'] = 0;
alien_0['y_position'] = 25; # 添加键值对 最后字典中键值对的顺序和添加顺序一致吗? 不一致
# 翻找字典这一过程对应着哈希算法, 对Key进行Hash%TableSize后找到Value, 所以print它就是无序输出
print(alien_0);


alien_empty = {};
alien_empty['color'] = 'green';
alien_empty['points'] = 5;
print(alien_empty); # 先创建空字典, 之后向其中添加Key, Value

alien_empty['color'] = 'red';
alien_empty['points'] = 10; # 修改字典中的值, 其实和添加一个原理
# 先对Key做Hash%TableSize之后, 如果发现为空, 则是添加操作, 如果不为空则发生了Hash冲突现象, 
# 此时判断两个Key是否相等, 不相等的话仍然是添加操作, 相等的话是修改操作

del alien_empty['color']; # 删除字典中的KV(KeyValue)对

person = {
    'first_name': 'Andy',
    'last_name': 'Loos',
    'age': 24,
    };

for key, value in person.items(): # items()返回可遍历的KV元组数组 元组是不可更改的
    print('Key = ' + str(key));
    print('Value = ' + str(value));

for entry in person.items():
    print('Key = ' + str(entry[0]) + ', Value = '+ str(entry[1]));

for i in person.items():
    print('元组为: ', i);

for key in person.keys(): # 写成 in person 也可以, 因为 字典遍历默认遍历Key 它返回一个列表
    print('Key = ' + key + ', Value = ' + str(person[key])); # 通过Key访问Value

for key in sorted(person.keys()): # 对字典的Key排序
    print('Key = ' + key);

for value in person.values(): # 遍历字典Value 结果中可能会有重复
    print('Value = ' + str(value));

for value in set(person.values()): # 这样子就不会有重复了
    print('Value = ' + str(value));


#### 字典列表
fruit_1 = {'category': 'apple', 'price': 5};
fruit_2 = {'category': 'banana', 'price': 11};
fruit_3 = {'category': 'watermelon', 'price': 1};
fruits = [fruit_1, fruit_2, fruit_3];
print(fruits)

#### 列表字典
pizza = {
    'curst': 'thick',
    'toppings': ['mushroom', 'cheese'],
    };
print(pizza);
#### 字典字典
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