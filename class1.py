

import random
result = 1 + 2
print("计算1 + 2的结果")
print("计算结果为："+str(result))

x_rate = 0.65
total_dollars = 200
fee = 2
total_pounds = (total_dollars - fee) * x_rate
total_dollars = (total_pounds - 100) / x_rate - fee
test = int(total_dollars)
print("total_dollars="+str(test))

a = random.randint(1,254)
b = random.randint(0,255)
c = random.randint(0,255)
d = random.randint(1,254)
print(str(a)+"."+str(b)+"."+str(c)+"."+str(d))