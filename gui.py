# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editor.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1072, 824)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_2.addWidget(self.textEdit, 2, 0, 1, 8)
        self.toolFontSize = QtWidgets.QSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolFontSize.sizePolicy().hasHeightForWidth())
        self.toolFontSize.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.toolFontSize.setFont(font)
        self.toolFontSize.setMinimum(1)
        self.toolFontSize.setProperty("value", 12)
        self.toolFontSize.setObjectName("toolFontSize")
        self.gridLayout_2.addWidget(self.toolFontSize, 1, 3, 1, 1)
        self.layoutTabs = QtWidgets.QHBoxLayout()
        self.layoutTabs.setObjectName("layoutTabs")
        self.newDocument = QtWidgets.QPushButton(self.centralwidget)
        self.newDocument.setStyleSheet("QPushButton{                             \n"
"    color: rgb(255, 255, 255);           \n"
"    background-color: rgb(180, 180, 180);\n"
"    border: none;                        \n"
"    padding: 10px 10px;                  \n"
"    font-size: 16px;                     \n"
"    border-radius: 8px;                  \n"
"}                                        \n"
"                                         \n"
"QPushButton:hover{                       \n"
"    background-color: white;             \n"
"    border: 2px solid rgb(180, 180, 180);\n"
"    color: rgb(0, 0, 0);                 \n"
"}                                        ")
        self.newDocument.setObjectName("newDocument")
        self.layoutTabs.addWidget(self.newDocument)
        self.gridLayout_2.addLayout(self.layoutTabs, 0, 0, 1, 8)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 4, 1, 1)
        self.toolFett = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolFett.sizePolicy().hasHeightForWidth())
        self.toolFett.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.toolFett.setFont(font)
        self.toolFett.setObjectName("toolFett")
        self.gridLayout_2.addWidget(self.toolFett, 1, 0, 1, 1)
        self.toolKursiv = QtWidgets.QToolButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setItalic(True)
        self.toolKursiv.setFont(font)
        self.toolKursiv.setObjectName("toolKursiv")
        self.gridLayout_2.addWidget(self.toolKursiv, 1, 1, 1, 1)
        self.toolUnter = QtWidgets.QToolButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setUnderline(True)
        self.toolUnter.setFont(font)
        self.toolUnter.setObjectName("toolUnter")
        self.gridLayout_2.addWidget(self.toolUnter, 1, 2, 1, 1)
        self.toolStandard = QtWidgets.QToolButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.toolStandard.setFont(font)
        self.toolStandard.setObjectName("toolStandard")
        self.gridLayout_2.addWidget(self.toolStandard, 1, 5, 1, 1)
        self.toolTitel = QtWidgets.QToolButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.toolTitel.setFont(font)
        self.toolTitel.setObjectName("toolTitel")
        self.gridLayout_2.addWidget(self.toolTitel, 1, 6, 1, 1)
        self.toolUeberschrift = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolUeberschrift.sizePolicy().hasHeightForWidth())
        self.toolUeberschrift.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.toolUeberschrift.setFont(font)
        self.toolUeberschrift.setObjectName("toolUeberschrift")
        self.gridLayout_2.addWidget(self.toolUeberschrift, 1, 7, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1072, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuDatei = QtWidgets.QMenu(self.menuBar)
        self.menuDatei.setObjectName("menuDatei")
        MainWindow.setMenuBar(self.menuBar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuDatei.addAction(self.actionNew)
        self.menuDatei.addAction(self.actionOpen)
        self.menuDatei.addAction(self.actionSave)
        self.menuDatei.addAction(self.actionClose)
        self.menuDatei.addSeparator()
        self.menuDatei.addAction(self.actionDelete)
        self.menuBar.addAction(self.menuDatei.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.newDocument.setText(_translate("MainWindow", "Neues Dokument"))
        self.toolFett.setText(_translate("MainWindow", "F"))
        self.toolKursiv.setText(_translate("MainWindow", "K"))
        self.toolUnter.setText(_translate("MainWindow", "U"))
        self.toolStandard.setText(_translate("MainWindow", "Standard"))
        self.toolTitel.setText(_translate("MainWindow", "Titel"))
        self.toolUeberschrift.setText(_translate("MainWindow", "Überschrift"))
        self.menuDatei.setTitle(_translate("MainWindow", "Datei"))
        self.actionNew.setText(_translate("MainWindow", "Neue Datei"))
        self.actionDelete.setText(_translate("MainWindow", "Datei löschen"))
        self.actionOpen.setText(_translate("MainWindow", "Datei öffnen"))
        self.actionClose.setText(_translate("MainWindow", "Datei schließen"))
        self.actionSave.setText(_translate("MainWindow", "Datei speichern"))
