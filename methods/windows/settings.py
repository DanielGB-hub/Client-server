from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(450, 291)
        self.frame = QtWidgets.QFrame(Form)
        # self.frame.setGeometry(QtCore.QRect(10, 10, 431, 231))
        self.frame.setGeometry(QtCore.QRect(10, 10, 431, 281))  # размер окна "Настройки"
        self.frame.setStyleSheet("QFrame{\n"
                                 "    border: 2px solid #FFFFFF;\n"
                                 "    border-radius: 7px;\n"
                                 "    background-color: #CFCFCF;\n"
                                 "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 120, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
                                      "    border-radius: 7px;\n"
                                      "}")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setClearButtonEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 170, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_3.setStyleSheet("QLineEdit{\n"
                                      "    border-radius: 7px;\n"
                                      "}")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setClearButtonEnabled(False)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(220, 230, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet("QPushButton{\n"
                                        "    color: white;\n"
                                        "    border-radius: 7px;\n"
                                        "    background-color: #454545;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "    background-color: #5E5E5E;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed{\n"
                                        "    background-color: #454545;\n"
                                        "}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(20, 230, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet("QPushButton{\n"
                                        "    color: white;\n"
                                        "    border-radius: 7px;\n"
                                        "    background-color: #454545;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "    background-color: #5E5E5E;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed{\n"
                                        "    background-color: #454545;\n"
                                        "}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(20, 20, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_4.setStyleSheet("QLineEdit{\n"
                                      "    border-radius: 7px;\n"
                                      "}")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setClearButtonEnabled(False)
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)  # добавляем поле пароля
        self.lineEdit_5.setGeometry(QtCore.QRect(20, 70, 391, 41))  # добавляем поле пароля
        self.lineEdit_5.setFont(font)  # добавляем поле пароля
        self.lineEdit_5.setFocusPolicy(QtCore.Qt.ClickFocus)  # добавляем поле пароля
        self.lineEdit_5.setStyleSheet("QLineEdit{\n"
                                      "    border-radius: 7px;\n"
                                      "}")  # добавляем поле пароля
        self.lineEdit_5.setText("")  # добавляем поле пароля
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)  # добавляем поле пароля
        self.lineEdit_5.setClearButtonEnabled(False)  # добавляем поле пароля
        self.lineEdit_5.setObjectName("lineEdit_5")  # добавляем поле пароля

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "IP Сервера"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "PORT Сервера"))
        self.pushButton_6.setText(_translate("Form", "Сохранить"))
        self.pushButton_7.setText(_translate("Form", "Назад"))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "Никнейм (логин)"))
        self.lineEdit_5.setPlaceholderText(_translate("Form", "Пароль"))  # добавляем поле для пароля
