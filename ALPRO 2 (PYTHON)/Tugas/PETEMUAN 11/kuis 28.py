def liter100km_ke_mpg(liter):
    km_per_mil = 1.609344
    liter_per_galon = 3.785411784
    mil = 100 / km_per_mil
    galon = liter / liter_per_galon
    return mil / galon

def mpg_ke_liter100km(mil):
    km_per_mil = 1.609344
    liter_per_galon = 3.785411784
    km = mil * km_per_mil
    liter = liter_per_galon
    return (liter / km) * 100

print(liter100km_ke_mpg(3.9))
print(liter100km_ke_mpg(7.5))
print(liter100km_ke_mpg(10.))
print(mpg_ke_liter100km(60.3))
print(mpg_ke_liter100km(31.4))
print(mpg_ke_liter100km(23.5))