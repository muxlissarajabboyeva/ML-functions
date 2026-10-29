
class TextRank:
    def __init__(self,matn):
        self.matn=matn

    def divide_gap(self):
        gaplar=self.matn.split(".")
        natija=[]

        for gap in gaplar:
            gap=gap.strip()

            if gap:
                natija.append(gap)

        return natija 

    def similarity(self,gap1,gap2):
        sozlar1=set(gap1.lower().replace(","," ").split())
        sozlar2=set(gap2.lower().replace(","," ").split())
        umumiy=0
        umumiy_sozlar=[]

        for soz in sozlar1:
            if soz in sozlar2:
                umumiy_sozlar.append(soz)
                umumiy+=1

        return umumiy_sozlar

    def qirra_vazni(self,gap1,gap2):
        umumiy_sozlar=self.similarity(gap1,gap2)
        return len(umumiy_sozlar)

    def vazn_matrix(self):
        gaplar=self.divide_gap()
        n=len(gaplar)
        matrix=[]

        for i in range(n):
            qator=[]
            for j in range(n):
                if i==j:
                    qator.append(0)
                else:
                    vazn=self.qirra_vazni(gaplar[i],gaplar[j])
                    qator.append(vazn)
            matrix.append(qator)
        return matrix

    def output_vazn_sum(self,gap_idx,matrix):
        return sum(matrix[gap_idx])

    def umumiy_ball(self,damping=0.85,iterations=10):
        matrix=self.vazn_matrix()
        n=len(matrix)
        if n==0:
            return []
        scores=[0/n]*n 

        for _ in range(iterations):
            new_score=[(1-damping)/n]*n
            for i in range(n):
                for j in range(n):
                    if i==j:
                        continue
                    vazn=matrix[j][i]
                    vazn_sum=self.output_vazn_sum(j,matrix)
                    if vazn_sum>0:
                        new_score[i]+=(damping*scores[j]*vazn/vazn_sum)
            scores=new_score
        return scores

    def sort_ball(self):
        gaplar=self.divide_gap()
        scores=self.umumiy_ball()
        natija=[]

        for i in range(len(gaplar)):
            natija.append((gaplar[i],scores[i]))
        natija.sort(key=lambda element:element[1],reverse=True)
        return natija


    def compare_all(self,):
        gaplar=self.divide_gap()

        for i in range(len(gaplar)):
            for j in range(i+1,len(gaplar)):
                natija=self.similarity(gaplar[i],gaplar[j])
                print(f"{i+1}-gap va {j+1}-gap:{natija}")

   




matn="""
Qiziq,odam baxtiyor paytida hammani baxtiyor deb o'ylaydi.

Odamzot o'zini judayam baxtiyor his etsa,xudbin bo'lib qoladi.

Odam har doim baxtiyor bo'lishni xohlaydi.

Har doim xudbin odam o'zini yomon his qiladi.
"""

textrank = TextRank(matn)

textrank.compare_all()

print("\nTextRank algoritmi:")

for gap, ball in textrank.sort_ball():
    print(f"{ball:.4f} - {gap}")