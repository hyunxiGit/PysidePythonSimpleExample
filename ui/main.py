# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Mon Dec 30 10:11:20 2019
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.my_treeWidget = QtWidgets.QTreeWidget(self.frame_3)
        self.my_treeWidget.setObjectName("my_treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.my_treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.my_treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.my_treeWidget)
        self.gridLayout_2.addWidget(self.my_treeWidget, 0, 0, 1, 1)
        self.horizontalLayout_4.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.my_listWidget = QtWidgets.QListWidget(self.frame_2)
        self.my_listWidget.setObjectName("my_listWidget")
        self.gridLayout.addWidget(self.my_listWidget, 0, 0, 1, 1)
        self.horizontalLayout_4.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.le_name = QtWidgets.QLineEdit(self.frame)
        self.le_name.setObjectName("le_name")
        self.horizontalLayout_2.addWidget(self.le_name)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.cb_gender = QtWidgets.QComboBox(self.frame)
        self.cb_gender.setObjectName("cb_gender")
        self.cb_gender.addItem("")
        self.cb_gender.addItem("")
        self.horizontalLayout.addWidget(self.cb_gender)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.le_photo = QtWidgets.QLineEdit(self.frame)
        self.le_photo.setObjectName("le_photo")
        self.horizontalLayout_5.addWidget(self.le_photo)
        self.tb_photo = QtWidgets.QToolButton(self.frame)
        self.tb_photo.setObjectName("tb_photo")
        self.horizontalLayout_5.addWidget(self.tb_photo)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.pb_submitt = QtWidgets.QPushButton(self.frame)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/fist.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_submitt.setIcon(icon)
        self.pb_submitt.setObjectName("pb_submitt")
        self.horizontalLayout_3.addWidget(self.pb_submitt)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 400, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_4.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionReload = QtWidgets.QAction(MainWindow)
        self.actionReload.setObjectName("actionReload")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuMenu.addAction(self.actionReload)
        self.menuMenu.addAction(self.actionExit)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.my_treeWidget.headerItem().setText(0, QtWidgets.QApplication.translate("MainWindow", "New Column", None, -1))
        self.my_treeWidget.headerItem().setText(1, QtWidgets.QApplication.translate("MainWindow", "New Column", None, -1))
        self.my_treeWidget.headerItem().setText(2, QtWidgets.QApplication.translate("MainWindow", "New Column", None, -1))
        __sortingEnabled = self.my_treeWidget.isSortingEnabled()
        self.my_treeWidget.setSortingEnabled(False)
        self.my_treeWidget.topLevelItem(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "New Item", None, -1))
        self.my_treeWidget.topLevelItem(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "New Item", None, -1))
        self.my_treeWidget.topLevelItem(2).setText(0, QtWidgets.QApplication.translate("MainWindow", "New Item", None, -1))
        self.my_treeWidget.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "name", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "gender", None, -1))
        self.cb_gender.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "male", None, -1))
        self.cb_gender.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "female", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "photo", None, -1))
        self.tb_photo.setText(QtWidgets.QApplication.translate("MainWindow", "...", None, -1))
        self.pb_submitt.setText(QtWidgets.QApplication.translate("MainWindow", "PushButton", None, -1))
        self.menuMenu.setTitle(QtWidgets.QApplication.translate("MainWindow", "menu", None, -1))
        self.actionReload.setText(QtWidgets.QApplication.translate("MainWindow", "reload", None, -1))
        self.actionExit.setText(QtWidgets.QApplication.translate("MainWindow", "exit", None, -1))

from ui import icons_rc
