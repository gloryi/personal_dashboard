from Config import dataFolder
from DataModel import DataModel


dataModel = DataModel(dataFolder)

trackablesList = dataModel.getDailyTrackablesList()

# There are valid test data, and it was readed
assert(len(trackablesList) > 0)

# First counter were readed
firstCounter = dataModel.getByKey("counter_1")
assert(firstCounter.getMax() == 32)

# Second counter were readed
secondCounter = dataModel.getByKey("counter_2")
assert(secondCounter.getMin() == 10)

# Data model returning all the counters coorectly
tuples = dataModel.getWithKeys()
assert(len(tuples) == 2)
