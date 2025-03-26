# %%
import numpy as np
import matplotlib.pyplot as plt

# %%

lst = list(range(1000))
print(lst)
lst[0]='hello'
print(lst)

# %%

x=np.arange(0,1000,3)
print(x)
# %%
som=np.sum(x)
print(som)
# %%
x2=np.array(
    [
        [1,2,3,4,5],
        [6,7,8,9,10]
    ],dtype=np.float16
)
print(x2)
print(type(x2))
print(x2.dtype)
print(x2.shape)
# %%
x3=100*np.random.rand(4,5)
print(x3)

# %%
x4=np.array(range(1000)).reshape(10,10,10)
x4

# %%
x=np.linspace(0,2*np.pi,1000)
print(x.shape)
#print(x)
#iteration sur les elemets de x afficher un par un
y=np.empty(x.shape,x.dtype)
# i=0
# for item in x:
#     y[i]=item**2
#     i+=1
#y=x**-2*np.sin(x)
y=np.exp(-x**2/10)*np.sin(15*x)
print(y[:10]) #Extration d'un tranch d'un vector
plt.plot(x,y)
plt.show()
# %%
x=np.arange(0,100)
x[0]
x[10:20]
x[:20]
x[90:]
x[1:100:2]
x[100:1:-2]
# %%
x[0]=10010
x[0:5]=np.array([-3,6,-7,9,5])
print(x)
# %%
print(x[-1])
# %%
print(x[-4:-1:1])
# %%
print(x[-1:-4:-1])
# %%
x=np.random.randint(100,size=10)
np.random.shuffle(x) 
print(x)
# %%
#m1=np.zeros((4,4)) #matrice tous elems 0
#m1=np.ones((4,4)) #matrice tous elems 1
m1=np.identity(10)
m1
# %%
a=np.random.randint(20,50)*np.random.rand(10,10)
y=np.random.randint(20,50)*np.random.rand(10)
print(y)
inv_a=np.linalg.inv(a)
m1
print(np.dot(m1,inv_a))
x=np.dot(inv_a,y)
print(x)
#verification
err1=np.sum((np.dot(a,x)-y)**2)
x2=np.linalg.solve(a,y)
err2=np.sum((np.dot(a,x2)-y)**2)
print('err1=',err1,'err2=',err2)
# %%
x=np.arange(100)
np.random.shuffle(x)
print(x)
#%%
print(x)
print(np.where(x%5==0))
#y=np.extract(x%3==0,x)
y=np.extract(x%3!=0,x)
print(y)
# %%
