# coding=gbk
import json

### JSON
numbers = [2, 3, 5, 7, 11, 13];

filename = 'numbers.json';
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj); # �洢��Ϣ ����1, Ҫ�洢������, ����2, �洢���ݵ��ļ�����
    pass;

with open(filename, 'r') as f_obj:
    numbers_from_file = json.load(f_obj); # ������Ϣ ����1, �洢���ݵ��ļ�����
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