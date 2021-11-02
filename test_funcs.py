
import numpy as np
from funcs import windspeed_mean

wind_sp=np.array((1,2,3,4,5))

print(windspeed_mean(wind_sp,2)[1])