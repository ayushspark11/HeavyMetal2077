import json
import model.mechModel.mech as mechmodel
import os

savedConfigPath = "savedConfigs/"
try:
    os.mkdir("savedConfigs/")
    print("savedConfig directory created")
except FileExistsError as error:
    print("savedConfig directory exists")

def loadMechConfig(configId):
    #pull json from memory and convert into mech model
    config = open(savedConfigPath + configId+".json")
    try:
        newMech = mechmodel.Mech()
        newMech.loadFromJson(config)
    finally:
        config.close()

def saveMechConfig(configId, mech):
    #convert mech model into json format and save to memory
    json_string = json.dumps(getDictHierarchy(mech))
    save_path = os.path.join(savedConfigPath, configId+".json")
    mechConfigFile = open(save_path, "w+")
    mechConfigFile.write(json_string)

def getDictHierarchy(item):
    dict_op = item.__dict__
    for item in dict_op:
        if hasattr(dict_op[item], '__dict__'):
            dict_op[item] = getDictHierarchy(dict_op[item])
    return dict_op
    