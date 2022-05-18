import json
import model.mechModel.mech as mechmodel

def loadMechConfig(configId):
    print("test " + configId)
    #pull json from memory and convert into mech model

def saveMechConfig(configId, mech):
    #convert mech model into json format and save to memory
    json_string = json.dumps(getDictHierarchy(mech))

def getDictHierarchy(item):
    dict_op = item.__dict__
    for item in dict_op:
        if hasattr(dict_op[item], '__dict__'):
            dict_op[item] = getDictHierarchy(dict_op[item])
    return dict_op
    