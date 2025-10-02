#Vetületi együtthatók számítása

a = 6377397.155  #a IUGG 1967 ellipszoid nagytengelye
1:a = 1/299.152813  #IUGG 1967 ellipszoid lapultsága
k = 1,003016135133
n = 1,000751489594
R = 6378512,966
phi0 = 47°26'21,13721"
#(phi0 = 47,4392047806°)
lambda0 = 19°3'07,57"
#(lambda0 = 19,05210369°)

#Bessel 1841 ellipszoidról Gauss gömbre

s= k * tan(pi/4 - phi/2)**n / ((1 - e * sin(phi)) / (1 + e * sin(phi)))**((n*e)/2)
phi' = 2 * arctan(s) - (pi/2)
lambda' = n * (lambda - lambda0)

#Gauss gömbről sztereografikus vetületre
q = cos(phi_) * cos (phi0) * cos(lamda_)
z = sin(phi_) * sin(phi0)
d = 1 + q + z
x = 2 * R * (q-z) / d
y = 2 * R * cos(phi_) * sin(lamda_) / d
