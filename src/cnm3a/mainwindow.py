import os
from qtpyvcp.widgets.form_widgets.main_window import VCPMainWindow
from PyQt5.QtWidgets import QStatusBar, QLabel
from qtpyvcp.actions.program_actions import load, run
from qtpyvcp.utilities.info import Info


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

