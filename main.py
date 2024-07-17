import sys
import base64
from getplan import *
from PySide6 import QtWidgets, QtGui

class MyWindow(QtWidgets.QWidget):
    def __init__(self, list_items:list = ["--None--"]):
        super().__init__()
        self._temp_list_items = list_items

        # Create the label
        self.label = QtWidgets.QLabel(f"Current: {self._temp_list_items[getActiveStat()]}")
        
        # Create the combobox
        self.combobox = QtWidgets.QComboBox()
        self.combobox.addItems(self._temp_list_items)
        self.combobox.setCurrentIndex(getActiveStat())

        # Create the Process Button
        self.process_button = QtWidgets.QPushButton("Process")
        
        # Create the Exit Button
        self.exit_button = QtWidgets.QPushButton("Exit")

        # Layout the widgets
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.combobox)
        layout.addWidget(self.process_button)
        layout.addWidget(self.exit_button)
        self.setLayout(layout)

        # Connect the button click signal to the process function
        self.process_button.clicked.connect(self.process)
        self.exit_button.clicked.connect(self.exit)
    
    def process(self):
        # Get the selected item text from the combobox
        selected_text = self.combobox.currentText()

        # Store the selected item text in the temp variable
        self._temp_active_stat = int(selected_text[0])
        
        # Change the Plan
        changePlan(id=self._temp_active_stat)
        
        # Change the label
        self.label.setText(f"Current: {self._temp_list_items[getActiveStat()]}")
    
    def exit(self):
        self.close()

# Data Initialization
def getBatteryPlans() -> list:
        batteryPlans = getPlan()
        return batteryPlans # return Format: [(1,guid,plan1),(2,guid,plan2),...]
    
# Data Process and Return the data combox needs
def dataProcess(batteryPlans:list):
    values = [f"{index+1}. {batteryPlans[index][-1]}" for index in range(len(batteryPlans))]
    active_stat = getActiveStat()
    return active_stat, values # values return Format: ["1. plan1","2.plan2","3.plan3",...]

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow(list_items=dataProcess(getBatteryPlans())[-1])
    window.show()
    sys.exit(app.exec())