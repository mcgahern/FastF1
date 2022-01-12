import fastf1
from fastf1.livetiming.data import LiveTimingData



livedata = LiveTimingData('saved_data.txt')
session = fastf1.get_session(2021, 'testing', 1)
session.load_laps(with_telemetry=True, livedata=livedata)