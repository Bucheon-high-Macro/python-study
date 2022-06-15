icecream = {'탱크보이':'1200', '폴라포':'1200', '빵빠레':'1800', '월드콘':'1500', '메로나':'1000'}
sell = {'탱크보이':'10', '폴라포':'20', '빵빠레':'17', '월드콘':'9', '메로나':'37'}
a = int(icecream.get('탱크보이'))*int(sell.get('탱크보이'))
b = int(icecream.get('폴라포'))*int(sell.get('폴라포'))
c = int(icecream.get('빵빠레'))*int(sell.get('빵빠레'))
d = int(icecream.get('월드콘'))*int(sell.get('월드콘'))
e = int(icecream.get('메로나'))*int(sell.get('메로나'))
print(a+b+c+d+e)
