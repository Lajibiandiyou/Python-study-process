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
        answer = int(first) / int(second); # 可能引发异常的代码块
        pass;
    except BaseException: # 引起的异常类, BaseException是所有异常的父类
       # 它包括, SystemExit系统退出, KeyboardInterrupt用户中断执行 
       # GeneratorExit生成器异常 和 Exception常规异常的基类
        print('Check your input numbers');
        pass;
    else: # try中语句执行成功则执行else中语句
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
    words = contents.split(); # 将contents根据空白分开, 返回list[LiteralString]
    num_words = len(words);
    print('The file has ' + str(num_words) + ' words.');