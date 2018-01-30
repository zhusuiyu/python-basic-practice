# list
# 定义一个列表
fruitList = ["banana", "orange", "apple", "mango"]
print(fruitList)
# 获取列表长度
lenght = len(fruitList)
print("length is %d" % lenght)
# 访问列表内元素
print("second node is %s" % fruitList[1])
# 列表末尾追加元素  append
fruitList.append("xigua")
print(fruitList)
# 把元素插入到指定位置 insert
fruitList.insert(2,"huolongguo")
print(fruitList)
# 删除末尾元素pop(),删除指定位置pop(index)
fruitList.pop(-2)
print(fruitList)


# tuple :元祖，不可变(即指向不可变),只读,定义的时候必须确定下来,哪怕是空元祖
animalTuple=('dog','cat','chicken')
print('animalTuple is '+str(animalTuple))
# 如果只有一个元素，要加逗号
onlyTuple=(1,)
print('onlyTuple is '+ str(onlyTuple))
# 可变情况：里面包含引用数据类型
canChangeTuple=(1,2,[3,4])
canChangeTuple[2][0]=5
canChangeTuple[2][1]=6
print('canChangeTuple now is '+str(canChangeTuple))
