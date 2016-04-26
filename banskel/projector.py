#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, absolute_import, division

# -----------------------------------------------------------------------------
# imports
# -----------------------------------------------------------------------------
from PyQt4.QtCore import QThread
from PyQt4.QtCore import pyqtSignal

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
    pass

# -----------------------------------------------------------------------------
def reproject(x, y, source_srid, dest_srid):

    sp = Proj("+init=EPSG:{}".format(source_srid))
    dp = Proj("+init=EPSG:{}".format(dest_srid))

    # TODO
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
                print(x, y)
                res = reproject(x, y, 4326, 3857) # srid pour la france
                print (res)
            except ValueError:
                continue


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
    def __init__(self):
        super(Projector, self).__init__()
        self.filename = ""

    def filename(self, filename):
        self.filename = filename

    def run(self):
        # TODO
        pass
