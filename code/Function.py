# coding=gbk


### �����ṹ. 
### �ĵ��ַ��� ��ʲô
### �в�/�޲�/�з���ֵ/�޷���ֵ

### λ��ʵ�� 
def get_pet(type, name):
    """�õ�������Ϣ"""
    print('type: ' + type + ', name: ' + name);
get_pet('Dog', 'Los'); # ����λ��Ҫ�ͺ��������λ����ͬ
### �ؼ���ʵ��
get_pet(type = 'Cat', name = 'AA'); # ��ʱ�����λ�þ�������, ��Ϊ�βκ�ʵ���Ѿ��໥����
get_pet(name = 'Cat', type = 'AA'); 
#get_pet(name = 'Cat', name = 'AA'); # ��Ȼ����, repeat argument
#get_pet(name = 'Cat'); # ��Ȼ����, required argument

### ����Ĭ��ֵ
### �����ò���Ĭ��ֵʱ, ���β��б�����Ҫ���г�û��Ĭ��ֵ���β�, 
### ���г���Ĭ��ֵ���β�, ��֤Python�ܹ���ȷ�������
def get_color(color = 'RED'): # ���ò���Ĭ��ֵ
    print('The Color is ' + color);

get_color(); # ��дʵ��, ��colorΪ'RED'
get_color('GREEN');# д��ʵ��, ��colorΪʵ��'GREEN'

### �б���ֵ�ʵ��

### ���з���ֵ�ĺ��� �Ƕ������ֵ����ô��?
def get_name(name, middle = ''):
    return middle + name.title();

print(get_name('ssss'))

### �����ֵ�
def build_person(first_name, last_name, age = -1):
    person = {'first': first_name, 'last': last_name};
    if age >= 0:
        person['age'] = age;
    return person;

print(build_person('Python', 'C++', -222));

### �����б� 
friends = ['luc', 'eee', 'ddd', 'abc'];
def greet_users(users):
    for user in users:
        print('Greeting, ' + user.title() + '!!!'); # ���Զ��б���б���, Ҳ�����޸���
        user = 'new'; # �޸Ĳ��˵�, ��Ϊfor each���õ������б�Ԫ�صĸ���, ������ԭ�����б�Ԫ��

greet_users(friends);
print(friends);

### �����뽫��Ϊ�������б��޸�ʱ �����ڴ������ʱ���б�Ŀ�������, ��
greet_users(friends[:]); # ��Ƭ, �������б�ĸ���(���)

### ����������ʵ��
def make_pizza(*toppings): # ��topping��ΪԪ�鴫�뺯�� * ��ʾ����һ����Ϊtoppings��Ԫ��
    print(toppings); # Ԫ�鲻���޸�, �κ��޸�, ɾ��, ���Ԫ�ز�����������һ����Ԫ��(id ����)
### Ȼ��, ����������ʵ��֮���Ǹ����ں��������б�����, ����֪�������Ķ�Ӧ��ϵ��
### Python��ƥ��λ��ʵ�κ͹ؼ���ʵ��, ֮�����µ�ʵ�ζ��ռ������һ���β���

make_pizza('A');
make_pizza('C', 'A', 'D');

arr = (1 ,'d', 'ss');
print(id(arr));
print(id(arr + (1, 'AA')))

def get_info(name, **info):
    profile = {};
    profile['name'] = name.title();
    for k, v in info.items():
        profile[k] = v;
    return profile;

print(get_info('cody', address = 'Tree', Tel = '123456')); # ����ǧ������ 'address' = 'Tree'
# ��Ϊ 'address' ��һ���ַ���, ���ܶ��ַ�����ֵ




