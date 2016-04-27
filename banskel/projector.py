#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, absolute_import, division

# -----------------------------------------------------------------------------
# imports
# -----------------------------------------------------------------------------
from PyQt4.QtCore import QThread
from PyQt4.QtCore import pyqtSignal
from PyQt4 import QtCore

from pyproj import Proj, transform
import os
import csv

# -----------------------------------------------------------------------------
# functions
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
def count_lines(filename):
    num_lines = 0
    with open(filename,'r') as f:
        num_lines = sum(1 for _ in f)
        #for i,line in enumerate(f):
        #    pass

    print("File {file} contain {nl} lines ".format(file=filename,nl=num_lines))
    return num_lines

# -----------------------------------------------------------------------------
def reproject(x, y, source_srid, dest_srid):

    sp = Proj("+init=EPSG:{}".format(source_srid))
    dp = Proj("+init=EPSG:{}".format(dest_srid))

    x2,y2 = transform(sp, dp, x, y)
    return (x2,y2)


# -----------------------------------------------------------------------------
def transform_csv(filename, separator=','):
    # read x,y and reproject values
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=',')
        for row in csv_reader:
            try:
                x = float(row[-1])
                y = float(row[-2])
                #print(x, y)
                res = reproject(x, y, 4326, 3857) # srid pour la france
                #print (res)
                #progressbar.setValue(current_line)
                yield res
            except ValueError:
                yield None


            #if isinstance(row[-1],float) and isinstance(row[-2], float):
            #    print(row[-1], row[-2])
            #res = reproject(row[-1], row[-2], 4326, 21781)
            #print(res)



# -----------------------------------------------------------------------------
# classes
# -----------------------------------------------------------------------------
class Projector(QThread):
    """
    TODO : declare signals
    """
    signal_in_progress = QtCore.pyqtSignal(int)
    signal_done = QtCore.pyqtSignal()

    def __init__(self,filename = ""):
        super(Projector, self).__init__()
        self._filename = filename


    @property
    def filename(self):
        return self._filename


    @filename.setter
    def filename(self, filename):
        self._filename = filename

    def run(self):

        generator = transform_csv(self.filename)
        for i,l in enumerate(generator, start=1):
            self.signal_in_progress.emit(i)
            #TODO stocker le resultat YES mais ou on le stocke !
            if l is None:
                print("INSIDE Projector.run() no value found at line {l}".format(l=i))
            else:
                print("INSIDE Projector.run()", l)
