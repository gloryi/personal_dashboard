import os

# TODO - Migrate to database
# or create proxy undependent from
# storage type

class DataTypes:
    PROD = "__PROD"
    TEST = "__TEST"

testFolder = os.path.join(os.getcwd(),"test_data")
prodFolder = os.path.join(os.getcwd(),"prod_data")

dataType = DataTypes.TEST

dataFolder = testFolder if dataType == DataTypes.TEST else prodFolder

