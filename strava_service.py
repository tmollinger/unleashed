import os
from abc import abstractmethod
import pandas as pd

from config import DATA_DIR


class DataService:
    @abstractmethod
    def get_activities_data(self):
        pass


class LocalDataService(DataService):
    def __init__(self, athlete_name):
        self.name = athlete_name

    def get_activities_data(self):
        athlete_dir = os.path.join(DATA_DIR, self.name)
        activities_file = os.path.join(athlete_dir, 'activities.csv')
        return pd.read_csv(activities_file)


if __name__ == '__main__':
    athlete = 'theo'
    df = LocalDataService(athlete).get_activities_data()
    data = df[['date', 'type', 'distance']]
    data.date = pd.to_datetime(data.date)
    data = data.set_index('date')
    print(data.groupby('type').resample('M').distance.sum() > 5000)
