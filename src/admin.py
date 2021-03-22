import sys
from PyQt5 import QtWidgets
from sql_utils import *
import admin_ui
import datetime
import json


class TicketAgencyAdmin(QtWidgets.QMainWindow, admin_ui.Ui_MainWindow):
    def __init__(self):
        super(TicketAgencyAdmin, self).__init__()
        self.setupUi(self)
        self.types = json.load(open('../resources/types.json', 'r'))
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
        self.eventSiteType.addItems(self.types)
        self.eventSiteTypeChoiceTool.addItems(self.types)
        self.eventSiteTypeChoiceTool.activated.connect(self.event_site_type_tool_choose)
        self.eventSiteTypeTicket.addItems(self.types)
        self.eventSiteTypeTicket.activated.connect(self.event_site_type_ticket_choose)
        self.eventTypeTicket.activated.connect(self.event_type_ticket_choose)
        self.addTicketsButton.clicked.connect(self.add_tickets_button_clicked)

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
        event = self.eventChoice.currentText()
        available_tickets = len(available_tickets_list(event))
        tickets_count = len(tickets_list(event))
        sold_tickets = len(sold_tickets_list(event))
        self.eventDate.clear()
        date, time = event_date_time(event)
        date = datetime.date.fromisoformat(date)
        date = date.strftime('%d.%m.%Y')
        self.eventDate.setText(str(date))
        self.eventTime.setText(time)
        self.availableTicketsCount.setText(str(available_tickets))
        self.allTicketsCount.setText(str(tickets_count))
        self.soldTicketsCount.setText(str(sold_tickets))

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
        self.viewTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.viewTable.horizontalHeader().setVisible(True)
        for i, item in enumerate(content):
            for j, idx in enumerate(item):
                self.viewTable.setItem(i, j, QtWidgets.QTableWidgetItem(str(idx)))

    def event_site_type_tool_choose(self):
        event_site_type = self.eventSiteTypeChoiceTool.currentText()
        event_site_list = event_sites_list(event_site_type)
        self.eventSiteChoiceTool.clear()
        self.eventSiteChoiceTool.addItems(event_site_list)
        self.eventTypeChoiceTool.clear()
        self.eventTypeChoiceTool.addItems(self.types[event_site_type])

    def add_event_site_button_clicked(self):
        event_site_name = self.eventSiteName.text()
        event_site_type = self.eventSiteType.currentText()
        add_event_site(event_site_name, event_site_type)
        self.eventSiteName.clear()

    def add_event_button_clicked(self):
        event_site_type = self.eventSiteTypeChoiceTool.currentText()
        event_site = self.eventSiteChoiceTool.currentText()
        event_type = self.eventTypeChoiceTool.currentText()
        event_name = self.eventName.text()
        event_date = str(self.eventDateChoice.date().toPyDate())
        event_time = str(self.eventTimeChoice.time().toPyTime().strftime('%H:%M'))
        add_event(event_site, event_site_type, event_type, event_name, event_date, event_time)
        self.eventName.clear()

    def event_site_type_ticket_choose(self):
        event_site_type = self.eventSiteTypeTicket.currentText()
        event_site_list = event_sites_list(event_site_type)
        self.eventSiteTicket.clear()
        self.eventSiteTicket.addItems(event_site_list)
        self.eventTypeTicket.clear()
        self.eventTypeTicket.addItems(self.types[event_site_type])

    def event_type_ticket_choose(self):
        date_from = '1970-01-01'
        date_to = '2199-01-01'
        time_from = '00:00'
        time_to = '23:59'
        event_site = self.eventSiteTicket.currentText()
        event_type = self.eventTypeTicket.currentText()
        event_list = events_list(event_site, event_type, date_from, date_to, time_from, time_to)
        self.eventTicket.clear()
        self.eventTicket.addItems(event_list)

    def add_tickets_button_clicked(self):
        event_site_type = self.eventSiteTypeTicket.currentText()
        event_site = self.eventSiteTicket.currentText()
        event_type = self.eventTypeTicket.currentText()
        event = self.eventTicket.currentText()
        rows_count = int(self.rowsCount.value())
        places_count = int(self.placesCount.value())
        first_category_price = float(self.firstCategoryPrice.value())
        second_category_price = float(self.secondCategoryPrice.value())
        third_category_price = float(self.thirdCategoryPrice.value())
        first_category_from = int(self.firstCategoryFrom.value())
        first_category_to = int(self.firstCategoryTo.value())
        second_category_from = int(self.secondCategoryFrom.value())
        second_category_to = int(self.secondCategoryTo.value())
        third_category_from = int(self.thirdCategoryFrom.value())
        third_category_to = int(self.thirdCategoryTo.value())
        for row in range(1, rows_count + 1, 1):
            for place in range(1, places_count + 1, 1):
                if first_category_from <= row <= first_category_to:
                    price = first_category_price
                elif second_category_from <= row <= second_category_to:
                    price = second_category_price
                elif third_category_from <= row <= third_category_to:
                    price = third_category_price
                else:
                    break
                add_ticket(event_site, event_site_type, event_type, event, row, place, price)

        self.eventTicket.clear()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = TicketAgencyAdmin()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
