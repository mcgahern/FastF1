import pandas as pd
import requests
import seaborn as sns
import matplotlib.pyplot as plt

# Retrieve Data from the Ergast API
from fastf1.plotting import team_color


def ergast_retrieve(api_endpoint: str):
    url = f'https://ergast.com/api/f1/{api_endpoint}.json'
    response = requests.get(url).json()

    return response['MRData']


# Specify the number of rounds we want in our plot
rounds = 21

# Initiate an empty dataframe to store the data
all_championship_standings = pd.DataFrame()

# We also want to store which driver drives for which team
driver_team_mapping = {}

# Initiate a loop to go through each round of championship
for i in range(1, rounds + 1):
    # Make request to driverStandings endpoint for the current round
    race = ergast_retrieve(f'current/{i}/driverStandings')

    # Get standings from result
    standings = race['StandingsTable']['StandingsLists'][0]['DriverStandings']

    # Initiate a dictionary to store the current rounds' standings in
    current_round = {'round': i}

    # Loop through all the drivers to collect their information
    for j in range(len(standings)):
        driver = standings[j]['Driver']['code']
        position = standings[j]['position']

        # Store the drivers' position
        current_round[driver] = int(position)

        # Create mapping for driver-team to be used in the colouring of the line graph
        driver_team_mapping[driver] = standings[j]['Constructors'][0]['name']

    # Append the current round to our final dataFrame
    all_championship_standings = all_championship_standings.append(current_round, ignore_index=True)

# Set round as the index of the dataFrame
all_championship_standings = all_championship_standings.set_index('round')
# print(all_championship_standings)

# Melt data so it can be used for input of a plot
all_championship_standings_melted = pd.melt(all_championship_standings.reset_index(), ['round'])
# print(all_championship_standings_melted)

# Plotting the data

# Increase the size of the plot
sns.set(rc={'figure.figsize': (11.7, 8.27)})

# Initiate the plot
fig, ax = plt.subplots()

# Set the title of the plot
ax.set_title('2021 Drivers Championship Standings')

# Draw a line for every driver in the data by looping through all the standings
# This is done so we can specify the team colours
for driver in pd.unique(all_championship_standings_melted['variable']):
    sns.lineplot(
        x='round',
        y='value',
        data=all_championship_standings_melted.loc[all_championship_standings_melted['variable']
                                                   == driver],
        color=team_color(driver_team_mapping[driver])
    )

# Invert y-axis to have championship leader (#1) on top
ax.invert_yaxis()

# Set the values that appear on the x and y axes
ax.set_xticks(range(1, rounds))
ax.set_yticks(range(1, 22))

# Set label of the axes
ax.set_xlabel('Round')
ax.set_ylabel('Championship Position')

# Disable the gridlines
ax.grid(False)

# Add the driver name to the lines
for line, name in zip(ax.lines, all_championship_standings.columns.tolist()):
    y = line.get_ydata()[-1]
    x = line.get_xdata()[-1]

    text = ax.annotate(
        name,
        xy=(x + 0.1, y),
        xytext=(0, 0),
        color=line.get_color(),
        xycoords=(
            ax.get_xaxis_transform(),
            ax.get_yaxis_transform()
        ),
        textcoords='offset points'
    )

# Save the plot
plt.show()
