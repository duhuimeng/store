name1='上衣'
price1=150
size1='均码'
colour1='白色'
num1=15
unit1='件'

name2='裤子'
price2=149
size2='均码'
colour2='灰色'
num2=15
unit2='件'

name3='衬衣'
price3=199
size3='均码'
colour3='白色'
num3=15
unit3='件'

name4='西服'
price4=499
size4='均码'
colour4='黑色'
num4=20
unit4='身'

print('------------------欢迎来到衣服专卖店------------------------')
print('名称       价格       尺码       颜色        数量        单位')
print('--------------------------------------------------------')
print(name1,'     ',price1,'     ',size1,'     ',colour1,'       ',num1,'       ',unit1)
print(name2,'     ',price2,'     ',size2,'     ',colour2,'       ',num2,'       ',unit2)
print(name3,'     ',price3,'     ',size3,'     ',colour3,'       ',num3,'       ',unit3)
print(name4,'     ',price4,'     ',size4,'     ',colour4,'       ',num4,'       ',unit4)
print('--------------------------------------------------------')
print('总金额:',price1*num1+price2*num2+price3*num3+price4*num4,'￥')