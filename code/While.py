# coding=gbk


### һ��ѭ����ѭ������, ѭ�������, ��ѭ����������ʱ, ��ִ��ѭ�����ڵ����, ��������ѭ��
current_num = 1;
while current_num <= 5: # ѭ������
    print(current_num); # ����������ѭ����
    current_num += 1; 
    
prompt = "\nTell me something, and I will repeat it back to you:";
prompt += "\nEnter 'quit' to end the program. ";
message = ""; # ָ��һ����ʼֵ�Խ���whileѭ��
while message != 'quit':
    message = input(prompt);
    if message != 'quit':
        print(message);
    # һ��ʼд������������, ʧ��ʧ��
    #if message == 'quit':
    #    break;
    #else: 
    #    print(message);
print('--------------------------------');

### ͨ�������, �ܶ�����(����)����ʹ�ó�������ѭ��, ����˵�û���Ҫ�˳���ʱ��, ��������'no'
### Ҳͬ����������'quit', ����������'exit', '\q'��, ���ܲ���while��ѭ����������Щ���� OR ��������
### ���ԾͿ�����һ����־λ, ���û�����������˳�����ʱ, �Ϳ��Խ���־λ��False, �˳�ѭ��
### ��û�з������STM32���жϺ�����? ����STM32��ADC�жϱ�־λ��EOC, JEOC��AWD, ��������������һ���ж�
### ����ʱ, �������ADC_IRQHandler���������ж�, ���ж����ҿ��Ը��ݲ�ͬ���жϱ�־λ���в�ͬ�Ĵ�����
flag = True;
while flag:
    message = input('Continue? ');

    if message.lower() == 'no':
        flag = False;
    elif message.lower() == 'quit':
        flag = False;
    else:
        print(message);

### ѭ���е�break��continue, break��������ǰѭ��, ִ��ѭ��������
### ��continue������������ѭ��, ִ����һ��ѭ��
for i in range(1,30):
    if(i & 1 == 1): # ���������
        print(i);
    else:
        continue;

for i in range(1,30):
    if(i & 1 == 1): # ���������
        print(i);
    else:
        break;

### �ƶ��б�Ԫ��
unused_fruits = ['apple', 'banana', 'graph', 'apple', 'apple', 'graph'];
used_fruits = [];

while unused_fruits: # ������Interceptor, ���б�Ԫ�ؽ��й���, ֻ���·��ظ�Ԫ��
    cur_fruit = unused_fruits.pop(); # ������set����
    if cur_fruit not in used_fruits:
        used_fruits.append(cur_fruit);

print(used_fruits);

### ɾ���б�Ԫ��
fruits = ['apple', 'banana', 'graph', 'apple', 'apple', 'graph'];

while 'apple' in fruits: # ������Interceptor, ���б�Ԫ�ؽ��й���
    fruits.remove('apple');

print(fruits);