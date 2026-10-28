import math

class TextVektor:
    def __init__(self, fayllar):
        self.fayllar = fayllar
        self.sozlar = fayllar.split()

    def TF(self, soz):
        soz_soni = self.sozlar.count(soz)
        jami_sozlar = len(self.sozlar)

        if jami_sozlar == 0:
            return 0

        return soz_soni / jami_sozlar

    def IDF(self, soz, fayllar):
        jami_fayllar = len(fayllar)
        soz_bor_fayllar = 0

        for fayl in fayllar:
            sozlar = fayl.split()

            if soz in sozlar:
                soz_bor_fayllar += 1

        if jami_fayllar == 0 or soz_bor_fayllar == 0:
            return 0

        return math.log(jami_fayllar / soz_bor_fayllar)

    def TF_IDF(self, soz, fayllar):
        tf = self.TF(soz)
        idf = self.IDF(soz, fayllar)

        return tf * idf

    def cos_similarity(self,fayl1,fayl2):
        A=TextVektor(fayl1)
        B=TextVektor(fayl2)
        sozlar = list(set(A.sozlar) | set(B.sozlar))
        A_vektor = [A.TF_IDF(soz, [fayl1, fayl2]) for soz in sozlar]
        B_vektor = [B.TF_IDF(soz, [fayl1, fayl2]) for soz in sozlar]
        AB=sum(a*b for a,b in zip(A_vektor,B_vektor))
        len_A=math.sqrt(sum(a**2 for a in A_vektor))
        len_B=math.sqrt(sum(b**2 for b in B_vektor))
        if len_A==0 or len_B==0:
            return 0
        return AB/(len_A*len_B)



fayl1 = """
Mahallamizga yangi maktab qurishni taklif qilaman.
"""

fayl2 = """
Mahallamizga yangi bog‘ qurishni taklif qilaman.
"""

fayllar = [fayl1, fayl2]

v = TextVektor(fayl1)

print(v.sozlar)

for soz in dict.fromkeys(v.sozlar):
    tf = v.TF(soz)
    idf = v.IDF(soz, fayllar)
    tf_idf = v.TF_IDF(soz, fayllar)
    cos_sim = v.cos_similarity(fayl1, fayl2)

    print(f"{soz} TF: {tf:.4f} IDF: {idf:.4f} TF-IDF: {tf_idf:.4f} Cos-Sim: {cos_sim:.4f}")
