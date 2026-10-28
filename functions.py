import math

class Vektor:
    def __init__(self,fayllar):
        self.fayllar=fayllar
        self.sozlar=fayllar.split()

fayl="""
Python juda qiziqarli.
Python dasturlash tili.
Python o'rganamiz.
"""
v = Vektor(fayl)
print(v.sozlar)
for soz in dict.fromkeys(v.sozlar):
    print(soz, v.sozlar.count(soz))