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
#for item in x:
#   print(item)
# %%
