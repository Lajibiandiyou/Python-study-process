
#coding=gbk

for value in range(1, 20, 4):
    print(value);

numbers = list(range(1, 6));
print(numbers);

even_numbers = list(range(2, 11, 2));
print(even_numbers);

odd_numbers = list(range(1, 11, 2));
print(odd_numbers);

#统计计算
print(min(odd_numbers));
print(max(odd_numbers));
print(sum(odd_numbers));

squares = [value ** 2 for value in range(1, 11)]; # 列表解析, 将for循环和创建新元素整合在一起
print(squares);

print(squares[-3:-2]);

for square in squares[:4]:
    print(square);

print(squares);

# 复制列表
squares_copy_depth = squares[:
                            ]; # 深拷贝, 即将列表中所有元素重新赋值
                            #给新列表, 二者的id不相同, 且二者的元素id也不相同
squares_copy_shallow = squares; # 浅拷贝, 即将列表的地址赋给新列表, 二者id相同, 且其中元素id也相同
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