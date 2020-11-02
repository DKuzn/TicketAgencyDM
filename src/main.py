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


class TicketAgencyApp(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self):
        super(TicketAgencyApp, self).__init__()
        self.order_list = []
        self.setupUi(self)
        self.payButton.clicked.connect(self.pay_button_clicked)
        self.addToOrderButton.clicked.connect(self.add_to_order_button_clicked)
        self.formTicketsButton.clicked.connect(self.form_ticket_button_clicked)
        self.cancelButton.clicked.connect(self.cancel_button_clicked)
        self.dateFrom.setDate(datetime.date.today())
        self.dateTo.setDate(datetime.date.today())
        self.eventSiteChoice.addItems(event_sites_list())
        self.eventSiteChoice.activated.connect(self.event_site_choose)
        self.eventChoice.activated.connect(self.event_choose)
        self.rowChoice.activated.connect(self.row_choose)
        self.placeChoice.activated.connect(self.place_choose)

    def pay_button_clicked(self):
        pass

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
        for i in self.order_list:
            ticket_unreserved(int(i))
        self.ticketsList.clear()

    def event_site_choose(self):
        self.eventChoice.clear()
        self.rowChoice.clear()
        self.placeChoice.clear()
        self.ticketPrice.setText('0')
        self.eventChoice.addItems(events_list(self.eventSiteChoice.currentText()))

    def event_choose(self):
        rows = rows_list(self.eventChoice.currentText())
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


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = TicketAgencyApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
