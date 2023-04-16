# coding=gbk
from audioop import reverse


names = ['James', 'Cody', 'Chris', 'Booker'];
print('init names: ');
print(names);
print('names[0]=' + names[0])
print('names[-1]=' + names[-1]) #索引为负则返回从后往前数的元素

names.append('Paul');
print('after append Paul');
print(names);
names.insert(1, 'Andy');
print('after insert Andy at index 1');
print(names);

del names[0];
print('after del index 0 ')
print(names);

poped_name = names.pop(); # 可以有参数, 即删除特定索引的元素
print('pop the last one')
print('poped name =' + poped_name);
print(names);

names.remove('Cody'); #若元素不存在则报错
print('remove Cody')
print(names);

print('顺序排序')
names.sort();
print(names);
print('逆序排序')
names.sort(reverse = True);
print(names);
print('反转names')
names.reverse();
print(names);
print('列表长度 = ' + str(len(names)));


print('遍历names')
for name in names:
    print(name.title());
    
    print('Great!');# 在循环中, 只要有缩进, 就认为这个语句属于循环, 即使中间有空行,所以执行多次
print('end of loop');# 这里没有空行, 但是没有缩进了, 所以执行一次