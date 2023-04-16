# coding=gbk

class Dog(object):
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


dog = Dog('willie', 6);
print(dog);
dog.print();
dog.sit();