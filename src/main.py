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
import tempfile
import platform
import os
from PyQt5 import QtWidgets
from sql_utils import *
import mainwindow
import datetime
import re
from form_tickets import get_a4


class TicketAgencyApp(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self):
        super(TicketAgencyApp, self).__init__()
        self.order_list = []
        self.order_is_payed = False
        self.email_is_valid = False
        self.max_tickets = 12
        self.temp_email = ''
        self.total_cost = 0
        self.setupUi(self)
        self.newOrderButton.clicked.connect(self.new_order_button_clicked)
        self.payButton.clicked.connect(self.pay_button_clicked)
        self.addToOrderButton.clicked.connect(self.add_to_order_button_clicked)
        self.formTicketsButton.clicked.connect(self.form_tickets_button_clicked)
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

    def new_order_button_clicked(self):
        if not self.order_is_payed:
            self.cancel_button_clicked()
            self.order_list = []
        else:
            self.order_list = []
        self.order_is_payed = False
        self.formTicketsButton.setEnabled(False)
        first_name = self.firstName.text()
        last_name = self.lastName.text()
        email = self.email.text()
        self.ticketsList.setRowCount(0)
        if email == '':
            self.email.setText('Введите E-mail')
        elif not email == 'Введите E-mail':
            self.email_is_valid = self.check_email(email)
            if self.email_is_valid:
                email = email.lower()
                self.temp_email = email
                uin_client = find_client(self.temp_email)
                if uin_client is None:
                    add_client(email, first_name, last_name)
                    uin_client = find_client(email)
                    add_order_for_new(uin_client)
                else:
                    if find_last_order(uin_client) is None:
                        add_order_for_new(uin_client)
                    else:
                        add_order_for_old(uin_client)
                self.orderStatus.setStyleSheet('color: blue')
                self.orderStatus.setText('Создан')
                self.addToOrderButton.setEnabled(True)
                self.payButton.setEnabled(True)
                self.cancelButton.setEnabled(True)
            elif not self.email_is_valid:
                self.email.setText('Некорректный E-mail')

    def pay_button_clicked(self):
        if not self.order_is_payed and not self.order_list == []:
            uin_client = find_client(self.temp_email)
            last_order = find_last_order(uin_client)
            for ticket in self.order_list:
                buy_ticket(ticket, last_order)
            pay_order(last_order)
            self.order_is_payed = True
            self.orderStatus.setStyleSheet('color: green')
            self.orderStatus.setText('Оплачен')
            self.formTicketsButton.setEnabled(True)

    def add_to_order_button_clicked(self):
        event = self.eventChoice.currentText()
        row = self.rowChoice.currentText()
        place = self.placeChoice.currentText()
        if event and row and place:
            ticket = find_ticket(event, row, place)
            ticket_reservation(ticket[0])
            if len(self.order_list) < self.max_tickets:
                self.order_list.append(str(ticket[0]))
                self.add_ticket_to_list(ticket[0])
                self.totalCost.setText(str(self.total_cost))
                self.row_choose()
        elif not place:
            self.event_choose()

    def form_tickets_button_clicked(self):
        tickets = get_a4(self.order_list)
        tmp = tempfile.NamedTemporaryFile(delete=False)
        tickets[0].save(tmp, format='PDF', resolution=100.0, save_all=True, append_images=tickets[1:])
        if platform.system() == 'Linux':
            os.system('xdg-open ' + tmp.name)
        elif platform.system() == 'Windows':
            os.system(tmp.name)

    def cancel_button_clicked(self):
        if not self.order_is_payed:
            for i in self.order_list:
                ticket_unreserved(int(i))
            self.order_list = []
            self.ticketsList.setRowCount(0)
            uin_client = find_client(self.temp_email)
            last_order = find_last_order(uin_client)
            delete_order(last_order)
            self.total_cost = 0
            self.totalCost.setText('0')
            self.orderStatus.setStyleSheet('color: red')
            self.orderStatus.setText('Отменен')
            self.cancelButton.setEnabled(False)
            self.addToOrderButton.setEnabled(False)
            self.payButton.setEnabled(False)

    def clear_data(self):
        self.firstName.clear()
        self.lastName.clear()
        self.email.clear()

    def add_ticket_to_list(self, uin_ticket):
        row_number = len(self.order_list)
        self.ticketsList.setRowCount(row_number)
        info = get_ticket_info(uin_ticket)
        self.total_cost += info[7]
        for idx, i in enumerate(info):
            self.ticketsList.setItem(row_number - 1, idx, QtWidgets.QTableWidgetItem(str(i)))

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
            self.eventDate.clear()
            date, time = event_date_time(event)
            date = datetime.date.fromisoformat(date)
            date = date.strftime('%d.%m.%Y')
            self.eventDate.setText(str(date))
            self.eventTime.setText(time)

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
