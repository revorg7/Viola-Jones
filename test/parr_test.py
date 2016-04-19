#http://www.admin-magazine.com/HPC/Articles/Parallel-Python-with-Joblib
import numpy as np
import pickle
bdt = pickle.load( open( "D:/boosting/bdt.pkl", "rb" ) )
#bdt = pickle.load( open( "D:/boosting/my-model.pkl", "rb" ) )

from Calc_harr import Calc_harr
hfs= Calc_harr()
hf = []
for feature_type in hfs:
    hf+=feature_type
del hfs

from evalharr1 import EvaluateHaar

def myfunc(lis):
#    return np.sum(X,axis=1)
#    print X.shape
#    return bdt.predict(X)

    vals = []
    for f in hf:
        vals.append(EvaluateHaar(lis,f))
    dat = np.array(vals)
    return bdt.predict(dat.T)
