# For now it's intended to be partially hardcoded
import csv
import os
from collections import defaultdict
from pathlib import Path
import json

class Parameter():
    def __init__(self, csvfile = None, jsonfile = None):
        self.csvfile = csvfile
        self.description = {}

    def setCsv(self, csvfile):
        self.csvfile = csvfile

    def setJson(self, jsonfile):
        with open(jsonfile) as descriptorFile:
            self.description = json.load(descriptorFile)

    def __repr__(self):
        return self.description["name"]


class DataModel():
    def __init__(self, baseFolder):
        self.baseFolder = baseFolder
        self.trackablesMapping = None
        self.initDashboardData()

    # By hardcoded i mean this
    # probably would be better to process it with json
    def listDailyTrackables(self):
        trackablesDir = os.path.join(self.baseFolder, "daily_trackables")
        return list(os.path.join(trackablesDir, _) for _ in os.listdir(trackablesDir))

    def mapDailyTrackables(self):
        dailyTrackables = self.listDailyTrackables()
        print("daily Trackables... ", dailyTrackables)
        self.trackablesMapping = defaultdict(Parameter)

        for trackable in dailyTrackables:
            pathWrapped = Path(trackable)

            print(pathWrapped.suffix)
            if pathWrapped.suffix == ".json":
                self.trackablesMapping[pathWrapped.stem].setJson(trackable)
            if pathWrapped.suffix == ".csv":
                self.trackablesMapping[pathWrapped.stem].setCsv(trackable)

    def initDashboardData(self):
        # TODO Log something
        self.mapDailyTrackables()

    def getDailyTrackablesList(self):
        return list(self.trackablesMapping.values())


