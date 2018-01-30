# dict(dictionary)
newDict = {'fruit': 'apple', 'animal': 'dog', 'number': 10}
# 读值
print(newDict['animal'])
# 改值
newDict['number'] = 20
print(newDict)
# 判断key是否存在的两种方法
# 1：in,返回boolean
print('fruit' in newDict)
print('dog' in newDict)
# 2:get(),有则返回值。无则返回none,可指定返回值
print(newDict.get('number'))
print(newDict.get('Number'))
print(newDict.get('Number', -1))
# 删除key pop()
newDict.pop('animal')
print(newDict)

# dict内部存放的顺序和key放入的顺序是没有关系的。
# 和list比较，dict有以下几个特点：
#     查找和插入的速度极快，不会随着key的增加而变慢；
#     需要占用大量的内存，内存浪费多。
# 而list相反：
#     查找和插入的时间随着元素的增加而增加；
#     占用空间小，浪费内存很少。
# 所以，dict是用空间来换取时间的一种方法。


# set :一组key的集合，不存储value，无重复key，无序
# 新建 set(list)
newSet = set([3, 2, 1, 1, 2, 3])
print('after set: ' + str(newSet))
# 添加 add
newSet.add('5')
print('after add: ' + str(newSet))
# 删除 remove
newSet.remove('5')
print('after remove: ' + str(newSet))
# 可做交集并集
set1 = set([3, 4, 5, '6', '7', '8'])
set2 = set([3, 4, 0, '5', '7', '9'])
print('交集：'+str(set1 & set2))
print('并集：'+str(set1 | set2))

# 议不可变对象
# dict和set里的key必须是不可变对象，否则无法查找
a=['a','c','b']
print(a.sort())
print(a)
# 可变对象调用对象方法不返回新对象，改变自身
b='abc'
newB=b.replace('c','C')
print(b)
print(newB)
# 不可变对象调用对象方法返回一个新对象，不改变自身，保证了不可变对象本身永远是不可变的
