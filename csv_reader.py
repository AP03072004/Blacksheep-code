
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('step_microliter_ramp_profile.csv')
plt.plot(data.time_ms, data.target)
plt.legend(['target'])
plt.xlabel('Time in seconds')
plt.ylabel('Flow rate in picoliter/second')
plt.show()



