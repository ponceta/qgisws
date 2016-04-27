#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
# import des modules PyQt necessaires
from PyQt4.QtGui import QApplication,  QVBoxLayout, QWidget, QPushButton, QLabel
from PyQt4.QtCore import *
# on ne lance les commandes suivantes que si on est dans un script

if __name__ == '__main__':
    # Tous les programmes Qt ont besoin d'une
    # instance de QApplication
    # On passe les arguments de la ligne de commande car Qt
    # sait en interpreter certain
    app = QApplication(sys.argv)
    # On cree un label avec du html
    label = QLabel("<b>Go to Hello World !</b></br><a href='http://ww.google.com'>Google</a>")
    # On cree un bouton avec un texte dessus
    button = QPushButton("&Quit this beautifull app !")
    #QObject.connect(button,SIGNAL("button_click()"),SLOT(quit()))
    # connectons le signal de clic au slot quit() de l'application
    # deprecated : button.connect(button, QtCore.SIGNAL("clicked()"),\
    #    app, QtCore.SLOT("quit()"))
    button.clicked.connect(app.quit)

    layout = QVBoxLayout()
    layout.addWidget(label)
    layout.addWidget(button)

    window = QWidget()
    window.setLayout(layout)
    # on doit explicitement demander l'affichage de la fenetre
    window.show()

    # On lance la boucle evenementielle
    sys.exit(app.exec_())



