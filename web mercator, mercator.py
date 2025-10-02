#Web Mercator vetületi rendszer
#Web Mercator vetület
#Gömbi koordinátákból vetületi koordináták számítása.
y1 = R * lambda_
x1 = 1/2 * R * ln((1 + sin(phi)) / (1 - sin(phi)))

#Vetületi koordinátákból gömbi koordináták számítása.
lamda_ = y / R
phi = (pi/2) - 2 * arctan(exp(-x / R))

# Mercator vetület
y2 = R * lambda_
x2 = R * ln(tan(pi/4 + phi/2))
#Vetületi koordinátákból gömbi koordináták.
lambda_ = y / R
phi = 2 * arctan(exp(x / R)) - (pi / 2)
#Ellipszoidi koordinátákból vetületi koordináták.
y3 = a * lambda_
x3 = a * ln(tan(pi/4 + phi/2)) - (e/2) * ln((1 + e * sin(phi)) / (1 - e * sin(phi)))

#Vetületi koordinátákból ellipszoidi koordináták.
lambda_ = y / a
#phi iteratív számítása
phi1 = e**(x/a)
phin+1 = 2 * arctan(phi1 * ((1 + e * sin(phin)) / (1 - e * sin(phin)))**(e/2)) - (pi/2)
