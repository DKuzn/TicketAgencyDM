# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1482, 872)
        MainWindow.setMinimumSize(QtCore.QSize(1482, 872))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 591, 641))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.ticketChooser = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.ticketChooser.setContentsMargins(0, 0, 0, 0)
        self.ticketChooser.setObjectName("ticketChooser")
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.ticketChooser.addWidget(self.label_13, 12, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.ticketChooser.addWidget(self.label_5, 10, 2, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.ticketChooser.addWidget(self.label_14, 6, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.ticketChooser.addWidget(self.label_4, 10, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.ticketChooser.addWidget(self.label_18, 8, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.ticketChooser.addWidget(self.label, 7, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.ticketChooser.addWidget(self.label_17, 4, 0, 1, 1)
        self.timeFrom = QtWidgets.QTimeEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.timeFrom.setFont(font)
        self.timeFrom.setKeyboardTracking(False)
        self.timeFrom.setCurrentSection(QtWidgets.QDateTimeEdit.MinuteSection)
        self.timeFrom.setCalendarPopup(False)
        self.timeFrom.setObjectName("timeFrom")
        self.ticketChooser.addWidget(self.timeFrom, 3, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.ticketChooser.addWidget(self.label_11, 2, 1, 1, 1)
        self.eventSiteTypeChoice = QtWidgets.QComboBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.eventSiteTypeChoice.setFont(font)
        self.eventSiteTypeChoice.setObjectName("eventSiteTypeChoice")
        self.ticketChooser.addWidget(self.eventSiteTypeChoice, 4, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.ticketChooser.addWidget(self.label_2, 5, 0, 1, 1)
        self.dateTo = QtWidgets.QDateEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.dateTo.setFont(font)
        self.dateTo.setCalendarPopup(True)
        self.dateTo.setObjectName("dateTo")
        self.ticketChooser.addWidget(self.dateTo, 1, 2, 1, 1)
        self.dateFrom = QtWidgets.QDateEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.dateFrom.setFont(font)
        self.dateFrom.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.dateFrom.setCalendarPopup(True)
        self.dateFrom.setCurrentSectionIndex(0)
        self.dateFrom.setObjectName("dateFrom")
        self.ticketChooser.addWidget(self.dateFrom, 1, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.ticketChooser.addWidget(self.label_12, 2, 2, 1, 1)
        self.ticketPrice = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ticketPrice.setFont(font)
        self.ticketPrice.setObjectName("ticketPrice")
        self.ticketChooser.addWidget(self.ticketPrice, 12, 1, 1, 1)
        self.placeChoice = QtWidgets.QComboBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.placeChoice.setFont(font)
        self.placeChoice.setObjectName("placeChoice")
        self.ticketChooser.addWidget(self.placeChoice, 11, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.ticketChooser.addWidget(self.label_15, 0, 1, 1, 1)
        self.eventChoice = QtWidgets.QComboBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.eventChoice.setFont(font)
        self.eventChoice.setObjectName("eventChoice")
        self.ticketChooser.addWidget(self.eventChoice, 7, 1, 1, 2)
        self.eventTypeChoice = QtWidgets.QComboBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.eventTypeChoice.setFont(font)
        self.eventTypeChoice.setObjectName("eventTypeChoice")
        self.ticketChooser.addWidget(self.eventTypeChoice, 6, 1, 1, 2)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.ticketChooser.addWidget(self.label_16, 0, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.ticketChooser.addWidget(self.label_7, 12, 0, 1, 1)
        self.eventSiteChoice = QtWidgets.QComboBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.eventSiteChoice.setFont(font)
        self.eventSiteChoice.setObjectName("eventSiteChoice")
        self.ticketChooser.addWidget(self.eventSiteChoice, 5, 1, 1, 2)
        self.timeTo = QtWidgets.QTimeEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.timeTo.setFont(font)
        self.timeTo.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(23, 59, 0)))
        self.timeTo.setCurrentSection(QtWidgets.QDateTimeEdit.MinuteSection)
        self.timeTo.setObjectName("timeTo")
        self.ticketChooser.addWidget(self.timeTo, 3, 2, 1, 1)
        self.addToOrderButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.addToOrderButton.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.addToOrderButton.setFont(font)
        self.addToOrderButton.setObjectName("addToOrderButton")
        self.ticketChooser.addWidget(self.addToOrderButton, 13, 1, 1, 2)
        self.rowChoice = QtWidgets.QComboBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.rowChoice.setFont(font)
        self.rowChoice.setObjectName("rowChoice")
        self.ticketChooser.addWidget(self.rowChoice, 11, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.ticketChooser.addWidget(self.label_19, 9, 0, 1, 1)
        self.eventDate = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.eventDate.setFont(font)
        self.eventDate.setText("")
        self.eventDate.setObjectName("eventDate")
        self.ticketChooser.addWidget(self.eventDate, 8, 1, 1, 2)
        self.eventTime = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.eventTime.setFont(font)
        self.eventTime.setText("")
        self.eventTime.setObjectName("eventTime")
        self.ticketChooser.addWidget(self.eventTime, 9, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.ticketChooser.addWidget(self.label_3, 10, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.ticketChooser.addWidget(self.label_10, 2, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.ticketChooser.addWidget(self.label_9, 0, 0, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 680, 591, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.clientData = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.clientData.setContentsMargins(0, 0, 0, 0)
        self.clientData.setObjectName("clientData")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.clientData.addWidget(self.label_6, 0, QtCore.Qt.AlignHCenter)
        self.firstName = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.firstName.setFont(font)
        self.firstName.setText("")
        self.firstName.setClearButtonEnabled(True)
        self.firstName.setObjectName("firstName")
        self.clientData.addWidget(self.firstName)
        self.lastName = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lastName.setFont(font)
        self.lastName.setText("")
        self.lastName.setClearButtonEnabled(True)
        self.lastName.setObjectName("lastName")
        self.clientData.addWidget(self.lastName)
        self.email = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.email.setFont(font)
        self.email.setClearButtonEnabled(True)
        self.email.setObjectName("email")
        self.clientData.addWidget(self.email)
        self.clearDataButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.clearDataButton.setFont(font)
        self.clearDataButton.setObjectName("clearDataButton")
        self.clientData.addWidget(self.clearDataButton)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(640, 20, 821, 641))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.verticalLayoutWidget_2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.payButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.payButton.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.payButton.setFont(font)
        self.payButton.setObjectName("payButton")
        self.gridLayout.addWidget(self.payButton, 6, 0, 1, 3)
        self.orderStatus = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.orderStatus.setFont(font)
        self.orderStatus.setText("")
        self.orderStatus.setObjectName("orderStatus")
        self.gridLayout.addWidget(self.orderStatus, 2, 2, 1, 1, QtCore.Qt.AlignLeft)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.newOrderButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.newOrderButton.setFont(font)
        self.newOrderButton.setObjectName("newOrderButton")
        self.gridLayout.addWidget(self.newOrderButton, 5, 0, 1, 3)
        self.label_22 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 4, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.label_20 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 2, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.label_23 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 4, 2, 1, 1)
        self.cancelButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.cancelButton.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cancelButton.setFont(font)
        self.cancelButton.setObjectName("cancelButton")
        self.gridLayout.addWidget(self.cancelButton, 7, 0, 1, 3)
        self.totalCost = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.totalCost.setFont(font)
        self.totalCost.setObjectName("totalCost")
        self.gridLayout.addWidget(self.totalCost, 4, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.ticketsList = QtWidgets.QTableWidget(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ticketsList.setFont(font)
        self.ticketsList.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ticketsList.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.ticketsList.setLineWidth(1)
        self.ticketsList.setRowCount(0)
        self.ticketsList.setColumnCount(8)
        self.ticketsList.setObjectName("ticketsList")
        item = QtWidgets.QTableWidgetItem()
        self.ticketsList.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ticketsList.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ticketsList.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.ticketsList.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.ticketsList.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.ticketsList.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.ticketsList.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.ticketsList.setHorizontalHeaderItem(7, item)
        self.ticketsList.horizontalHeader().setMinimumSectionSize(28)
        self.ticketsList.verticalHeader().setSortIndicatorShown(False)
        self.gridLayout.addWidget(self.ticketsList, 3, 0, 1, 3)
        self.formTicketsButton = QtWidgets.QPushButton(self.centralwidget)
        self.formTicketsButton.setEnabled(False)
        self.formTicketsButton.setGeometry(QtCore.QRect(640, 680, 821, 171))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.formTicketsButton.setFont(font)
        self.formTicketsButton.setAcceptDrops(False)
        self.formTicketsButton.setAutoFillBackground(False)
        self.formTicketsButton.setAutoDefault(False)
        self.formTicketsButton.setDefault(False)
        self.formTicketsButton.setFlat(False)
        self.formTicketsButton.setObjectName("formTicketsButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Билетное Агентство \"Кузница\""))
        self.label_13.setText(_translate("MainWindow", "руб."))
        self.label_5.setText(_translate("MainWindow", "Место"))
        self.label_14.setText(_translate("MainWindow", "Выберите тип мероприятия"))
        self.label_4.setText(_translate("MainWindow", "Ряд"))
        self.label_18.setText(_translate("MainWindow", "Дата мероприятия"))
        self.label.setText(_translate("MainWindow", "Выберите мероприятие"))
        self.label_17.setText(_translate("MainWindow", "Выберите тип площадки"))
        self.label_11.setText(_translate("MainWindow", "С"))
        self.label_2.setText(_translate("MainWindow", "Выберите площадку"))
        self.label_12.setText(_translate("MainWindow", "По"))
        self.ticketPrice.setText(_translate("MainWindow", "0"))
        self.label_15.setText(_translate("MainWindow", "С"))
        self.label_16.setText(_translate("MainWindow", "По"))
        self.label_7.setText(_translate("MainWindow", "Цена билета"))
        self.addToOrderButton.setText(_translate("MainWindow", "Добавить в заказ"))
        self.label_19.setText(_translate("MainWindow", "Время мероприятия"))
        self.label_3.setText(_translate("MainWindow", "Выберите место"))
        self.label_10.setText(_translate("MainWindow", "Выберите время"))
        self.label_9.setText(_translate("MainWindow", "Выберите дату"))
        self.label_6.setText(_translate("MainWindow", "Данные о клиенте"))
        self.firstName.setPlaceholderText(_translate("MainWindow", "Имя"))
        self.lastName.setPlaceholderText(_translate("MainWindow", "Фамилия"))
        self.email.setPlaceholderText(_translate("MainWindow", "E-mail (обязательно)"))
        self.clearDataButton.setText(_translate("MainWindow", "Очистить данные"))
        self.payButton.setText(_translate("MainWindow", "Оплатить заказ"))
        self.label_8.setText(_translate("MainWindow", "Заказ"))
        self.newOrderButton.setText(_translate("MainWindow", "Новый заказ"))
        self.label_22.setText(_translate("MainWindow", "Общая стоимость"))
        self.label_20.setText(_translate("MainWindow", "Статус заказа"))
        self.label_23.setText(_translate("MainWindow", "руб."))
        self.cancelButton.setText(_translate("MainWindow", "Отменить заказ"))
        self.totalCost.setText(_translate("MainWindow", "0"))
        item = self.ticketsList.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Тип"))
        item = self.ticketsList.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Название"))
        item = self.ticketsList.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Площадка"))
        item = self.ticketsList.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Дата"))
        item = self.ticketsList.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Время"))
        item = self.ticketsList.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Ряд"))
        item = self.ticketsList.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Место"))
        item = self.ticketsList.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Цена"))
        self.formTicketsButton.setText(_translate("MainWindow", "Сформировать билеты"))

