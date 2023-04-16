# coding=gbk
### open(filename[, mode[, buffering]]) 函数
### name 文件名 
### mode 文件打开模式
### 'r' 读 'w' 写, 会覆盖已有数据
### buffering 设置文件缓冲, 磁盘不是按照字节读写的, 而是将磁盘分为很多块进行读写
### 假设一个块为4096字节, 那就意味着写入一个字节和写入4096个字节都需要一次I/O操作
### 它们的用时是相同的。在这种情况为了提高效率就要减少I/O操作的次数，使用的手段就是为#文件设立一个缓冲区
### 当需要写入的字节数不足一个块设备大小的时候，那么都放入缓冲区当中，凑够一个块的大小才调用一次系统调用。
### 全缓冲, 缓冲区有一定大小满足那个数量就进行一次系统调用
### 行缓冲, 碰到一个换行符就进行一次输出也就是一次系统调用
### 无缓冲, 希望实时写入文件，如串口设备

filename = 'pi_digits.txt';
### 一次性读取文件内容
with open(filename) as file_object:
    # open(str) str是需要打开的文件名, 分为绝对路径和相对路径
    # with 不再需要访问文件后将其关闭 
    # 使用with时, open()返回的文件对象只在with代码块内可用 为什么? 因为with块结束后IO关闭, 文件无法访问
    contents = file_object.read(); # 读取文件全部内容 在到达文件末尾时返回一个空字符串
    print(contents); 
    pass;

#file_object.read(); # ValueError: I/O operation on closed file.

### 逐行读取文件内容
with open(filename) as file_object:
    for line in file_object:
        print(line); # 文件中每行末尾有一个换行符, Windows下是\r\n, 所以读取文件print的时候也会将换行符打印
        #print(line.rstrip()); # 这样子就不会有换行符了 他会删除空格, 换行符, 回车符, 制表符
        pass;
    pass;

with open(filename) as file_object:
    lines = file_object.readlines(); # 返回list[str]
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
print(pi_string[ : 10]); # 对str切片, 只得到其小数点后八位


### 写入文件
filename = 'programming.txt';

with open(filename, 'w') as file_object: # 若文件不存在 则首先创建文件
    file_object.write('I Love Programming.....\r\n'); # 只能将字符串写入文件
    print('successful write');
    pass;


