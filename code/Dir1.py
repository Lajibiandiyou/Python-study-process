# coding=gbk

alien_0 = {'color': 'green',
          'points': 5
          }; # ������ʽ
print(alien_0); # ��ӡ���ֵ�
print(alien_0['color']); # ����Key 'color' �����ֵ��е�Value 'green'
print(alien_0['points']); # ����Key 'points' �����ֵ��е�Value 5
print(len(alien_0));# �ֵ��С(����ֵ�Ը���)


new_points = alien_0['points'];
print('You earn ' + str(new_points) + ' points');

alien_0['x_position'] = 0;
alien_0['y_position'] = 25; # ��Ӽ�ֵ�� ����ֵ��м�ֵ�Ե�˳������˳��һ����? ��һ��
# �����ֵ���һ���̶�Ӧ�Ź�ϣ�㷨, ��Key����Hash%TableSize���ҵ�Value, ����print�������������
print(alien_0);


alien_empty = {};
alien_empty['color'] = 'green';
alien_empty['points'] = 5;
print(alien_empty); # �ȴ������ֵ�, ֮�����������Key, Value

alien_empty['color'] = 'red';
alien_empty['points'] = 10; # �޸��ֵ��е�ֵ, ��ʵ�����һ��ԭ��
# �ȶ�Key��Hash%TableSize֮��, �������Ϊ��, ������Ӳ���, �����Ϊ��������Hash��ͻ����, 
# ��ʱ�ж�����Key�Ƿ����, ����ȵĻ���Ȼ����Ӳ���, ��ȵĻ����޸Ĳ���

del alien_empty['color']; # ɾ���ֵ��е�KV(KeyValue)��

person = {
    'first_name': 'Andy',
    'last_name': 'Loos',
    'age': 24,
    };

for key, value in person.items(): # items()���ؿɱ�����KVԪ������ Ԫ���ǲ��ɸ��ĵ�
    print('Key = ' + str(key));
    print('Value = ' + str(value));

for entry in person.items():
    print('Key = ' + str(entry[0]) + ', Value = '+ str(entry[1]));

for i in person.items():
    print('Ԫ��Ϊ: ', i);

for key in person.keys(): # д�� in person Ҳ����, ��Ϊ �ֵ����Ĭ�ϱ���Key ������һ���б�
    print('Key = ' + key + ', Value = ' + str(person[key])); # ͨ��Key����Value

for key in sorted(person.keys()): # ���ֵ��Key����
    print('Key = ' + key);

for value in person.values(): # �����ֵ�Value ����п��ܻ����ظ�
    print('Value = ' + str(value));

for value in set(person.values()): # �����ӾͲ������ظ���
    print('Value = ' + str(value));


#### �ֵ��б�
fruit_1 = {'category': 'apple', 'price': 5};
fruit_2 = {'category': 'banana', 'price': 11};
fruit_3 = {'category': 'watermelon', 'price': 1};
fruits = [fruit_1, fruit_2, fruit_3];
print(fruits)

#### �б��ֵ�
pizza = {
    'curst': 'thick',
    'toppings': ['mushroom', 'cheese'],
    };
print(pizza);
#### �ֵ��ֵ�
users = {
    'james' : {
        'first': 'lay',
        'last': 'james'
        },
    'cody': {
        'first': 'cody',
        'last': 'Q'
        }
    };
print(users)