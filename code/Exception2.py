# coding=gbk
import json

### JSON
numbers = [2, 3, 5, 7, 11, 13];

filename = 'numbers.json';
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj); # 存储信息 参数1, 要存储的数据, 参数2, 存储数据的文件对象
    pass;

with open(filename, 'r') as f_obj:
    numbers_from_file = json.load(f_obj); # 加载信息 参数1, 存储数据的文件对象
    pass;

print(numbers_from_file)

def get_stored_username():
    filename = 'username.json';
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj);
            pass;
        pass;
    except FileNotFoundError:
        return None;
    else:
        return username;

   

def greet_user():
    username = get_stored_username();
    if username == None:
        username = input('Type your name: ');
        filename = 'username.json';
        with open(filename, 'w') as f:
            json.dump(username, f);
            pass;
        pass;
    else:
        print('Welcome back, ' + username);