import math 

# 재료역학 10주
# 예제 9.9 (p.406)

G = 90*1000

# Step 1
# 전단변형률(gamma_xy) 구하기

gamma_xy = math.tan(0.04/2)    # 0.020
print('gamma_xy = ', gamma_xy)

# Step 2
# 수펑력 구하기

tau_xy = G * gamma_xy   # 1800
# print('tau_xy = ', tau_xy)

A = 8*2.5
p = tau_xy * A    # 36 kips

print('수평력 P = {:.0f} kips'.format(p/1000))
