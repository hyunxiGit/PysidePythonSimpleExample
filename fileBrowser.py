from PySide2 import QtWidgets
from ui import main
from ui import icons_rc

import sys

# window class,
class MyQtApp(main.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        # set up the window
        super(MyQtApp, self).__init__()
        self.setupUi(self)

        self.showMaximized()
        #set window title
        self.setWindowTitle('My QT app')
        self.populate_lineEdit()
        self.populate_tree_widget()
        self.populate_list_widget()


    def populate_lineEdit(self):
        #button click callback
        self.pb_submitt.clicked.connect(self.pb_submitt_clicked)
        self.tb_photo.clicked.connect(self.tb_photo_clicked)
        #button set text
        self.pb_submitt.setText("submitt!")

    def populate_tree_widget(self):
        self.my_treeWidget.setHeaderLabels(['ID','NAME','COLOR'])
        self.my_treeWidget.clear()
        x = ['apple', 'banana', 'orange']

        for i,e in enumerate(x):
            items = QtWidgets.QTreeWidgetItem(self.my_treeWidget)
            items.setText(0, str(i))
            items.setText(1, e)

    def populate_list_widget(self):
        self.my_listWidget.clear()
        list = ['a','b','c']
        self.my_listWidget.addItems(list)

    def tb_photo_clicked(self):
        photoPath,ext = QtWidgets.QFileDialog.getOpenFileName(self,'select photo')
        if photoPath:
            self.le_photo.setText(photoPath)

    def pb_submitt_clicked(self):
        name = self.le_name.text()
        if not self.le_name.text():
            QtWidgets.QMessageBox.about(self,'Name required!','Please fill in name!')
            return
        gender = self.cb_gender.currentText()
        print (gender)

#run window code
if __name__=='__main__':
    # Qapplication , can have only 1 in the program
    app = QtWidgets.QApplication()
    at_app = MyQtApp()
    at_app.show()
    app.exec_()


