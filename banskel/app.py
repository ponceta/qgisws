#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, absolute_import, division

import sys
from PyQt4 import QtGui
from  browser import Browser

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    browser = Browser()
    browser.show()
    sys.exit(app.exec_())
