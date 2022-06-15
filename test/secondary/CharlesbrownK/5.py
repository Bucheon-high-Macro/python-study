toy = {"레고":'12000', '기차':'15000', '로봇':'9000', '지구본':'13500', '시계':'10000'}
lego = int(toy["레고"])
train = int(toy["기차"])
robot = int(toy["로봇"])
globe = int(toy["지구본"])
watch = int(toy["시계"])

sell = {"레고":23, '기차':50, '로봇':27, '지구본':15, '시계':57}
sell_lego = int(sell["레고"])
sell_train = int(sell["기차"])
sell_robot = int(sell["로봇"])
sell_globe = int(sell["지구본"])
sell_watch = int(sell["시계"])

revenue = lego * sell_lego + train * sell_train + robot * sell_robot + globe * sell_globe + watch * sell_watch
print(revenue)
