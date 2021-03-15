# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1482, 913)
        MainWindow.setMinimumSize(QtCore.QSize(1482, 872))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.toolsChoice = QtWidgets.QTabWidget(self.centralwidget)
        self.toolsChoice.setGeometry(QtCore.QRect(10, 10, 1461, 891))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.toolsChoice.setFont(font)
        self.toolsChoice.setObjectName("toolsChoice")
        self.ticketsViewTool = QtWidgets.QWidget()
        self.ticketsViewTool.setObjectName("ticketsViewTool")
        self.gridLayoutWidget = QtWidgets.QWidget(self.ticketsViewTool)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 40, 641, 491))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.ticketChooser = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.ticketChooser.setContentsMargins(0, 0, 0, 0)
        self.ticketChooser.setObjectName("ticketChooser")
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.ticketChooser.addWidget(self.label_11, 2, 1, 1, 1)
        self.allTicketsCount = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.allTicketsCount.setFont(font)
        self.allTicketsCount.setText("")
        self.allTicketsCount.setObjectName("allTicketsCount")
        self.ticketChooser.addWidget(self.allTicketsCount, 10, 1, 1, 2)
        self.eventSiteTypeChoice = QtWidgets.QComboBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.eventSiteTypeChoice.setFont(font)
        self.eventSiteTypeChoice.setObjectName("eventSiteTypeChoice")
        self.ticketChooser.addWidget(self.eventSiteTypeChoice, 4, 1, 1, 2)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.ticketChooser.addWidget(self.label_10, 2, 0, 1, 1)
        self.eventSiteChoice = QtWidgets.QComboBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.eventSiteChoice.setFont(font)
        self.eventSiteChoice.setObjectName("eventSiteChoice")
        self.ticketChooser.addWidget(self.eventSiteChoice, 5, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.ticketChooser.addWidget(self.label_2, 5, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.ticketChooser.addWidget(self.label_18, 8, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.ticketChooser.addWidget(self.label_14, 6, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.ticketChooser.addWidget(self.label_7, 12, 0, 1, 1)
        self.availableTicketsCount = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.availableTicketsCount.setFont(font)
        self.availableTicketsCount.setText("")
        self.availableTicketsCount.setObjectName("availableTicketsCount")
        self.ticketChooser.addWidget(self.availableTicketsCount, 11, 1, 1, 2)
        self.timeTo = QtWidgets.QTimeEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.timeTo.setFont(font)
        self.timeTo.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(23, 59, 0)))
        self.timeTo.setCurrentSection(QtWidgets.QDateTimeEdit.MinuteSection)
        self.timeTo.setObjectName("timeTo")
        self.ticketChooser.addWidget(self.timeTo, 3, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.ticketChooser.addWidget(self.label_12, 2, 2, 1, 1)
        self.dateFrom = QtWidgets.QDateEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.dateFrom.setFont(font)
        self.dateFrom.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.dateFrom.setCalendarPopup(True)
        self.dateFrom.setCurrentSectionIndex(0)
        self.dateFrom.setObjectName("dateFrom")
        self.ticketChooser.addWidget(self.dateFrom, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.ticketChooser.addWidget(self.label_6, 11, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.ticketChooser.addWidget(self.label_16, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.ticketChooser.addWidget(self.label_3, 10, 0, 1, 1)
        self.eventChoice = QtWidgets.QComboBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.eventChoice.setFont(font)
        self.eventChoice.setObjectName("eventChoice")
        self.ticketChooser.addWidget(self.eventChoice, 7, 1, 1, 2)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.ticketChooser.addWidget(self.label_9, 0, 0, 1, 1)
        self.soldTicketsCount = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soldTicketsCount.setFont(font)
        self.soldTicketsCount.setText("")
        self.soldTicketsCount.setObjectName("soldTicketsCount")
        self.ticketChooser.addWidget(self.soldTicketsCount, 12, 1, 1, 2)
        self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.ticketChooser.addWidget(self.label_19, 9, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.ticketChooser.addWidget(self.label_15, 0, 1, 1, 1)
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
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.ticketChooser.addWidget(self.label_17, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.ticketChooser.addWidget(self.label, 7, 0, 1, 1)
        self.eventTypeChoice = QtWidgets.QComboBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.eventTypeChoice.setFont(font)
        self.eventTypeChoice.setObjectName("eventTypeChoice")
        self.ticketChooser.addWidget(self.eventTypeChoice, 6, 1, 1, 2)
        self.timeFrom = QtWidgets.QTimeEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.timeFrom.setFont(font)
        self.timeFrom.setKeyboardTracking(False)
        self.timeFrom.setCurrentSection(QtWidgets.QDateTimeEdit.MinuteSection)
        self.timeFrom.setCalendarPopup(False)
        self.timeFrom.setObjectName("timeFrom")
        self.ticketChooser.addWidget(self.timeFrom, 3, 1, 1, 1)
        self.dateTo = QtWidgets.QDateEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.dateTo.setFont(font)
        self.dateTo.setCalendarPopup(True)
        self.dateTo.setObjectName("dateTo")
        self.ticketChooser.addWidget(self.dateTo, 1, 2, 1, 1)
        self.toolsChoice.addTab(self.ticketsViewTool, "")
        self.tablesViewTool = QtWidgets.QWidget()
        self.tablesViewTool.setObjectName("tablesViewTool")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tablesViewTool)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 1431, 841))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.choiceTables = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.choiceTables.setContentsMargins(0, 0, 0, 0)
        self.choiceTables.setObjectName("choiceTables")
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.choiceTables.addWidget(self.label_4, 0, 0, 1, 1)
        self.choiceTable = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.choiceTable.setFont(font)
        self.choiceTable.setObjectName("choiceTable")
        self.choiceTables.addWidget(self.choiceTable, 0, 1, 1, 1)
        self.viewTable = QtWidgets.QTableWidget(self.gridLayoutWidget_2)
        self.viewTable.setObjectName("viewTable")
        self.viewTable.setColumnCount(0)
        self.viewTable.setRowCount(0)
        self.choiceTables.addWidget(self.viewTable, 1, 0, 1, 2)
        self.toolsChoice.addTab(self.tablesViewTool, "")
        self.addTools = QtWidgets.QWidget()
        self.addTools.setObjectName("addTools")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.addTools)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 210, 661, 321))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.addEvent = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.addEvent.setContentsMargins(0, 0, 0, 0)
        self.addEvent.setObjectName("addEvent")
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.addEvent.addWidget(self.label_8, 0, 1, 1, 4)
        self.label_20 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.addEvent.addWidget(self.label_20, 3, 1, 1, 2)
        self.label_29 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.addEvent.addWidget(self.label_29, 1, 1, 1, 2)
        self.eventTimeChoice = QtWidgets.QTimeEdit(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.eventTimeChoice.setFont(font)
        self.eventTimeChoice.setObjectName("eventTimeChoice")
        self.addEvent.addWidget(self.eventTimeChoice, 5, 4, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.addEvent.addWidget(self.label_27, 5, 3, 1, 1)
        self.eventSiteChoiceTool = QtWidgets.QComboBox(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.eventSiteChoiceTool.setFont(font)
        self.eventSiteChoiceTool.setObjectName("eventSiteChoiceTool")
        self.addEvent.addWidget(self.eventSiteChoiceTool, 2, 3, 1, 2)
        self.eventTypeChoiceTool = QtWidgets.QComboBox(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.eventTypeChoiceTool.setFont(font)
        self.eventTypeChoiceTool.setObjectName("eventTypeChoiceTool")
        self.addEvent.addWidget(self.eventTypeChoiceTool, 3, 3, 1, 2)
        self.eventDateChoice = QtWidgets.QDateEdit(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.eventDateChoice.setFont(font)
        self.eventDateChoice.setCalendarPopup(True)
        self.eventDateChoice.setObjectName("eventDateChoice")
        self.addEvent.addWidget(self.eventDateChoice, 5, 2, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.addEvent.addWidget(self.label_26, 5, 1, 1, 1)
        self.eventName = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.eventName.setFont(font)
        self.eventName.setInputMethodHints(QtCore.Qt.ImhNone)
        self.eventName.setClearButtonEnabled(False)
        self.eventName.setObjectName("eventName")
        self.addEvent.addWidget(self.eventName, 4, 1, 1, 4)
        self.label_24 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.addEvent.addWidget(self.label_24, 2, 1, 1, 2)
        self.eventSiteTypeChoiceTool = QtWidgets.QComboBox(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.eventSiteTypeChoiceTool.setFont(font)
        self.eventSiteTypeChoiceTool.setObjectName("eventSiteTypeChoiceTool")
        self.addEvent.addWidget(self.eventSiteTypeChoiceTool, 1, 3, 1, 2)
        self.addEventButton = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.addEventButton.setFont(font)
        self.addEventButton.setObjectName("addEventButton")
        self.addEvent.addWidget(self.addEventButton, 6, 1, 1, 4)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.addTools)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 661, 181))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.addEventSite = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.addEventSite.setContentsMargins(0, 0, 0, 0)
        self.addEventSite.setObjectName("addEventSite")
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.addEventSite.addWidget(self.label_5, 0, 1, 1, 2)
        self.addEventSiteButton = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.addEventSiteButton.setFont(font)
        self.addEventSiteButton.setObjectName("addEventSiteButton")
        self.addEventSite.addWidget(self.addEventSiteButton, 3, 1, 1, 2)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.addEventSite.addWidget(self.label_13, 1, 1, 1, 1)
        self.eventSiteType = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.eventSiteType.setFont(font)
        self.eventSiteType.setObjectName("eventSiteType")
        self.addEventSite.addWidget(self.eventSiteType, 1, 2, 1, 1)
        self.eventSiteName = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.eventSiteName.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.eventSiteName.setFont(font)
        self.eventSiteName.setFrame(True)
        self.eventSiteName.setDragEnabled(False)
        self.eventSiteName.setReadOnly(False)
        self.eventSiteName.setClearButtonEnabled(False)
        self.eventSiteName.setObjectName("eventSiteName")
        self.addEventSite.addWidget(self.eventSiteName, 2, 1, 1, 2)
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.addTools)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(720, 10, 721, 521))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.addTickets = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.addTickets.setContentsMargins(0, 0, 0, 0)
        self.addTickets.setObjectName("addTickets")
        self.label_28 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.addTickets.addWidget(self.label_28, 3, 0, 1, 2)
        self.label_22 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.addTickets.addWidget(self.label_22, 2, 0, 1, 2)
        self.label_34 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.addTickets.addWidget(self.label_34, 6, 3, 1, 1)
        self.secondClassFrom = QtWidgets.QSpinBox(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.secondClassFrom.setFont(font)
        self.secondClassFrom.setObjectName("secondClassFrom")
        self.addTickets.addWidget(self.secondClassFrom, 8, 2, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.addTickets.addWidget(self.label_23, 5, 2, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.addTickets.addWidget(self.label_33, 6, 2, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.addTickets.addWidget(self.label_21, 0, 0, 1, 4)
        self.rowsCount = QtWidgets.QSpinBox(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.rowsCount.setFont(font)
        self.rowsCount.setMinimum(1)
        self.rowsCount.setMaximum(1000)
        self.rowsCount.setObjectName("rowsCount")
        self.addTickets.addWidget(self.rowsCount, 5, 1, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.addTickets.addWidget(self.label_25, 5, 0, 1, 1)
        self.eventSiteTicket = QtWidgets.QComboBox(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.eventSiteTicket.setFont(font)
        self.eventSiteTicket.setObjectName("eventSiteTicket")
        self.addTickets.addWidget(self.eventSiteTicket, 2, 2, 1, 2)
        self.label_30 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.addTickets.addWidget(self.label_30, 1, 0, 1, 2)
        self.eventSiteTypeTicket = QtWidgets.QComboBox(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.eventSiteTypeTicket.setFont(font)
        self.eventSiteTypeTicket.setObjectName("eventSiteTypeTicket")
        self.addTickets.addWidget(self.eventSiteTypeTicket, 1, 2, 1, 2)
        self.firstClassFrom = QtWidgets.QSpinBox(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.firstClassFrom.setFont(font)
        self.firstClassFrom.setObjectName("firstClassFrom")
        self.addTickets.addWidget(self.firstClassFrom, 7, 2, 1, 1)
        self.eventTypeTicket = QtWidgets.QComboBox(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.eventTypeTicket.setFont(font)
        self.eventTypeTicket.setObjectName("eventTypeTicket")
        self.addTickets.addWidget(self.eventTypeTicket, 3, 2, 1, 2)
        self.placesCount = QtWidgets.QSpinBox(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.placesCount.setFont(font)
        self.placesCount.setMinimum(1)
        self.placesCount.setMaximum(1000)
        self.placesCount.setObjectName("placesCount")
        self.addTickets.addWidget(self.placesCount, 5, 3, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.addTickets.addWidget(self.label_32, 6, 0, 1, 2)
        self.eventTicket = QtWidgets.QComboBox(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.eventTicket.setFont(font)
        self.eventTicket.setObjectName("eventTicket")
        self.addTickets.addWidget(self.eventTicket, 4, 2, 1, 2)
        self.label_31 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.addTickets.addWidget(self.label_31, 4, 0, 1, 2)
        self.thirdClassFrom = QtWidgets.QSpinBox(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.thirdClassFrom.setFont(font)
        self.thirdClassFrom.setObjectName("thirdClassFrom")
        self.addTickets.addWidget(self.thirdClassFrom, 9, 2, 1, 1)
        self.firstClassTo = QtWidgets.QSpinBox(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.firstClassTo.setFont(font)
        self.firstClassTo.setObjectName("firstClassTo")
        self.addTickets.addWidget(self.firstClassTo, 7, 3, 1, 1)
        self.secondClassTo = QtWidgets.QSpinBox(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.secondClassTo.setFont(font)
        self.secondClassTo.setObjectName("secondClassTo")
        self.addTickets.addWidget(self.secondClassTo, 8, 3, 1, 1)
        self.thirdClassTo = QtWidgets.QSpinBox(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.thirdClassTo.setFont(font)
        self.thirdClassTo.setObjectName("thirdClassTo")
        self.addTickets.addWidget(self.thirdClassTo, 9, 3, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.addTickets.addWidget(self.label_35, 7, 0, 1, 2)
        self.label_36 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.addTickets.addWidget(self.label_36, 8, 0, 1, 2)
        self.label_37 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.addTickets.addWidget(self.label_37, 9, 0, 1, 2)
        self.addTicketsButton = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.addTicketsButton.setFont(font)
        self.addTicketsButton.setObjectName("addTicketsButton")
        self.addTickets.addWidget(self.addTicketsButton, 10, 0, 1, 4)
        self.toolsChoice.addTab(self.addTools, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.toolsChoice.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Билетное Агенство \"Кузница\""))
        self.label_11.setText(_translate("MainWindow", "С"))
        self.label_10.setText(_translate("MainWindow", "Выберите время"))
        self.label_2.setText(_translate("MainWindow", "Выберите площадку"))
        self.label_18.setText(_translate("MainWindow", "Дата мероприятия"))
        self.label_14.setText(_translate("MainWindow", "Выберите тип мероприятия"))
        self.label_7.setText(_translate("MainWindow", "Продано"))
        self.label_12.setText(_translate("MainWindow", "По"))
        self.label_6.setText(_translate("MainWindow", "Доступно к покупке"))
        self.label_16.setText(_translate("MainWindow", "По"))
        self.label_3.setText(_translate("MainWindow", "Всего билетов"))
        self.label_9.setText(_translate("MainWindow", "Выберите дату"))
        self.label_19.setText(_translate("MainWindow", "Время мероприятия"))
        self.label_15.setText(_translate("MainWindow", "С"))
        self.label_17.setText(_translate("MainWindow", "Выберите тип площадки"))
        self.label.setText(_translate("MainWindow", "Выберите мероприятие"))
        self.toolsChoice.setTabText(self.toolsChoice.indexOf(self.ticketsViewTool), _translate("MainWindow", "Просмотр билетов"))
        self.label_4.setText(_translate("MainWindow", "Выберите таблицу"))
        self.toolsChoice.setTabText(self.toolsChoice.indexOf(self.tablesViewTool), _translate("MainWindow", "Просмотр таблиц"))
        self.label_8.setText(_translate("MainWindow", "Добавить мероприятие"))
        self.label_20.setText(_translate("MainWindow", "Выберите тип мероприятия"))
        self.label_29.setText(_translate("MainWindow", "Выберите тип площадки"))
        self.label_27.setText(_translate("MainWindow", "Время"))
        self.label_26.setText(_translate("MainWindow", "Дата"))
        self.eventName.setPlaceholderText(_translate("MainWindow", "Название мероприятия"))
        self.label_24.setText(_translate("MainWindow", "Выберите площадку"))
        self.addEventButton.setText(_translate("MainWindow", "Добавить"))
        self.label_5.setText(_translate("MainWindow", "Добавить площадку"))
        self.addEventSiteButton.setText(_translate("MainWindow", "Добавить"))
        self.label_13.setText(_translate("MainWindow", "Выберите тип площадки"))
        self.eventSiteName.setPlaceholderText(_translate("MainWindow", "Название площадки"))
        self.label_28.setText(_translate("MainWindow", "Выберите тип мероприятия"))
        self.label_22.setText(_translate("MainWindow", "Выберите площадку"))
        self.label_34.setText(_translate("MainWindow", "По"))
        self.label_23.setText(_translate("MainWindow", "Количество мест"))
        self.label_33.setText(_translate("MainWindow", "С"))
        self.label_21.setText(_translate("MainWindow", "Добавить билеты"))
        self.label_25.setText(_translate("MainWindow", "Количество рядов"))
        self.label_30.setText(_translate("MainWindow", "Выберите тип площадки"))
        self.label_32.setText(_translate("MainWindow", "Классы билетов по рядам"))
        self.label_31.setText(_translate("MainWindow", "Выберите мероприятие"))
        self.label_35.setText(_translate("MainWindow", "Первый класс"))
        self.label_36.setText(_translate("MainWindow", "Второй класс"))
        self.label_37.setText(_translate("MainWindow", "Третий класс"))
        self.addTicketsButton.setText(_translate("MainWindow", "Добавить"))
        self.toolsChoice.setTabText(self.toolsChoice.indexOf(self.addTools), _translate("MainWindow", "Заполнение базы данных"))

