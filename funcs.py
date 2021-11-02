import numpy as np

def windspeed_mean(ws,cf=1.):
    mn=np.sum(cf*ws)/len(ws)
    n=len(ws)
    return mn,n

#wind_sp=np.array((1,2,3,4,5))

#print(windspeed_mean(wind_sp,2)[1])

