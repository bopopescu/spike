from __future__ import print_function
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/chiron/bitbuck/draft/Visu/util/fticrResol.ui'
#
# Created: Tue Jul 29 13:59:51 2014
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from ..Pyside_PyQt4 import*
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(950, 750)
        MainWindow.setCursor(QtCore.Qt.ArrowCursor)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(770, 10, 141, 41))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_7 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_2.addWidget(self.label_8, 0, 1, 1, 1)
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 251, 211))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.layoutD = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.layoutD.setObjectName(_fromUtf8("layoutD"))
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(270, 0, 491, 51))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_5 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_2.addWidget(self.label_5)
        self.label_6 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_2.addWidget(self.label_6)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 240, 141, 22))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 220, 151, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 300, 211, 16))
        self.label_9.setText(_fromUtf8(""))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(10, 640, 121, 20))
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 470, 251, 161))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.zoom = QtGui.QWidget()
        self.zoom.setObjectName(_fromUtf8("zoom"))
        self.lineEdit_2 = QtGui.QLineEdit(self.zoom)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 60, 171, 21))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_10 = QtGui.QLabel(self.zoom)
        self.label_10.setGeometry(QtCore.QRect(10, 40, 191, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.pushButton_7 = QtGui.QPushButton(self.zoom)
        self.pushButton_7.setGeometry(QtCore.QRect(20, 90, 111, 21))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.pushButton_13 = QtGui.QPushButton(self.zoom)
        self.pushButton_13.setGeometry(QtCore.QRect(140, 90, 91, 21))
        self.pushButton_13.setObjectName(_fromUtf8("pushButton_13"))
        self.label_2 = QtGui.QLabel(self.zoom)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 73, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.tabWidget.addTab(self.zoom, _fromUtf8(""))
        self.profile_peaks = QtGui.QWidget()
        self.profile_peaks.setObjectName(_fromUtf8("profile_peaks"))
        self.label_13 = QtGui.QLabel(self.profile_peaks)
        self.label_13.setGeometry(QtCore.QRect(0, 10, 201, 20))
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.lineEdit_4 = QtGui.QLineEdit(self.profile_peaks)
        self.lineEdit_4.setGeometry(QtCore.QRect(30, 40, 171, 22))
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.pushButton_12 = QtGui.QPushButton(self.profile_peaks)
        self.pushButton_12.setGeometry(QtCore.QRect(150, 90, 61, 41))
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        self.pushButton_9 = QtGui.QPushButton(self.profile_peaks)
        self.pushButton_9.setGeometry(QtCore.QRect(110, 70, 91, 21))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.tabWidget.addTab(self.profile_peaks, _fromUtf8(""))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(180, 350, 91, 41))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.label_12 = QtGui.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(350, 500, 121, 21))
        self.label_12.setText(_fromUtf8(""))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.tabWidget_2 = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 270, 171, 141))
        self.tabWidget_2.setObjectName(_fromUtf8("tabWidget_2"))
        self.Navigation = QtGui.QWidget()
        self.Navigation.setEnabled(True)
        self.Navigation.setAccessibleName(_fromUtf8(""))
        self.Navigation.setObjectName(_fromUtf8("Navigation"))
        self.pushButton = QtGui.QPushButton(self.Navigation)
        self.pushButton.setGeometry(QtCore.QRect(30, 80, 61, 21))
        self.pushButton.setText(_fromUtf8(""))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.Navigation)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 80, 61, 21))
        self.pushButton_2.setMaximumSize(QtCore.QSize(115, 32))
        self.pushButton_2.setText(_fromUtf8(""))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.Navigation)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 0, 91, 81))
        self.pushButton_3.setText(_fromUtf8(""))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.tabWidget_2.addTab(self.Navigation, _fromUtf8("Navigation"))
        self.Tools = QtGui.QWidget()
        self.Tools.setObjectName(_fromUtf8("Tools"))
        self.pushButton_10 = QtGui.QPushButton(self.Tools)
        self.pushButton_10.setGeometry(QtCore.QRect(0, 0, 51, 51))
        self.pushButton_10.setText(_fromUtf8(""))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.pushButton_11 = QtGui.QPushButton(self.Tools)
        self.pushButton_11.setGeometry(QtCore.QRect(50, 0, 51, 51))
        self.pushButton_11.setText(_fromUtf8(""))
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.pushButton_14 = QtGui.QPushButton(self.Tools)
        self.pushButton_14.setGeometry(QtCore.QRect(0, 50, 51, 51))
        self.pushButton_14.setText(_fromUtf8(""))
        self.pushButton_14.setObjectName(_fromUtf8("pushButton_14"))
        self.pushButton_15 = QtGui.QPushButton(self.Tools)
        self.pushButton_15.setGeometry(QtCore.QRect(110, 0, 51, 51))
        self.pushButton_15.setText(_fromUtf8(""))
        self.pushButton_15.setObjectName(_fromUtf8("pushButton_15"))
        self.label_14 = QtGui.QLabel(self.Tools)
        self.label_14.setGeometry(QtCore.QRect(60, 80, 91, 17))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.tabWidget_2.addTab(self.Tools, _fromUtf8(""))
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(160, 230, 41, 31))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(210, 230, 41, 31))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 640, 111, 16))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_15 = QtGui.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(20, 660, 31, 16))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_16 = QtGui.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(40, 660, 131, 16))
        self.label_16.setText(_fromUtf8(""))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_17 = QtGui.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(20, 680, 31, 21))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.label_18 = QtGui.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(40, 680, 131, 16))
        self.label_18.setText(_fromUtf8(""))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(80, 420, 71, 21))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 420, 51, 19))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pushButton_8 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(160, 420, 91, 21))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 950, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Data Visualization", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Size:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "taille", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "File :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "fich", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "save view", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", "highest intensity: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "zoom coord (llx, lly, urx, ury):", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_7.setText(QtGui.QApplication.translate("MainWindow", "make zoom 3D", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_13.setText(QtGui.QApplication.translate("MainWindow", "make zoom", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "resolution:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.zoom), QtGui.QApplication.translate("MainWindow", "zoom", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("MainWindow", "profile coord (llx, lly, urx, ury):", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_12.setText(QtGui.QApplication.translate("MainWindow", "peaks", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_9.setText(QtGui.QApplication.translate("MainWindow", "make profile", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.profile_peaks), QtGui.QApplication.translate("MainWindow", "profile & peaks", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("MainWindow", "pt or m/z", None, QtGui.QApplication.UnicodeUTF8))
        self.Navigation.setToolTip(QtGui.QApplication.translate("MainWindow", "Navigation\n"
"\n"
"", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setToolTip(QtGui.QApplication.translate("MainWindow", "Zoom back", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setToolTip(QtGui.QApplication.translate("MainWindow", "Zoom forward", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setToolTip(QtGui.QApplication.translate("MainWindow", "original view", None, QtGui.QApplication.UnicodeUTF8))
        self.Tools.setToolTip(QtGui.QApplication.translate("MainWindow", "Tools\n"
"", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("MainWindow", "selected tool", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Tools), QtGui.QApplication.translate("MainWindow", "Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("MainWindow", "png", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_6.setText(QtGui.QApplication.translate("MainWindow", "pdf", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("MainWindow", "x:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("MainWindow", "y:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "scale :", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_8.setText(QtGui.QApplication.translate("MainWindow", "change scale", None, QtGui.QApplication.UnicodeUTF8))

