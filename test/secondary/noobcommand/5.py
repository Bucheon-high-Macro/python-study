toy1 = {'레고':'23', '기차':'50', '로봇':'27', '지구본':'15', '시계':'57'}
toy2 = {'레고':'12000', '기차':'15000', '로봇':'9000', '지구본':'13500', '시계':'10000'}

a = int(toy1.get('레고'))*int(toy2.get('레고'))
b = int(toy1.get('기차'))*int(toy2.get('기차'))
c = int(toy1.get('로봇'))*int(toy2.get('로봇'))
d = int(toy1.get('지구본'))*int(toy2.get('지구본'))
e = int(toy1.get('시계'))*int(toy2.get('시계'))
print(a+b+c+d+e)
