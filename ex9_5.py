# 문제 9.5 직경AB, CD 두께 구하기
# 재료역학 교재 p.409 문제 풀이

sigma_x, sigma_y, sigma_z = 12000, 0, 20000
E ,neu = 10**7, 1/3
t, d = 3/4, 9

e_x = sigma_x / E - neu*sigma_y/E - neu*sigma_z/E
e_y = sigma_y / E - neu*sigma_x/E - neu*sigma_z/E
e_z = sigma_z / E - neu*sigma_x/E - neu*sigma_y/E

# print(e_x, e_y, e_z)
print('e_x={:.3f}x10^-3 \ne_y={:.3f}x10^-3 \ne_z={:.3f}x10^-3 '.format(e_x*1000, e_y*1000, e_z*1000))

d_ba = e_x * d
d_cd = e_z * d
print('d_ba = {:.1f}x10^-3 in.   \nd_cd = {:.1f}x10^-3 in.'.format(d_ba*1000, d_cd*1000))

d_t = e_y * t 
print('d_t = {:.3f}x10^-3 in.'.format(d_t*1000))
