
#coding=gbk

for value in range(1, 20, 4):
    print(value);

numbers = list(range(1, 6));
print(numbers);

even_numbers = list(range(2, 11, 2));
print(even_numbers);

odd_numbers = list(range(1, 11, 2));
print(odd_numbers);

#ͳ�Ƽ���
print(min(odd_numbers));
print(max(odd_numbers));
print(sum(odd_numbers));

squares = [value ** 2 for value in range(1, 11)]; # �б����, ��forѭ���ʹ�����Ԫ��������һ��
print(squares);

print(squares[-3:-2]);

for square in squares[:4]:
    print(square);

print(squares);

# �����б�
squares_copy_depth = squares[:
                            ]; # ���, �����б�������Ԫ�����¸�ֵ
                            #�����б�, ���ߵ�id����ͬ, �Ҷ��ߵ�Ԫ��idҲ����ͬ
squares_copy_shallow = squares; # ǳ����, �����б�ĵ�ַ�������б�, ����id��ͬ, ������Ԫ��idҲ��ͬ
print('origin list')
print(squares);
print('its id is ', id(squares), 'and the first element id of it is ', id(squares[0]));
print('squares_copy_depth list')
print(squares_copy_depth);
print('its id is ', id(squares_copy_depth), 'and the first element id of it is ', id(squares_copy_depth[0]));
print('squares_copy_shallow list')
print(squares_copy_shallow);
print('its id is ', id(squares_copy_shallow), 'and the first element id of it is ', id(squares_copy_shallow[0]));
dimension = [50, 200];
print(dimension);
dimension[0] = 1;
dimension_unchangable = (50, 200);
print(dimension_unchangable);
dimension_unchangable[0] = 5; # error tuple doest support item assignement 
dimension_unchangable = (2, 5);
print(dimension_unchangable);