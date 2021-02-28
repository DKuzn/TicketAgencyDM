import sys
from PyQt5 import QtWidgets
from sql_utils import *
import admin_ui
import datetime


class TicketAgencyAdmin(QtWidgets.QMainWindow, admin_ui.Ui_MainWindow):
    def __init__(self):
        super(TicketAgencyAdmin, self).__init__()
        self.setupUi(self)
        self.dateFrom.setDate(datetime.date.today())
        self.dateTo.setDate(datetime.date.today())
        self.eventDateChoice.setDate(datetime.date.today())
        self.dateFrom.dateChanged.connect(self.date_time_is_changed)
        self.dateTo.dateChanged.connect(self.date_time_is_changed)
        self.timeFrom.timeChanged.connect(self.date_time_is_changed)
        self.timeTo.timeChanged.connect(self.date_time_is_changed)
        self.eventSiteTypeChoice.addItems(event_site_types_list())
        self.eventSiteTypeChoice.activated.connect(self.event_site_type_choose)
        self.eventSiteChoice.activated.connect(self.event_site_choose)
        self.eventTypeChoice.activated.connect(self.event_type_choose)
        self.eventChoice.activated.connect(self.event_choose)
        self.choiceTable.addItems(list_tables())
        self.choiceTable.activated.connect(self.table_choose)
        self.addEventSiteButton.clicked.connect(self.add_event_site_button_clicked)
        self.addEventButton.clicked.connect(self.add_event_button_clicked)

    def date_time_is_changed(self):
        self.eventChoice.clear()
        self.eventTypeChoice.clear()
        self.eventDate.clear()
        self.eventTime.clear()
        self.allTicketsCount.clear()
        self.availableTicketsCount.clear()
        self.soldTicketsCount.clear()

    def event_site_type_choose(self):
        self.date_time_is_changed()
        self.eventSiteChoice.clear()
        self.eventChoice.clear()
        self.eventSiteChoice.addItems(event_sites_list(self.eventSiteTypeChoice.currentText()))

    def event_site_choose(self):
        self.date_time_is_changed()
        date_from, date_to, time_from, time_to = self.get_date_time()
        event_site = self.eventSiteChoice.currentText()
        event_types = event_types_list(event_site, date_from, date_to, time_from, time_to)
        self.eventTypeChoice.addItems(event_types)

    def event_type_choose(self):
        event_site = self.eventSiteChoice.currentText()
        event_type = self.eventTypeChoice.currentText()
        if event_type:
            date_from, date_to, time_from, time_to = self.get_date_time()
            events = events_list(event_site, event_type, date_from, date_to, time_from, time_to)
            self.eventChoice.clear()
            self.eventChoice.addItems(events)

    def event_choose(self):
        pass

    def get_date_time(self):
        date_from = str(self.dateFrom.date().toPyDate())
        date_to = str(self.dateTo.date().toPyDate())
        time_from = str(self.timeFrom.time().toPyTime())
        time_to = str(self.timeTo.time().toPyTime())
        return date_from, date_to, time_from, time_to

    def table_choose(self):
        table_name = self.choiceTable.currentText()
        content = get_table(table_name)
        header = content.pop(0)
        self.viewTable.setColumnCount(len(header))
        self.viewTable.setRowCount(len(content))
        self.viewTable.setHorizontalHeaderLabels(header)
        self.viewTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.viewTable.horizontalHeader().setVisible(True)
        for i, item in enumerate(content):
            for j, idx in enumerate(item):
                self.viewTable.setItem(i, j, QtWidgets.QTableWidgetItem(str(idx)))

    def add_event_site_button_clicked(self):
        event_site_name = self.eventSiteName.text()
        event_site_type = self.eventSiteType.text()
        add_event_site(event_site_name, event_site_type)

    def add_event_button_clicked(self):
        pass


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = TicketAgencyAdmin()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
