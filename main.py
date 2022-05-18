APPNAME = "Heavy Metal 2077"
#from model.mechModel.mech import Mech
import model.mechModel.mech as mechmodel
import service.mechSheetController as msc
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import *
import sys

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

def saveTestMech():
    testMech = mechmodel.Mech()
    testMech.head.armor = 7

    msc.saveMechConfig("testid", testMech)

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(300, 200, 300, 200)
    win.setWindowTitle("Heavy Metal 2077")

    label = QtWidgets.QLabel(win)
    label.setText("Biggus Dickus")
    label.move(150, 100)

    win.show()
    sys.exit(app.exec())

saveTestMech()
window()