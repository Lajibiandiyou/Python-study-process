# coding=gbk
from audioop import reverse


names = ['James', 'Cody', 'Chris', 'Booker'];
print('init names: ');
print(names);
print('names[0]=' + names[0])
print('names[-1]=' + names[-1]) #����Ϊ���򷵻شӺ���ǰ����Ԫ��

names.append('Paul');
print('after append Paul');
print(names);
names.insert(1, 'Andy');
print('after insert Andy at index 1');
print(names);

del names[0];
print('after del index 0 ')
print(names);

poped_name = names.pop(); # �����в���, ��ɾ���ض�������Ԫ��
print('pop the last one')
print('poped name =' + poped_name);
print(names);

names.remove('Cody'); #��Ԫ�ز������򱨴�
print('remove Cody')
print(names);

print('˳������')
names.sort();
print(names);
print('��������')
names.sort(reverse = True);
print(names);
print('��תnames')
names.reverse();
print(names);
print('�б��� = ' + str(len(names)));


print('����names')
for name in names:
    print(name.title());
    
    print('Great!');# ��ѭ����, ֻҪ������, ����Ϊ����������ѭ��, ��ʹ�м��п���,����ִ�ж��
print('end of loop');# ����û�п���, ����û��������, ����ִ��һ��