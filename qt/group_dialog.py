# Created By: Virgil Dupras
# Created On: 2011-07-22
# Copyright 2011 Hardcoded Software (http://www.hardcoded.net)
# 
# This software is licensed under the "BSD" License as described in the "LICENSE" file, 
# which should be included with this package. The terms are also available at 
# http://www.hardcoded.net/licenses/bsd_license

from PyQt4.QtGui import QDialog, QVBoxLayout, QHBoxLayout, QPushButton

from core.gui.group_dialog import GroupDialog as GroupDialogModel
from .page_repr import PageRepresentation

class GroupDialog(QDialog):
    def __init__(self, parent, app):
        QDialog.__init__(self, parent)
        self.app = app
        self.model = GroupDialogModel(app.model)
        self._setupUi()
        
        self.model.set_children([self.pageReprView.model])
        
        self.previousPageButton.clicked.connect(self.model.prev_page)
        self.nextPageButton.clicked.connect(self.model.next_page)
    
    def _setupUi(self):
        self.setWindowTitle("Grouping Dialog")
        self.resize(600, 600)
        self.mainLayout = QVBoxLayout(self)
        self.pageReprView = PageRepresentation()
        self.mainLayout.addWidget(self.pageReprView)
        self.buttonLayout = QHBoxLayout()
        self.previousPageButton = QPushButton("<<")
        self.buttonLayout.addWidget(self.previousPageButton)
        self.nextPageButton = QPushButton(">>")
        self.buttonLayout.addWidget(self.nextPageButton)
        self.mainLayout.addLayout(self.buttonLayout)
    
