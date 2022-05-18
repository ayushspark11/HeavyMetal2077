APPNAME = "Heavy Metal 2077"
#from model.mechModel.mech import Mech
import model.mechModel.mech as mechmodel
import service.mechSheetController as msc
import model.frontend.window as fe #needs to be imported to cause the UI to showup


#TODO:
#request windows permission: EXTREMELY IMPORTANT (request local storage access)
#load local config files
#open main window
#load main window components
#populate main window components
#load editor screen
#load from config: list of components
#save modified mech config to memory
#generate pdf based on config from memory or from editor
msc.loadMechConfig("testid")

# Git Got I actually did something

