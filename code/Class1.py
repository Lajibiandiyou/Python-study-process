# coding=gbk

class Dog(object):
    """Dog��"""
     
    def __init__(self, name, age): # ÿ������Dogʵ��ʱ, �����Զ������������, ������Java�еĹ�����
        # ��C++�еĹ��캯��
        """��ʼ��"""
        self.name = name; # ��selfΪǰ׺�ı������Թ��������з���ʹ��
        self.age = age; # ��ͨ�����ഴ�����κ�ʵ�����ɷ��ʸñ���/�޸ı���ֵ
        pass;

    def sit(self): # ΪDog�ഴ���ķ���, ��Ҫ�ֶ�Dogʵ������
        print(self.name.title() + ' is sitting');
        pass;

    def roll_over(self): # ΪDog�ഴ���ķ���, ��Ҫ�ֶ�Dogʵ������
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