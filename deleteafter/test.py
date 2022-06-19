ch = 4**2020+2**2017-15
ocn=2
cif = []
while ch:
    cif.append(ch%ocn)
    ch//=ocn
print(cif.count(1))