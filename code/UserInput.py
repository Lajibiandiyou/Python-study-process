# coding=gbk
 
message = input('Waiting User Command.....'); # ȡ���û�������̺�, ����������message��
print(message + '\t' + str(type(message))); # ��ȡ��message��str����

age = input('How old are you?');
age_int = int(age);
print('Your age is ' + age + str(type(age))); # ��ʱ��ϣ��age��int��, �����������, ��ʱ����
#ͨ����int����ת������str����ת��Ϊint����
print('Your age_int is ' + str(age_int) + str(type(age_int)));

���� = int(input('���������?')); # ������������Ϊ������, ����������gbkת��Ϊ����
if ���� > 16:
    print('����Ϊ: ' + str(����) + ', �Ϸ�')
else:
    print('����Ϊ: ' + str(����) + ', �Ƿ�');

number = int(input('Even Or Odd? '));
if number & 1 == 0: # Ҳ����дΪ number % 2 == 0
    print(str(number) + ', its even');
else:
    print(str(number) + ', its odd');