# coding=gbk
### open(filename[, mode[, buffering]]) ����
### name �ļ��� 
### mode �ļ���ģʽ
### 'r' �� 'w' д, �Ḳ����������
### buffering �����ļ�����, ���̲��ǰ����ֽڶ�д��, ���ǽ����̷�Ϊ�ܶ����ж�д
### ����һ����Ϊ4096�ֽ�, �Ǿ���ζ��д��һ���ֽں�д��4096���ֽڶ���Ҫһ��I/O����
### ���ǵ���ʱ����ͬ�ġ����������Ϊ�����Ч�ʾ�Ҫ����I/O�����Ĵ�����ʹ�õ��ֶξ���Ϊ#�ļ�����һ��������
### ����Ҫд����ֽ�������һ�����豸��С��ʱ����ô�����뻺�������У��չ�һ����Ĵ�С�ŵ���һ��ϵͳ���á�
### ȫ����, ��������һ����С�����Ǹ������ͽ���һ��ϵͳ����
### �л���, ����һ�����з��ͽ���һ�����Ҳ����һ��ϵͳ����
### �޻���, ϣ��ʵʱд���ļ����紮���豸

filename = 'pi_digits.txt';
### һ���Զ�ȡ�ļ�����
with open(filename) as file_object:
    # open(str) str����Ҫ�򿪵��ļ���, ��Ϊ����·�������·��
    # with ������Ҫ�����ļ�����ر� 
    # ʹ��withʱ, open()���ص��ļ�����ֻ��with������ڿ��� Ϊʲô? ��Ϊwith�������IO�ر�, �ļ��޷�����
    contents = file_object.read(); # ��ȡ�ļ�ȫ������ �ڵ����ļ�ĩβʱ����һ�����ַ���
    print(contents); 
    pass;

#file_object.read(); # ValueError: I/O operation on closed file.

### ���ж�ȡ�ļ�����
with open(filename) as file_object:
    for line in file_object:
        print(line); # �ļ���ÿ��ĩβ��һ�����з�, Windows����\r\n, ���Զ�ȡ�ļ�print��ʱ��Ҳ�Ὣ���з���ӡ
        #print(line.rstrip()); # �����ӾͲ����л��з��� ����ɾ���ո�, ���з�, �س���, �Ʊ��
        pass;
    pass;

with open(filename) as file_object:
    lines = file_object.readlines(); # ����list[str]
    pass;

for line in lines:
    print(line.rstrip());
    pass;

pi_string = '';
for line in lines:
    pi_string += line.rstrip();
    pass;
print(pi_string);
print(len(pi_string));
print(pi_string[ : 10]); # ��str��Ƭ, ֻ�õ���С������λ


### д���ļ�
filename = 'programming.txt';

with open(filename, 'w') as file_object: # ���ļ������� �����ȴ����ļ�
    file_object.write('I Love Programming.....\r\n'); # ֻ�ܽ��ַ���д���ļ�
    print('successful write');
    pass;


