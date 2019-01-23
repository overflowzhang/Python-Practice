#Pickle

import pickle

# The name of the file where wo will store the object
shoplistfile = 'shoplist.data'
#The list of things to buy
shoplist = ['apple','mango','carrot']

#Write to the file
f = open(shoplistfile,'wb')
#Dump the object to a file
pickle.dump(shoplist,f)     ###这一过程被称为封装 Pickling
f.close()

#Destroy the shoplist variable
del shoplist

#Read back from the storage
f = open(shoplistfile,'rb')
# Load the object from the file
storedlist = pickle.load(f)      ###这一过程被称为拆封 Unpickling
print(storedlist)