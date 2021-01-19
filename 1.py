name1='砂糖橘子'
price1=3
quality1='A+'
num1=30
unit1='个'

name2='苹果'
price2=2
quality2='A'
num2=25
unit2='个'

name3='榴莲'
price3=25
quality3='A-'
num3=5
unit3='斤'

name4='香蕉'
price4=12
quality4='B+'
num4=14
unit4='斤'

name5='芒果'
price5=21
quality5='B'
num5=10
unit5='斤'

print('------------------------欢迎来到水果商城----------------------------')
print('名称          价格             质量              数量            单位')
print('-----------------------------------------------------------------')
print(name1,'      ',price1,'            ',quality1,'             ',num1,'            ',unit1)
print(name2,'         ',price2,'            ',quality2,'              ',num2,'            ',unit2)
print(name3,'         ',price3,'           ',quality3,'             ',num3,'             ',unit3)
print(name4,'         ',price4,'           ',quality4,'             ',num4,'            ',unit4)
print(name5,'         ',price5,'           ',quality5,'              ',num5,'            ',unit5)
print('-----------------------------------------------------------------')
print('总金额:',price1*num1+price2*num2+price3*num3+price4*num4+price5*num5,'￥')