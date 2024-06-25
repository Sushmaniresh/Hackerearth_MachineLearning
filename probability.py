P_MB = float(input())
P_AB = float(input())
P_R = float(input())

#print(P_MB,P_AB,P_R)

c = P_MB * (1-P_AB)
d = P_AB * (1-P_MB)
e = c+d
r = P_R*e
print("{:.6f}".format(r))