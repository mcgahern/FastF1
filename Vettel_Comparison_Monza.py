import fastf1 as ff1
from fastf1 import plotting
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure

# Setup Plotting
plotting.setup_mpl()

# Load Sesssion Data
race_2021 = ff1.get_session(2021,'Monza', 'Q')
race_2020 = ff1.get_session(2020,'Monza', 'Q')
race_2019 = ff1.get_session(2019,'Monza', 'Q')
race_2018 = ff1.get_session(2018,'Monza', 'Q')

# Collect All Race Laps
laps_2021 = race_2021.load_laps(with_telemetry=True)
laps_2020 = race_2020.load_laps(with_telemetry=True)
laps_2019 = race_2019.load_laps(with_telemetry=True)
laps_2018 = race_2018.load_laps(with_telemetry=True)

# Get Vettel Laps for each Year
vet_2021 = laps_2021.pick_driver('VET')
vet_2020 = laps_2020.pick_driver('VET')
vet_2019 = laps_2019.pick_driver('VET')
vet_2018 = laps_2018.pick_driver('VET')

# Extract Fastest Laps
fastest_2021 = vet_2021.pick_fastest()
fastest_2020 = vet_2020.pick_fastest()
fastest_2019 = vet_2019.pick_fastest()
fastest_2018 = vet_2018.pick_fastest()

# Get telemetry from fastest laps
telemetry_2021 = fastest_2021.get_car_data().add_distance()
telemetry_2020 = fastest_2020.get_car_data().add_distance()
telemetry_2019 = fastest_2019.get_car_data().add_distance()
telemetry_2018 = fastest_2018.get_car_data().add_distance()

fig,ax = plt.subplots(3)
fig.suptitle("Fastest Quali Lap Telemetry Comparison")

ax[0].title.set_text("Vettel Fastest Lap each Year ")
ax[0].plot(telemetry_2021['Distance'], telemetry_2021['Speed'], label='2021', color = 'green')
ax[0].plot(telemetry_2020['Distance'], telemetry_2020['Speed'], label='2020', color = 'red')
ax[0].plot(telemetry_2019['Distance'], telemetry_2019['Speed'], label='2019', linestyle='dotted', color='red')
ax[0].plot(telemetry_2018['Distance'], telemetry_2018['Speed'], label='2018', linestyle='dashed', color='red')
ax[0].legend(loc='lower right')
ax[0].set(ylabel='Speed')


ax[1].plot(telemetry_2021['Distance'], telemetry_2021['Throttle'], label='2021', color = 'green')
ax[1].plot(telemetry_2020['Distance'], telemetry_2020['Throttle'], label='2020', color = 'red')
ax[1].plot(telemetry_2019['Distance'], telemetry_2019['Throttle'], label='2019', linestyle='dotted', color='red')
ax[1].plot(telemetry_2018['Distance'], telemetry_2018['Throttle'], label='2018', linestyle='dashed', color='red')
ax[1].set(ylabel='Throttle')


ax[2].plot(telemetry_2021['Distance'], telemetry_2021['Brake'], label='2021', color = 'green')
ax[2].plot(telemetry_2020['Distance'], telemetry_2020['Brake'], label='2020', color = 'red')
ax[2].plot(telemetry_2019['Distance'], telemetry_2019['Brake'], label='2019', linestyle='dotted', color='red')
ax[2].plot(telemetry_2018['Distance'], telemetry_2018['Brake'], label='2018', linestyle='dashed', color='red')
ax[2].set(ylabel='Braking Pressure')

# Hide x labels and tick labels for top plots and y ticks for right plots
for a in ax.flat:
    a.label_outer()

plt.show()
