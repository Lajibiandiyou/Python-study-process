# coding=gbk

print('Divide two numbers, and type q to quit.');

while True:
    first = input('the first number: ');
    if first == 'q':
        break;
    second = input('the second number: ');
    if second == 'q':
        break;
    try:
        answer = int(first) / int(second); # ���������쳣�Ĵ����
        pass;
    except BaseException: # ������쳣��, BaseException�������쳣�ĸ���
       # ������, SystemExitϵͳ�˳�, KeyboardInterrupt�û��ж�ִ�� 
       # GeneratorExit�������쳣 �� Exception�����쳣�Ļ���
        print('Check your input numbers');
        pass;
    else: # try�����ִ�гɹ���ִ��else�����
        print(answer);
        pass;
    
    pass;


filename = 'alice.txt';

try:
    with open(filename, encoding = 'gbk', errors = 'ignore') as file_object:
        contents = file_object.read();
        pass;
    pass;
except FileNotFoundError:
    msg = 'Sorry, the file ' + filename + ' does not exist.';
    print(msg);
    pass;
else:
    words = contents.split(); # ��contents���ݿհ׷ֿ�, ����list[LiteralString]
    num_words = len(words);
    print('The file has ' + str(num_words) + ' words.');