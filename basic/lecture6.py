#pickle
#save object to file
#pickling, unpickling

import pickle

myDic={'kim':'232-3534','park':'000-333'}
myLst=[24,56,33]
myStr='beautiful weather~~'
f = open('pickle.txt','wb')
pickle.dump(myDic,f)
pickle.dump(myLst,f)
pickle.dump(myStr,f)
f.close()

f = open('pickle.txt','rb')
d1 = pickle.load(f)
d2 = pickle.load(f)
d3 = pickle.load(f)
f.close()

print(d1)
print(d2)
print(d3)