# For now it's intended to be partially hardcoded
import csv
import os
from collections import defaultdict
from pathlib import Path
import json

from datetime import datetime

class DatesConverter():

    def strToDate(self, date):
        #print("strToDate ", date)
        return datetime.strptime(date, "%d-%m-%Y")

    def dateToStr(self, date):
        return date.strftime("%d-%m-%y")


class dashboardValue():
    def __init__(self, value = None , commentary=""):
        self.value = value
        self.commenary = commentary

    def setValue(self, value):
        self.value = value

    def setCommentary(self, commentary):
        self.commentary = commentary

class Parameter():
    def __init__(self, csvfile = None, jsonfile = None):
        self.csvfile = csvfile
        self.description = {}
        # TODO - change to something else
        self.paramLog = defaultdict(dashboardValue)

    def readCsv(self):
        with open(self.csvfile) as csvfile:
            reader = csv.reader(csvfile)
            for line in reader:
                # COMMENTARY COULD BE EMPTY
                date, value, commentary = line
                date = DatesConverter().strToDate(date)
                value = float(value)
                self.paramLog[date].setValue(value)
                if commentary:
                    self.paramLog[date].setCommentary(commentary)

    def getIterableValues(self):
        return (_.value for _ in self.paramLog.values())

    def getMax(self):
        return max(self.getIterableValues())

    def getMin(self):
        return min(self.getIterableValues())

    def getAverage(sefl):
        return sum(self.getItrableValues())/len(self.paramLog)

    def setCsv(self, csvfile):
        self.csvfile = csvfile
        self.readCsv()

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
        self.mapDailyTrackables()

    def getDailyTrackablesList(self):
        return list(self.trackablesMapping.values())

    def getByKey(self, key):
        return self.trackablesMapping[key]

    def getWithKeys(self):
        # return list((_.key, _.value) for _ in self.trackablesMapping.items())
        return self.trackablesMapping.items()
