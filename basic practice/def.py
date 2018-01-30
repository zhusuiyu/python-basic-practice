# 1、空函数
    # pass用于占位,让程序能正常执行
def empty():
    pass

# 2、参数检查
    # 内置函数会自动检查参数类型是否错误并抛出，而自定义函数不会，所以要进行参数检查
    # 数据类型检查使用isinstance()
def my_abs(x):
    if not isinstance(x,(float,int)):
        # 抛出异常:错误的参数类型
        raise TypeError('bad operand type')
    if x > 0:
        return x
    else:
        return -x

print(my_abs(12))
# print(my_abs('12'))

# 3、返回多个值(实际返回的是tuple)
import math
def move(x,y,step,angel=0):
    nx=x+step*math.cos(angel)
    ny=y+step*math.sin(angel)
    # 实际返回的是一个tuple,可省略括号(nx,ny)    
    return nx,ny
    # 解构赋值
x,y=move(100,60,20,math.pi/3)
print('x is %s,y is %s' %(x,y))
    # 实际返回的是一个tuple,可省略括号
print(move(100,60,20,math.pi/3))

# practice1:
    # 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：ax2 + bx + c = 0的两个解。
def quadratic(a,b,c):
    d=b*b-4*a*c
    if a==0:
        return -c/b
    elif d==0:
        return -(b/2*a)
    elif d>0:
        nx=-b+math.sqrt(d)/(2*a)
        ny=-b-math.sqrt(d)/(2*a)
        return nx,ny
    else:
        return "无解"
quaResult=quadratic(1,2,4)
print(quaResult)