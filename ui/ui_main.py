# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtGui import (QCursor,
                           QIcon, QCloseEvent)
from PySide6.QtWidgets import (QAbstractSpinBox, QFrame, QHBoxLayout,
                               QLabel, QLineEdit, QMenuBar,
                               QPushButton, QSizePolicy, QSlider, QSpinBox,
                               QStatusBar, QVBoxLayout, QWidget, QApplication)

from ui import buttons, password


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(542, 519)
        icon = QIcon()
        icon.addFile(u"images/key_black_24dp.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
                                 "    background-color: #121212;\n"
                                 "    color: white;\n"
                                 "    font-family: Verdana;\n"
                                 "    font-size: 16pt;\n"
                                 "    margin: 10px;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton {\n"
                                 "    border: 2px solid gray;\n"
                                 "    border-radius: 5px;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:checked {\n"
                                 "    background-color:#006300;\n"
                                 "    border-color: #090\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton#btn_lower,\n"
                                 "#btn_upper,\n"
                                 "#btn_digits,\n"
                                 "#btn_special {\n"
                                 "    padding:10px\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:hover {\n"
                                 "    border-color: #090\n"
                                 "}\n"
                                 "QPushButton:pressed {\n"
                                 "    border: 4px solid #090\n"
                                 "    border-radius: 5px;\n"
                                 "}\n"
                                 "QFrame {\n"
                                 " border: 2px solid gray;\n"
                                 " border-radius: 5px;\n"
                                 " margin-right: 0;\n"
                                 "}\n"
                                 "QFrame:hover {\n"
                                 "    border-color: #090\n"
                                 "}\n"
                                 "QSlider::groove:horizontal {\n"
                                 "	bacground-color: transparent;\n"
                                 "	height: 5px;\n"
                                 "}\n"
                                 "QSlider::sub-page:horizontal  {\n"
                                 "	background-color: #090;\n"
                                 "}\n"
                                 "QSlider::add-page:horizontal {\n"
                                 "	background-color: gray;\n"
                                 "}\n"
                                 "QSlider::handle:horizontal {\n"
                                 "	backgr"
                                 "ound-color: white;\n"
                                 "	width: 22px;\n"
                                 "	border-radius: 10px;\n"
                                 "}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout_6 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"border: none;\n"
                                        "")
        icon1 = QIcon()
        icon1.addFile(u"images/lock_white_24dp.svg", QSize(), QIcon.Disabled, QIcon.On)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QSize(100, 100))

        self.verticalLayout.addWidget(self.pushButton_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton {\n"
                                      "	border: none;\n"
                                      "	margin: 0;\n"
                                      "	background-color: transparent;\n"
                                      "}")
        icon2 = QIcon()
        icon2.addFile(u"images/visibility_off_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u"images/visibility_white_24dp.svg", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QSize(30, 30))
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(True)

        self.horizontalLayout_5.addWidget(self.pushButton)

        self.horizontalLayout.addWidget(self.frame)

        self.btn_refresh = QPushButton(self.centralwidget)
        self.btn_refresh.setObjectName(u"")
        self.btn_refresh.setStyleSheet(u"QPushButton {\n"
                                       "	margin-right: 0;\n"
                                       "	margin-left: 0;\n"
                                       "}")
        icon3 = QIcon()
        icon3.addFile(u"images/refresh_white_24dp.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_refresh.setIcon(icon3)
        self.btn_refresh.setIconSize(QSize(52, 52))

        self.horizontalLayout.addWidget(self.btn_refresh)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
                                        "	padding: 5px;\n"
                                        "	margin-left: 0\n"
                                        "}")
        icon4 = QIcon()
        icon4.addFile(u"images/content_copy_white_24dp.svg", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_2.setIcon(icon4)
        self.pushButton_2.setIconSize(QSize(42, 42))

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.centralwidget)

        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.slider_length = QSlider(self.centralwidget)
        self.slider_length.setObjectName(u"slider_length")
        self.slider_length.setMinimumSize(QSize(22, 5))
        self.slider_length.setBaseSize(QSize(5, 22))
        self.slider_length.setStyleSheet(u"QSlider::sub-page:horizontal  {\n"
                                         "	background-color: #090;\n"
                                         "}\n"
                                         "QSlider::add-page:horizontal {\n"
                                         "	background-color: gray;\n"
                                         "}\n"
                                         "QSlider::handle:horizontal {\n"
                                         "	background-color:white;\n"
                                         "	border-radius: 5px;\n"
                                         "}")
        self.slider_length.setMaximum(100)
        self.slider_length.setValue(12)
        self.slider_length.setSliderPosition(12)
        self.slider_length.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.slider_length)

        self.spinbox_length = QSpinBox(self.centralwidget)
        self.spinbox_length.setObjectName(u"spinbox_length")
        self.spinbox_length.setStyleSheet(u"QSpinBox {\n"
                                          "	border: 2px solid gray;\n"
                                          "	border-radius: 5px;\n"
                                          "	background: transparent;\n"
                                          "	padding: 2px;\n"
                                          "}\n"
                                          "\n"
                                          "QSpinBox:hover {\n"
                                          "	border-color: #009900\n"
                                          "}")
        self.spinbox_length.setAlignment(Qt.AlignCenter)
        self.spinbox_length.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.horizontalLayout_3.addWidget(self.spinbox_length)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_lower = QPushButton(self.centralwidget)
        self.btn_lower.setObjectName(u"btn_lower")
        self.btn_lower.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.btn_lower)

        self.btn_upper = QPushButton(self.centralwidget)
        self.btn_upper.setObjectName(u"btn_upper")
        self.btn_upper.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.btn_upper)

        self.btn_digits = QPushButton(self.centralwidget)
        self.btn_digits.setObjectName(u"btn_digits")
        self.btn_digits.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.btn_digits)

        self.btn_special = QPushButton(self.centralwidget)
        self.btn_special.setObjectName(u"btn_special")
        self.btn_special.setCheckable(False)

        self.horizontalLayout_4.addWidget(self.btn_special)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 542, 51))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        self.connect_reefresh()
        self.pushButton.clicked.connect(self.change_password_visibility)
        self.pushButton_2.clicked.connect(self.copy_to_clipboard)
        self.do_when_password_edit()

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Password Generator", None))
        self.pushButton_4.setText("")
        self.pushButton.setText("")
        self.btn_refresh.setText("")
        self.pushButton_2.setText("")
        self.label_2.setText("")
        self.label.setText("")
        self.btn_lower.setText(QCoreApplication.translate("MainWindow", u"a-z", None))
        self.btn_upper.setText(QCoreApplication.translate("MainWindow", u"A-Z", None))
        self.btn_digits.setText(QCoreApplication.translate("MainWindow", u"0-9", None))
        self.btn_special.setText(QCoreApplication.translate("MainWindow", u"#$%", None))

    def connect_slider_to_spinbox(self) -> None:
        self.slider_length.valueChanged.connect(self.spinbox_length.setValue)
        self.spinbox_length.valueChanged.connect(self.slider_length.setValue)
        self.spinbox_length.valueChanged.connect(self.set_password)

    def connect_reefresh(self):
        self.btn_refresh.clicked.connect(self.set_password)
        for btn in buttons.GENERATE_PASSWORD:
            getattr(self, btn).clicked.connect(self.set_password)

    def get_characters(self) -> str:
        chars = ""

        for btn in buttons.Characters:
            if getattr(self, btn.name):
                chars += btn.value
        return chars

    def set_password(self) -> None:
        self.lineEdit.setText(
            password.create_new(
                length=self.slider_length.value(),
                characters=self.get_characters()
            )
        )
        self.set_entropy()
        self.set_strength()

    def get_character_number(self) -> int:
        num = 0

        for btn in buttons.CHARACTER_NUMBER.items():
            if getattr(self, btn[0]).isChecked():
                num += btn[1]

        return num

    def set_entropy(self) -> None:
        length = len(self.lineEdit.text())
        char_num = self.get_character_number()
        self.label.setText(
            f"Entropy: {password.get_entropy(length, char_num)} bit"
        )

    def set_strength(self) -> None:
        length = len(self.lineEdit.text())
        char_num = self.get_character_number()
        for strength in password.StrengthToEntropy:
            if password.get_entropy(length, char_num) > strength.value:
                self.label_2.setText(f"Strength: {strength.name}")

    def change_password_visibility(self):
        if self.pushButton.isChecked():
            self.lineEdit.setEchoMode(QLineEdit.Normal)
        else:
            self.lineEdit.setEchoMode(QLineEdit.Password)

    def copy_to_clipboard(self) -> None:
        QApplication.clipboard().setText(self.lineEdit.text())

    def close_event(self, event: QCloseEvent) -> None:
        QApplication.clipboard().clear()

    def do_when_password_edit(self) -> None:
        self.lineEdit.textEdited.connect(self.set_entropy)
        self.lineEdit.textEdited.connect(self.set_strength)
