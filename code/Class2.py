# coding=gbk

class Battery(object):

    def __init__(self, battery = 70):
        self.battery = battery;
        pass;

    def print_battery(self):
        print(str(self.battery) + '-kWh battery');

    pass;

class Car(object): # ���object��ʾCar�ĸ�����ʲô(��������object)

    def __init__(self, make, model ,year):
        self.make = make;
        self.model = model;
        self.year = year;
        self.odometer_reading = 0; # __init__������Ҫ�����б���ȫ������, ��ʹ�����û����ɼ�/�û������޸�
        pass;

    def read_odometer(self):
        print('This car has ' + str(self.odometer_reading) + ' miles on it.');
        pass;

    def update_odometer(self, mileage):
        self.odometer_reading = mileage;
        pass;

    pass;

car = Car('audi', 'a4', 2016);
### �޸�����ֵ
car.odometer_reading = 12; # ֱ�ӷ�������
car.read_odometer();

car.update_odometer(122); # �÷���ʵ�ַ�װ, ����ֱ���ʵ�������޸�, ����python�з������η���?
### ���ܹ����ʳ�����˶�����ͨ��ֱ�ӷ�������������̱��޸�Ϊ�κ�ֵ��Ҫȷ����ȫ�����˽��л�������⣬�����ر�ע��ϸ�ڡ�
car.read_odometer();

### Car�ֱ����, ���ͳ�, ���ͳ�, �綯����. �����೵��Car�����Ա�ʾΪ is a �Ĺ�ϵ,
### ���Կ����ü̳зֱ𴴽�GasolineCar, DesselCar��ElectricCar

class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year); # ���ø����__init__����
        # �������ʼ��ǰ, �϶�Ҫ���ø���__init__����, ��Ϊ������Է��ʸ������, ���ɵ��ø������ⷽ��
        self.battery = Battery(); # ������в�ͬ�ڸ��������
        pass;
    
    pass;

eCar = ElectricCar('d','a', 2);
print(type(eCar));
eCar.read_odometer();
eCar.battery.print_battery();

### ������д, ���ඨ��һ���͸�����ͬ(ͬ��, �Ҳ����б�ҲҪ��ͬ)�ķ���, 
### ������ʵ�����ø÷���ʱ, ��������ø��෽��, ���ǵ���������д��ķ���
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

