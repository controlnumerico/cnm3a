import os
from qtpyvcp.widgets.form_widgets.main_window import VCPMainWindow
from PyQt5.QtWidgets import QStatusBar, QLabel
#from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import *

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


from qtpyvcp.actions.program_actions import load, run
from qtpyvcp.actions.machine_actions import max_velocity
from qtpyvcp.utilities.info import Info
from qtpyvcp import hal


# Setup logging
from qtpyvcp.utilities import logger
LOG = logger.getLogger('qtpyvcp.' + __name__)

class MyMainWindow(VCPMainWindow):
    """Main window class for the VCP."""
    def __init__(self, *args, **kwargs):
        super(MyMainWindow, self).__init__(*args, **kwargs)

        self.label = self.findChild(QLabel, "MyStatusBarNewLabel")
        self.edit = self.findChild(QStatusBar, "statusbar")
        self.edit.messageChanged.connect(self.changeText)

        self.btn_loadrun.clicked.connect(self.load_then_run)
        self.btn_set50.clicked.connect(self.abc)
        self.btn_rotate.clicked.connect(self.abcd)


        hal_comp = hal.COMPONENTS['qtpyvcp']

        self._cycle_ready_pin = hal_comp.addPin("cycle_ready.in", "float", "in")
        self._cycle_ready_pin.value = self.isEnabled()
        self._cycle_ready_pin.valueChanged.connect(self.onCycleReadyPinChanged)




    def changeText(self):
        self.label.setText(self.edit.currentMessage())

    # add any custom methods hereeee

    def on_exitAppBtn_clicked(self):
        self.app.quit()

   # add any custom methods here
    def load_then_run(self):
        # now we load the prog
        info = Info()
        nc_files_dir = info.getProgramPrefix()
        path = os.path.expanduser(nc_files_dir)
        load(path + "/axis.ngc")
#        run()



    def onCycleReadyPinChanged(self, value):
            max_velocity.set(value)
            self.pixmap = QPixmap("/home/cnc/.iMG/dial.png")
            self.label_2.setPixmap(self.pixmap.transformed(QTransform().rotate(value),QtCore.Qt.SmoothTransformation)) 


    def abc(self):
        # now we load the prog
        self.actionbutton_3.setStyleSheet('border-color: red')
        self.max_velocity_slider.setStyleSheet('border-color: red')
        max_velocity.set(10)

    def abcd(self):
        # now we load the prog
        angle = 90  # What angle would you like to rotate
        self.pixmap = QPixmap("/home/cnc/.iMG/dial.png")
        self.label_2.setPixmap(self.pixmap.transformed(QTransform().rotate(angle),QtCore.Qt.SmoothTransformation)) 



