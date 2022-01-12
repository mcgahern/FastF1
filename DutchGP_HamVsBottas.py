import fastf1 as ff1
from fastf1 import plotting
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure

# Setup Plotting
plotting.setup_mpl()

# Enable the cache
#ff1.Cache.enable_cache('cache')

# Load Sesssion Data
race = ff1.get_session(2021,'Zandvoort', 'R')

# Collect all race laps
laps = race.load_laps(with_telemetry=True)

# Get laps of Bot and Ham
laps_bot = laps.pick_driver('BOT')
laps_ham = laps.pick_driver('HAM')

# Extract the fastest laps
fastest_bot = laps_bot.pick_fastest()
fastest_ham = laps_ham.pick_fastest()

# Get telemetry from fastest laps
telemetry_bot = fastest_bot.get_car_data().add_distance()
telemetry_ham = fastest_ham.get_car_data().add_distance()

fig,ax = plt.subplots(3)
fig.suptitle("Fastest Race Lap Telemetry Comparision")

ax[0].plot(telemetry_bot['Distance'], telemetry_bot['Speed'], label='BOT')
ax[0].plot(telemetry_ham['Distance'], telemetry_ham['Speed'], label='HAM')
ax[0].set(ylabel='Speed')
ax[0].legend(loc='lower right')

ax[1].plot(telemetry_bot['Distance'], telemetry_bot['Throttle'], label='BOT')
ax[1].plot(telemetry_ham['Distance'], telemetry_ham['Throttle'], label='HAM')
ax[1].set(ylabel='Throttle')

ax[2].plot(telemetry_bot['Distance'], telemetry_bot['Brake'], label='BOT')
ax[2].plot(telemetry_ham['Distance'], telemetry_ham['Brake'], label='HAM')
ax[2].set(ylabel='Brake Points')

# Hide x labels and tick labels for top plots and y ticks for right plots
for a in ax.flat:
    a.label_outer()

plt.show()
