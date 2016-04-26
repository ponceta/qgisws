#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, absolute_import, division


# -----------------------------------------------------------------------------
# imports
# -----------------------------------------------------------------------------
# standard
import os
# pyqt
from PyQt4.QtGui import QDialog
from PyQt4.QtGui import QDialogButtonBox
from PyQt4.QtGui import QFileDialog
from PyQt4.QtCore import *
from PyQt4.QtCore import pyqtSignal
from fileinput_ui import Ui_file_browser
from projector import count_lines, transform_csv

# -----------------------------------------------------------------------------
# classes
# -----------------------------------------------------------------------------
class Browser(QDialog, Ui_file_browser):

    # -------------------------------------------------------------------------
    # public methods
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self._filename = ""
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)

        # init attributes
        # TODO

        # custom settings for widgets
        # TODO

        # connect
        # TODO
        #QObject.connect(self, self.pushButtonBrowse, SIGNAL('clicked()'), __browse)
        self.pushButtonBrowse.clicked.connect(self.__browse)


    # -------------------------------------------------------------------------
    @property
    def filename(self):
        return self._filename


    # -------------------------------------------------------------------------
    @filename.setter
    def filename(self, filename):
        if os.path.isfile(filename):
            self._filename = filename
            self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)
            count_lines(filename)
            transform_csv(filename)
        else:
            print("Selected file : {file} is not a file".format(file=filename))



    # -------------------------------------------------------------------------
    # private methods
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    def __in_progress(self, line):
        # TODO
        pass

    # -------------------------------------------------------------------------
    def __compute_done(self):
        # TODO
        pass

    # -------------------------------------------------------------------------
    def __ok(self):
        # TODO
        pass

    # -------------------------------------------------------------------------
    def __browse(self):
        # TODO
        #myFileDialog = QFileDialog(self)
        #myFileDialog.show()
        self.filename = QFileDialog.getOpenFileName(self, 'Choose File', '.',  '*.csv',)
        print(self.filename)
        self.lineEditFileName.setText(self.filename)

