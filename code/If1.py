# coding=gbk


cars = ['audi', 'bmw', 'toyota'];

for car in cars:
    if(car != 'audi'): # bool ���ʽ ������ʱ�����Сд, ��Ϊ��д��Сд��ĸ��ASCII�벻һ��
        print('car is ' + car.upper()); # һ����, python���������ж�if��else�������ǲ���ͬһ��
    else: 
        print('car is :{}\t'.format(car.upper()) + car.title());
        # format ��ʽ�������������ֶν����滻
        print(f'car is :{car.upper()}\t'+ car.title());
        # ͬ��, ֻ���﷨���Ӽ���

print('for loop ends');
print(car); # ����forѭ��Ӧ�ý����˰�, ������Ȼ���Դ�ӡ���
# 

## ���������

if(not 1 > 0 and 1 > -1): # ��������� and or ����
    print('Yeah');
else:
    print('Wrong');

# in �� not in 
list1 = ['A', 'B', 'C'];
if('A' in list1):
    print('A is in list1');
if('D' not in list1):
    print('D isnot in list1');