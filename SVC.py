from sig2class import SVC2004 as svc


path = 'C:\\Users\\ASUS\\Documents\\BME\\6. félév\\Önálló laboratórium\\Signature Verification\\SVC 2004\\Task2'

sig = svc(userId= '1', directory = path)
#sig.normalize()

df = sig.signatures['U1S1.TXT']

print(df)

# for user in range(1, 41): itt lehetne egy ciklus ami random bekér 
# genuine meg forged id kat random.sample-el (1,21 és 21,41) aztán eltarolni egy training valtozoba
# miutan pl van 5 genuine es 5 forged, ezeknek az ertekeit lehetne normalizalni
# igy kiveve a ket adatbazis random adatait