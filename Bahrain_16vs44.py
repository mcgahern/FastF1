import fastf1 as ff1
from fastf1 import plotting
from matplotlib import pyplot as plt

plotting.setup_mpl()

#ff1.Cache.enable_cache('path/to/folder/for/cache')

#Load the race
race = ff1.get_session(2020,'Bahrain Grand Prix', 'R')
laps = race.load_laps()
print(laps.head())
print(laps.columns)


#Create Driver Variables
lec = laps.pick_driver('LEC')
ham = laps.pick_driver('HAM')

#Creating Axis, and Plots
fig, ax = plt.subplots()
ax.plot(lec['LapNumber'], lec['LapTime'], color='red')
ax.plot(ham['LapNumber'], ham['LapTime'], color='cyan')
ax.set_title('Leclers vs Hamilton')
ax.set_xlabel("Lap Number")
ax.set_ylabel("Lap Time")
plt.show()