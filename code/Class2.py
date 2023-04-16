# coding=gbk

class Battery(object):

    def __init__(self, battery = 70):
        self.battery = battery;
        pass;

    def print_battery(self):
        print(str(self.battery) + '-kWh battery');

    pass;

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
car.read_odometer();

car.update_odometer(122); # 用方法实现封装, 避免直接怼实例属性修改, 但是python有访问修饰符吗?
### 但能够访问程序的人都可以通过直接访问属性来将里程表修改为任何值。要确保安全，除了进行基本检查外，还需特别注意细节。
car.read_odometer();

### Car分别多种, 汽油车, 柴油车, 电动车等. 这三类车和Car都可以表示为 is a 的关系,
### 所以可以用继承分别创建GasolineCar, DesselCar和ElectricCar

class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year); # 调用父类的__init__方法
        # 在子类初始化前, 肯定要调用父类__init__方法, 因为子类可以访问父类变量, 并可调用父类任意方法
        self.battery = Battery(); # 子类具有不同于父类的属性
        pass;
    
    pass;

eCar = ElectricCar('d','a', 2);
print(type(eCar));
eCar.read_odometer();
eCar.battery.print_battery();

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

