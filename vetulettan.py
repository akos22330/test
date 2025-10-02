#Gömbi koordinátákból térbeli koordináták számítása
from math import sin, cos, sqrt, atan2
omega=47.681
lambda_ =16.577
h = 251
R = 6378513
omega_rad = omega * (3.141592653589793 / 180)
lambda_rad = lambda_ * (3.141592653589793 / 180)

X = (R + h) * cos(omega_rad) * cos(lambda_rad)
Y = (R + h) * cos(omega_rad) * sin(lambda_rad)
Z = (R + h) * sin(omega_rad)

#Térbeli koordinákból gömbi koordináták számítása
p = sqrt(X**2 + Y**2)
omega_rad_new = atan2(Z, p)
lambda_rad_new = atan2(Y, X)
omega_new = omega_rad_new * (180 / 3.141592653589793)
lambda_new = lambda_rad_new * (180 / 3.141592653589793)
h_new = sqrt(X**2 + Y**2 + Z**2) - R

print("omega_rad:", omega_rad," lambda_rad:", lambda_rad)
print("Térbeli koordináták: X =", X, "Y =", Y, "Z =", Z)
print("Gömbi koordináták visszaszámolva: p =", p,"  omega =", omega_new, "lambda =lambda", lambda_new, "h =", h_new)
print("A visszaszámolt értékek megegyeznek az eredetiekkel.")