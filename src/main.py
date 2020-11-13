# main.py
#
# Copyright 2020 Дмитрий Кузнецов
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
from PyQt5 import QtWidgets
from sql_utils import *
import mainwindow
import datetime
import re


class TicketAgencyApp(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self):
        super(TicketAgencyApp, self).__init__()
        self.order_list = []
        self.order_is_payed = False
        self.setupUi(self)
        self.payButton.clicked.connect(self.pay_button_clicked)
        self.addToOrderButton.clicked.connect(self.add_to_order_button_clicked)
        self.formTicketsButton.clicked.connect(self.form_ticket_button_clicked)
        self.cancelButton.clicked.connect(self.cancel_button_clicked)
        self.clearDataButton.clicked.connect(self.clear_data)
        self.dateFrom.setDate(datetime.date.today())
        self.dateTo.setDate(datetime.date.today())
        self.dateFrom.dateChanged.connect(self.date_time_is_changed)
        self.dateTo.dateChanged.connect(self.date_time_is_changed)
        self.timeFrom.timeChanged.connect(self.date_time_is_changed)
        self.timeTo.timeChanged.connect(self.date_time_is_changed)
        self.eventSiteTypeChoice.addItems(event_site_types_list())
        self.eventSiteTypeChoice.activated.connect(self.event_site_type_choose)
        self.eventSiteChoice.activated.connect(self.event_site_choose)
        self.eventTypeChoice.activated.connect(self.event_type_choose)
        self.eventChoice.activated.connect(self.event_choose)
        self.rowChoice.activated.connect(self.row_choose)
        self.placeChoice.activated.connect(self.place_choose)

    def pay_button_clicked(self):
        if not self.order_is_payed and not self.order_list == []:
            first_name = self.firstName.text()
            last_name = self.lastName.text()
            email = self.email.text()
            if email == '':
                self.email.setText('Введите E-mail')
            email_is_valid = self.check_email(email)
            if email_is_valid:
                email = email.lower()
                uin_client = find_client(email)
                if uin_client is None:
                    add_client(email, first_name, last_name)
                    uin_client = find_client(email)
                    add_order_for_new(uin_client)
                else:
                    add_order_for_old(uin_client)

                last_order = find_last_order(uin_client)
                for ticket in self.order_list:
                    buy_ticket(ticket, last_order)
                self.order_is_payed = True

    def add_to_order_button_clicked(self):
        event = self.eventChoice.currentText()
        row = self.rowChoice.currentText()
        place = self.placeChoice.currentText()
        if event and row and place:
            ticket = find_ticket(event, row, place)
            ticket_reservation(ticket[0])
            self.order_list.append(str(ticket[0]))
            self.ticketsList.clear()
            self.ticketsList.addItems(self.order_list)
            self.row_choose()
        elif not place:
            self.event_choose()

    def form_ticket_button_clicked(self):
        pass

    def cancel_button_clicked(self):
        if not self.order_is_payed:
            for i in self.order_list:
                ticket_unreserved(int(i))
            self.order_list = []
            self.ticketsList.clear()

    def clear_data(self):
        self.firstName.clear()
        self.lastName.clear()
        self.email.clear()

    def date_time_is_changed(self):
        self.eventChoice.clear()
        self.rowChoice.clear()
        self.placeChoice.clear()
        self.eventTypeChoice.clear()
        self.ticketPrice.setText('0')

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
        if event:
            rows = rows_list(event)
            self.rowChoice.clear()
            self.rowChoice.addItems(rows)

    def row_choose(self):
        event = self.eventChoice.currentText()
        row = self.rowChoice.currentText()
        places = places_list(event, row)
        self.placeChoice.clear()
        self.placeChoice.addItems(places)

    def place_choose(self):
        row = self.rowChoice.currentText()
        place = self.placeChoice.currentText()
        event = self.eventChoice.currentText()
        ticket = find_ticket(event, row, place)
        self.ticketPrice.setText(str(ticket[1]))

    def get_date_time(self):
        date_from = str(self.dateFrom.date().toPyDate())
        date_to = str(self.dateTo.date().toPyDate())
        time_from = str(self.timeFrom.time().toPyTime())
        time_to = str(self.timeTo.time().toPyTime())
        return date_from, date_to, time_from, time_to

    @staticmethod
    def check_email(email: str):
        email_template = '^[0-9A-Za-z]+[\._]?[0-9A-Za-z]+[@]\w+[.]\w+$'
        if re.search(email_template, email):
            return True
        else:
            return False


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = TicketAgencyApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
