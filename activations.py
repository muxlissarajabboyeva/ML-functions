import math

def sigmoid(z):
   natija=1/(1+math.exp(-z))
   return natija
print(sigmoid(3.26))

def softmax(qiymatlar):
   max_qiymat=qiymatlar[0]
   for qiymat in qiymatlar:
      if qiymat>max_qiymat:
         max_qiymat=qiymat

   exp_qiymatlar=[]
   for qiymat in qiymatlar:
      exp_qiymatlar.append(math.exp(qiymat-max_qiymat))

   summa=0
   for qiymat in exp_qiymatlar:
      summa+=qiymat

   natija=[]
   for qiymat in exp_qiymatlar:
      natija.append(round(qiymat/summa,2))
      

   return natija

print(softmax([1000,1001,1002]))



def oddiy_orta_qiymat(x):
   surat=0
   maxraj=0
   for i in range(len(x)):
      surat+=x[i]
      maxraj+=1

   return surat/maxraj

x=[2,3,4]
print(oddiy_orta_qiymat(x))



def vaznli_orta_qiymat(x,w):
   surat=0
   maxraj=0
   for i in range(len(x)):
      surat+=x[i]*w[i]
      maxraj+=w[i]
   return surat/maxraj

x = [80, 90, 70]
w = [2, 3, 1]

print(vaznli_orta_qiymat(x, w))


def guruh_orta_qiymat(x,f):
   x_orta=0
   f_sum=0
   for i in range(len(x)):
     guruh_markaz=(x[i][0]+x[i][1])/2
     x_orta+=guruh_markaz*f[i]
     f_sum+=f[i]

   return x_orta/f_sum

x=[(10,20),(20,30),(30,40)]
f=[2,5,3]

print(guruh_orta_qiymat(x,f))

def orta_geometrik(x):
   g=1
   n=0
   for i in range(len(x)):
      g*=x[i]
      n+=1
   return g**(1/n)

x=[25]
print(orta_geometrik(x))

def garmonik_ortacha(x):
   surat=0
   maxraj=0

   for i in range(len(x)):
      maxraj+=1/(x[i])
      surat+=1
   return round(surat/maxraj,2)
print(garmonik_ortacha([60,40]))

def kvadratik_ortacha(x):
   surat=0
   maxraj=0
   for i in range(len(x)):
      surat+=(x[i]**2)
      maxraj+=1

   return math.sqrt(surat/maxraj)

print(kvadratik_ortacha([3,4,2]))

def dispersiya(d):
   orta_qiy=0
   n=0
   summ=0
   for i in range(len(d)):
      summ+=d[i]
      n+=1

   orta_qiy=summ/n

   summ=0
   for i in range(len(d)):
      summ+=(d[i]-orta_qiy)**2

   return summ/n

print(dispersiya([1,2,4,6,7]))

def Hosila(x,h):
   f=((x+h)**2-(x**2))/h
   return f
print(Hosila(3,0.1))

def Gradient_Descent(w_eski, x, y, alpha=0.00001):
    bashorat = w_eski * x

    gradient = (bashorat - y) * x

    w_yangi = w_eski - alpha * gradient

    return w_yangi


w = 1
x = 100
y = 200

for i in range(100):
    w = Gradient_Descent(w, x, y)
    print(f"{i+1}-qadam: w = {w}")
   





      


   

   
      
   
      

