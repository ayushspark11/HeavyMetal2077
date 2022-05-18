import json
import model.mechModel.mech as mechmodel

def loadMechConfig(configId):
    print("test " + configId)
    #pull json from memory and convert into mech model

def saveMechConfig(configId, mech):
    #convert mech model into json format and save to memory
    json_string = json.dumps(mech.asDict())
    #print(json_string)