# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/main_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1627, 1112)
        MainWindow.setStyleSheet("\n"
"QMainWindow {\n"
"    background-color:#f5f5f5;\n"
"}\n"
"QPushButton, QToolButton, QCommandLinkButton{\n"
"    padding: 0 5px 0 5px;\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #c1c9cf, stop:1 #d2d8dd);\n"
"    border-right-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 #c1c9cf, stop:1 #d2d8dd);\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #c1c9cf, stop:1 #d2d8dd);\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #c1c9cf, stop:1 #d2d8dd);\n"
"    border-width: 2px;\n"
"    border-radius: 8px;\n"
"    color: #616161;\n"
"    font-weight: bold;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #fbfdfd, stop:0.5 #ffffff, stop:1 #fbfdfd);\n"
"}\n"
"QPushButton::default, QToolButton::default, QCommandLinkButton::default{\n"
"    border: 2px solid transparent;\n"
"    color: #FFFFFF;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #84afe5, stop:1 #1168e4);\n"
"}\n"
"QPushButton:hover, QToolButton:hover, QCommandLinkButton:hover{\n"
"    color: #3d3d3d;\n"
"}\n"
"QPushButton:pressed, QToolButton:pressed, QCommandLinkButton:pressed{\n"
"    color: #aeaeae;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #ffffff, stop:0.5 #fbfdfd, stop:1 #ffffff);\n"
"}\n"
"QPushButton:disabled, QToolButton:disabled, QCommandLinkButton:disabled{\n"
"    color: #616161;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #dce7eb, stop:0.5 #e0e8eb, stop:1 #dee7ec);\n"
"}\n"
"QLineEdit, QTextEdit, QPlainTextEdit, QSpinBox, QDoubleSpinBox, QTimeEdit, QDateEdit, QDateTimeEdit {\n"
"    border-width: 2px;\n"
"    border-radius: 8px;\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 #c1c9cf, stop:1 #d2d8dd);\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #c1c9cf, stop:1 #d2d8dd);\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #c1c9cf, stop:1 #d2d8dd);\n"
"    border-left-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 #c1c9cf, stop:1 #d2d8dd);\n"
"    background-color: #f4f4f4;\n"
"    color: #3d3d3d;\n"
"}\n"
"QLineEdit:focus, QTextEdit:focus, QPlainTextEdit:focus, QSpinBox:focus, QDoubleSpinBox:focus, QTimeEdit:focus, QDateEdit:focus, QDateTimeEdit:focus {\n"
"    border-width: 2px;\n"
"    border-radius: 8px;\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 #85b7e3, stop:1 #9ec1db);\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #85b7e3, stop:1 #9ec1db);\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #85b7e3, stop:1 #9ec1db);\n"
"    border-left-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 #85b7e3, stop:1 #9ec1db);\n"
"    background-color: #f4f4f4;\n"
"    color: #3d3d3d;\n"
"}\n"
"QLineEdit:disabled, QTextEdit:disabled, QPlainTextEdit:disabled, QSpinBox:disabled, QDoubleSpinBox:disabled, QTimeEdit:disabled, QDateEdit:disabled, QDateTimeEdit:disabled {\n"
"    color: #b9b9b9;\n"
"}\n"
"QSpinBox::up-button, QDoubleSpinBox::up-button, QTimeEdit::up-button, QDateEdit::up-button, QDateTimeEdit::up-button {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    color: #272727;\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    padding: 3px;\n"
"}\n"
"QSpinBox::down-button, QDoubleSpinBox::down-button, QTimeEdit::down-button, QDateEdit::down-button, QDateTimeEdit::down-button {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: bottom right;\n"
"    width: 15px;\n"
"    color: #272727;\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-bottom-right-radius: 3px;\n"
"    padding: 3px;\n"
"}\n"
"QSpinBox::up-button:pressed, QDoubleSpinBox::up-button:pressed, QTimeEdit::up-button:pressed, QDateEdit::up-button:pressed, QDateTimeEdit::up-button:pressed {\n"
"    color: #aeaeae;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #ffffff, stop:0.5 #fbfdfd, stop:1 #ffffff);\n"
"}\n"
"QSpinBox::down-button:pressed, QDoubleSpinBox::down-button:pressed, QTimeEdit::down-button:pressed, QDateEdit::down-button:pressed, QDateTimeEdit::down-button:pressed {\n"
"    color: #aeaeae;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #ffffff, stop:0.5 #fbfdfd, stop:1 #ffffff);\n"
"}\n"
"QSpinBox::up-button:hover, QDoubleSpinBox::up-button:hover, QTimeEdit::up-button:hover, QDateEdit::up-button:hover, QDateTimeEdit::up-button:hover {\n"
"    color: #FFFFFF;\n"
"    border-top-right-radius: 5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #84afe5, stop:1 #1168e4);\n"
"    \n"
"}\n"
"QSpinBox::down-button:hover, QDoubleSpinBox::down-button:hover, QTimeEdit::down-button:hover, QDateEdit::down-button:hover, QDateTimeEdit::down-button:hover {\n"
"    color: #FFFFFF;\n"
"    border-bottom-right-radius: 5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #84afe5, stop:1 #1168e4);\n"
"}\n"
"QSpinBox::up-arrow, QDoubleSpinBox::up-arrow, QTimeEdit::up-arrow, QDateEdit::up-arrow, QDateTimeEdit::up-arrow {\n"
"    image: url(/usr/share/icons/Adwaita/16x16/actions/go-up-symbolic.symbolic.png);\n"
"}\n"
"QSpinBox::down-arrow, QDoubleSpinBox::down-arrow, QTimeEdit::down-arrow, QDateEdit::down-arrow, QDateTimeEdit::down-arrow {\n"
"    image: url(/usr/share/icons/Adwaita/16x16/actions/go-down-symbolic.symbolic.png);\n"
"}\n"
"QProgressBar {\n"
"    max-height: 8px;\n"
"    text-align: center;\n"
"    font: italic bold 11px;\n"
"    color: #3d3d3d;\n"
"    border: 1px solid transparent;\n"
"    border-radius:4px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #ddd5d5, stop:0.5 #dad3d3, stop:1 #ddd5d5);\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #467dd1, stop:0.5 #3b88fc, stop:1 #467dd1);\n"
"    border-radius: 4px;\n"
"}\n"
"QProgressBar:disabled {\n"
"    color: #616161;\n"
"}\n"
"QProgressBar::chunk:disabled {\n"
"    background-color: #aeaeae;\n"
"}\n"
"QSlider::groove {\n"
"    border: 1px solid #bbbbbb;\n"
"    background-color: #52595d;\n"
"    border-radius: 4px;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    height: 6px;\n"
"}\n"
"QSlider::groove:vertical {\n"
"    width: 6px;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: #ffffff;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    width: 12px;\n"
"    margin: -5px 0;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background: #ffffff;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    height: 12px;\n"
"    margin: 0 -5px;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::add-page, QSlider::sub-page {\n"
"    border: 1px transparent;\n"
"    background-color: #52595d;\n"
"    border-radius: 4px;\n"
"}\n"
"QSlider::add-page:horizontal {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #ddd5d5, stop:0.5 #dad3d3, stop:1 #ddd5d5);\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #467dd1, stop:0.5 #3b88fc, stop:1 #467dd1);\n"
"}\n"
"QSlider::add-page:vertical {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #467dd1, stop:0.5 #3b88fc, stop:1 #467dd1);\n"
"}\n"
"QSlider::sub-page:vertical {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #ddd5d5, stop:0.5 #dad3d3, stop:1 #ddd5d5);\n"
"}\n"
"QSlider::add-page:horizontal:disabled, QSlider::sub-page:horizontal:disabled, QSlider::add-page:vertical:disabled, QSlider::sub-page:vertical:disabled {\n"
"    background: #b9b9b9;\n"
"}\n"
"QComboBox, QFontComboBox {\n"
"    border-width: 2px;\n"
"    border-radius: 8px;\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 #c1c9cf, stop:1 #d2d8dd);\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #c1c9cf, stop:1 #d2d8dd);\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #c1c9cf, stop:1 #d2d8dd);\n"
"    border-left-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 #c1c9cf, stop:1 #d2d8dd);\n"
"    background-color: #f4f4f4;\n"
"    color: #272727;\n"
"    padding-left: 5px;\n"
"}\n"
"QComboBox:editable, QComboBox:!editable, QComboBox::drop-down:editable, QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: #ffff;\n"
"}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    color: #272727;\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: url(/usr/share/icons/Adwaita/16x16/actions/go-down-symbolic.symbolic.png); /*Adawaita icon thene*/\n"
"}\n"
"\n"
"QComboBox::down-arrow:on {\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid darkgray;\n"
"    border-radius: 8px;\n"
"    selection-background-color: #dadada;\n"
"    selection-color: #272727;\n"
"    color: #272727;\n"
"    background: white;\n"
"}\n"
"QLabel, QCheckBox, QRadioButton {\n"
"    color: #272727;\n"
"}\n"
"QCheckBox {\n"
"    padding: 2px;\n"
"}\n"
"QCheckBox:disabled, QRadioButton:disabled {\n"
"    color: #808086;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"    border-radius:4px;\n"
"    border-style:solid;\n"
"    padding-left: 1px;\n"
"    padding-right: 1px;\n"
"    padding-bottom: 1px;\n"
"    padding-top: 1px;\n"
"    border-width:1px;\n"
"    border-color: transparent;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    image: url(/usr/share/icons/Adwaita/16x16/actions/object-select-symbolic.symbolic.png);\n"
"    height: 15px;\n"
"    width: 15px;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-color: #48a5fd;\n"
"    color: #ffffff;\n"
"    border-radius: 3px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #48a5fd, stop:0.5 #329cfb, stop:1 #48a5fd);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    \n"
"    height: 15px;\n"
"    width: 15px;\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-color: #48a5fd;\n"
"    border-radius: 3px;\n"
"    background-color: #fbfdfa;\n"
"}\n"
"QLCDNumber {\n"
"    color: #616161;;\n"
"}\n"
"QMenuBar {\n"
"    background-color: #ececec;\n"
"}\n"
"QMenuBar::item {\n"
"    color: #616161;\n"
"    spacing: 3px;\n"
"    padding: 1px 4px;\n"
"    background-color: #ececec;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"    background-color: #dadada;\n"
"    color: #3d3d3d;\n"
"}\n"
"QMenu {\n"
"    background-color: #ececec;\n"
"}\n"
"QMenu::item:selected {\n"
"    background-color: #dadada;\n"
"    color: #3d3d3d;\n"
"}\n"
"QMenu::item {\n"
"    color: #616161;;\n"
"    background-color: #e0e0e0;\n"
"}\n"
"QTabWidget {\n"
"    color:rgb(0,0,0);\n"
"    background-color:#000000;\n"
"}\n"
"QTabWidget::pane {\n"
"    border-color: #050a0e;\n"
"    background-color: #e0e0e0;\n"
"    border-width: 1px;\n"
"    border-radius: 4px;\n"
"    position: absolute;\n"
"    top: -0.5em;\n"
"    padding-top: 0.5em;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    alignment: center;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border-bottom: 1px solid #c0c0c0;\n"
"    padding: 3px;\n"
"    color: #272727;\n"
"    background-color: #fefefc;\n"
"    margin-left:0px;\n"
"}\n"
"QTabBar::tab:!last {\n"
"    border-right: 1px solid;\n"
"    border-right-color: #c0c0c0;\n"
"    border-bottom-color: #c0c0c0;\n"
"}\n"
"QTabBar::tab:first {\n"
"    border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"}\n"
"QTabBar::tab:last {\n"
"    border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {\n"
"    color: #FFFFFF;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #84afe5, stop:1 #1168e4);\n"
"}\n"
"QRadioButton::indicator {\n"
"    height: 14px;\n"
"    width: 14px;\n"
"    border-style:solid;\n"
"    border-radius:7px;\n"
"    border-width: 1px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    border-color: #48a5fd;\n"
"    background-color: qradialgradient(cx:0.5, cy:0.5, radius:0.4,fx:0.5, fy:0.5, stop:0 #ffffff, stop:0.5 #ffffff, stop:0.6 #48a5fd, stop:1 #48a5fd);\n"
"}\n"
"QRadioButton::indicator:!checked {\n"
"    border-color: #a9b7c6;\n"
"    background-color: #fbfdfa;\n"
"}\n"
"QStatusBar {\n"
"    color:#027f7f;\n"
"}\n"
"\n"
"QDial {\n"
"    background: #16a085;\n"
"}\n"
"\n"
"QToolBox {\n"
"    color: #a9b7c6;\n"
"    background-color: #222b2e;\n"
"}\n"
"QToolBox::tab {\n"
"    color: #a9b7c6;\n"
"    background-color:#222b2e;\n"
"}\n"
"QToolBox::tab:selected {\n"
"    color: #FFFFFF;\n"
"    background-color:#222b2e;\n"
"}\n"
"QScrollArea {\n"
"    color: #FFFFFF;\n"
"    background-color:#222b2e;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    max-height: 10px;\n"
"    border: 1px transparent grey;\n"
"    margin: 0px 20px 0px 20px;\n"
"    background: transparent;\n"
"}\n"
"QScrollBar:vertical {\n"
"    max-width: 10px;\n"
"    border: 1px transparent grey;\n"
"    margin: 20px 0px 20px 0px;\n"
"    background: transparent;\n"
"}\n"
"QScrollBar::handle:vertical, QScrollBar::handle:horizontal {\n"
"    background: #52595d;\n"
"    border-style: transparent;\n"
"    border-radius: 4px;\n"
"    min-height: 25px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover, QScrollBar::handle:vertical:hover {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #467dd1, stop:0.5 #3b88fc, stop:1 #467dd1);\n"
"}\n"
"QScrollBar::add-line, QScrollBar::sub-line {\n"
"    border: 2px transparent grey;\n"
"    border-radius: 4px;\n"
"    subcontrol-origin: margin;\n"
"    background: #b9b9b9;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    width: 20px;\n"
"    subcontrol-position: right;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    height: 20px;\n"
"    subcontrol-position: bottom;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    width: 20px;\n"
"    subcontrol-position: left;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"    height: 20px;\n"
"    subcontrol-position: top;\n"
"}\n"
"QScrollBar::add-line:vertical:pressed, QScrollBar::add-line:horizontal:pressed, QScrollBar::sub-line:horizontal:pressed, QScrollBar::sub-line:vertical:pressed {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #467dd1, stop:0.5 #3b88fc, stop:1 #467dd1);\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal, QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"QScrollBar::up-arrow:vertical {\n"
"    image: url(/usr/share/icons/Adwaita/16x16/actions/go-up-symbolic.symbolic.png);\n"
"}\n"
"QScrollBar::down-arrow:vertical {\n"
"    image: url(/usr/share/icons/Adwaita/16x16/actions/go-down-symbolic.symbolic.png);\n"
"}\n"
"QScrollBar::left-arrow:horizontal {\n"
"    image: url(/usr/share/icons/Adwaita/16x16/actions/go-previous-symbolic.symbolic.png);\n"
"}\n"
"QScrollBar::right-arrow:horizontal {\n"
"    image: url(/usr/share/icons/Adwaita/16x16/actions/go-next-symbolic.symbolic.png);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setMinimumSize(QtCore.QSize(240, 260))
        self.pushButton_8.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_2.addWidget(self.pushButton_8, 5, 5, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 3, 6, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setMinimumSize(QtCore.QSize(240, 260))
        self.pushButton_10.setStyleSheet("background-color: rgb(150, 202, 247);\n"
"\n"
"border-color: rgb(255, 255, 255,0);")
        self.pushButton_10.setText("")
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_2.addWidget(self.pushButton_10, 5, 9, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setMinimumSize(QtCore.QSize(240, 260))
        self.pushButton_13.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.pushButton_13.setText("")
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout_2.addWidget(self.pushButton_13, 7, 5, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setMinimumSize(QtCore.QSize(240, 260))
        self.pushButton_5.setStyleSheet("background-color: rgb(150, 202, 247);\n"
"\n"
"border-color: rgb(255, 255, 255,0);")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_2.addWidget(self.pushButton_5, 3, 9, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 3, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(240, 260))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 3, 5, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem2, 4, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(240, 260))
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 3, 7, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setMinimumSize(QtCore.QSize(240, 260))
        self.pushButton_15.setStyleSheet("background-color: rgb(150, 202, 247);\n"
"\n"
"border-color: rgb(255, 255, 255,0);")
        self.pushButton_15.setText("")
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout_2.addWidget(self.pushButton_15, 7, 9, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10% 10%")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.delete_btn = QtWidgets.QPushButton(self.frame)
        self.delete_btn.setMinimumSize(QtCore.QSize(40, 40))
        self.delete_btn.setMaximumSize(QtCore.QSize(40, 40))
        self.delete_btn.setStyleSheet("*{border-color: rgb(255, 255, 255);\n"
"border-radius:20% 20%;}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 0, 0,.3);\n"
"\n"
"}")
        self.delete_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-delete-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_btn.setIcon(icon)
        self.delete_btn.setIconSize(QtCore.QSize(30, 30))
        self.delete_btn.setObjectName("delete_btn")
        self.gridLayout.addWidget(self.delete_btn, 1, 2, 1, 1)
        self.play_btn = QtWidgets.QPushButton(self.frame)
        self.play_btn.setMinimumSize(QtCore.QSize(40, 40))
        self.play_btn.setMaximumSize(QtCore.QSize(40, 40))
        self.play_btn.setStyleSheet("*{border-color: rgb(255, 255, 255);\n"
"border-radius:20% 20%;}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"\n"
"    background-color: rgb(170, 255, 255);\n"
"}\n"
"")
        self.play_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-play-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play_btn.setIcon(icon1)
        self.play_btn.setIconSize(QtCore.QSize(30, 30))
        self.play_btn.setObjectName("play_btn")
        self.gridLayout.addWidget(self.play_btn, 1, 0, 1, 1)
        self.text_to_talk_lbl = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(13)
        self.text_to_talk_lbl.setFont(font)
        self.text_to_talk_lbl.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.text_to_talk_lbl.setObjectName("text_to_talk_lbl")
        self.gridLayout.addWidget(self.text_to_talk_lbl, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 11)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setMinimumSize(QtCore.QSize(240, 260))
        self.pushButton_6.setStyleSheet("background-color: rgb(150, 202, 247);\n"
"\n"
"border-color: rgb(255, 255, 255,0);")
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_2.addWidget(self.pushButton_6, 5, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem3, 8, 3, 1, 1)
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setMinimumSize(QtCore.QSize(240, 260))
        self.pushButton_1.setStyleSheet("background-color: rgb(150, 202, 247);\n"
"\n"
"border-color: rgb(255, 255, 255,0);")
        self.pushButton_1.setText("")
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout_2.addWidget(self.pushButton_1, 3, 1, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 80))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_2.setStyleSheet("background-color: #38474f;\n"
"border-radius:5% 5%;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.collection_name_lbl = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(31)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.collection_name_lbl.setFont(font)
        self.collection_name_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.collection_name_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.collection_name_lbl.setObjectName("collection_name_lbl")
        self.gridLayout_3.addWidget(self.collection_name_lbl, 0, 2, 1, 1)
        self.back_btn = QtWidgets.QPushButton(self.frame_2)
        self.back_btn.setMinimumSize(QtCore.QSize(30, 0))
        self.back_btn.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.back_btn.setFont(font)
        self.back_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back_btn.setStyleSheet("background-color: rgb(255, 255, 255,0);\n"
"\n"
"border-color: rgb(255, 255, 255,0);")
        self.back_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-back-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_btn.setIcon(icon2)
        self.back_btn.setIconSize(QtCore.QSize(40, 40))
        self.back_btn.setObjectName("back_btn")
        self.gridLayout_3.addWidget(self.back_btn, 0, 0, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_16.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_16.setMaximumSize(QtCore.QSize(70, 70))
        self.pushButton_16.setStyleSheet("background-color: rgb(255, 255, 255,0);\n"
"\n"
"border-color: rgb(255, 255, 255,0);")
        self.pushButton_16.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/7069717.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_16.setIcon(icon3)
        self.pushButton_16.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout_3.addWidget(self.pushButton_16, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 11)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 3, 10, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem5, 2, 3, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem6, 6, 1, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setMinimumSize(QtCore.QSize(240, 260))
        self.pushButton_9.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_2.addWidget(self.pushButton_9, 5, 7, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem7, 3, 2, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem8, 3, 8, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setMinimumSize(QtCore.QSize(240, 260))
        self.pushButton_11.setStyleSheet("background-color: rgb(150, 202, 247);\n"
"\n"
"border-color: rgb(255, 255, 255,0);")
        self.pushButton_11.setText("")
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_2.addWidget(self.pushButton_11, 7, 1, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setMinimumSize(QtCore.QSize(240, 260))
        self.pushButton_7.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_2.addWidget(self.pushButton_7, 5, 3, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setMinimumSize(QtCore.QSize(240, 260))
        self.pushButton_14.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.pushButton_14.setText("")
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout_2.addWidget(self.pushButton_14, 7, 7, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem9, 3, 4, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setMinimumSize(QtCore.QSize(240, 260))
        self.pushButton_12.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.pushButton_12.setText("")
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_2.addWidget(self.pushButton_12, 7, 3, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(240, 260))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 3, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.text_to_talk_lbl.setText(_translate("MainWindow", "TextLabel"))
        self.collection_name_lbl.setText(_translate("MainWindow", "MAIN"))
import app_resources_rc
