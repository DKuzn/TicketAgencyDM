import sys
from PyQt5 import QtWidgets
from sql_utils import *
from form_tickets import get_a4
import admin_ui
import datetime
import json
import os
import platform
import tempfile


class TicketAgencyAdmin(QtWidgets.QMainWindow, admin_ui.Ui_MainWindow):
    def __init__(self):
        super(TicketAgencyAdmin, self).__init__()
        self.setupUi(self)
        self.types = json.load(open('../resources/types.json', 'r', encoding='UTF-8'))
        self.ticketsListRecovery.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
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
        self.eventSiteTicket.activated.connect(self.event_site_ticket_choose)
        self.eventTypeTicket.activated.connect(self.event_type_ticket_choose)
        self.eventTicket.activated.connect(self.event_ticket_choose)
        self.addTicketsButton.clicked.connect(self.add_tickets_button_clicked)
        self.eventSiteName.textChanged.connect(self.event_site_name_text_changed)
        self.eventName.textChanged.connect(self.event_name_text_changed)
        self.applyDiscountButton.clicked.connect(self.apply_discount_button_clicked)
        self.priceIncreaseButton.clicked.connect(self.price_increase_button_clicked)
        self.showNearestEventButton.clicked.connect(self.show_nearest_event_button_clicked)
        self.findOrdersButton.clicked.connect(self.find_order_button_clicked)
        self.ordersList.itemClicked.connect(self.orders_list_item_clicked)
        self.ticketsRecoveryButton.clicked.connect(self.tickets_recovery_button_clicked)
        self.eventSiteTypeNearest.addItems(self.types)
        self.eventSiteTypeNearest.activated.connect(self.event_site_type_nearest_choose)
        self.allEventSitesBox.stateChanged.connect(self.all_event_sites_box_change_state)
        self.ticketsListRecovery.itemClicked.connect(self.tickets_list_recovery_select_row)

    def event_site_name_text_changed(self):
        self.eventSiteName.setStyleSheet('color: black')
        self.addEventSiteButton.setEnabled(True)
        self.addEventSiteStatus.setStyleSheet('color: blue')
        self.addEventSiteStatus.setText('Добавление...')

    def event_name_text_changed(self):
        self.eventName.setStyleSheet('color: black')
        self.addEventButton.setEnabled(True)
        self.addEventStatus.setStyleSheet('color: blue')
        self.addEventStatus.setText('Добавление...')

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
        try:
            if not event_site_name == '':
                add_event_site(event_site_name, event_site_type)
                self.eventSiteName.setStyleSheet('color: green')
                self.addEventSiteStatus.setStyleSheet('color: green')
                self.addEventSiteStatus.setText('Площадка добавлена успешно!')
            else:
                self.eventSiteName.setStyleSheet('color: red')
                self.addEventSiteStatus.setStyleSheet('color: red')
                self.addEventSiteStatus.setText('Ошибка! Введите название площадки.')
        except psycopg2.errors.UniqueViolation:
            self.eventSiteName.setStyleSheet('color: red')
            self.addEventSiteStatus.setStyleSheet('color: red')
            self.addEventSiteStatus.setText('Ошибка! Данная площадка была добавлена ранее.')
            dbase.rollback()

    def add_event_button_clicked(self):
        event_site_type = self.eventSiteTypeChoiceTool.currentText()
        event_site = self.eventSiteChoiceTool.currentText()
        event_type = self.eventTypeChoiceTool.currentText()
        event_name = self.eventName.text()
        event_date = str(self.eventDateChoice.date().toPyDate())
        event_time = str(self.eventTimeChoice.time().toPyTime().strftime('%H:%M'))
        try:
            if '' not in (event_site_type, event_site, event_type, event_name):
                add_event(event_site, event_site_type, event_type, event_name, event_date, event_time)
                self.eventName.setStyleSheet('color: green')
                self.addEventStatus.setStyleSheet('color: green')
                self.addEventStatus.setText('Мероприятие добавлено успешно!')
            else:
                self.eventName.setStyleSheet('color: red')
                self.addEventStatus.setStyleSheet('color: red')
                self.addEventStatus.setText('Ошибка! Введите название мероприятия.')
        except psycopg2.errors.UniqueViolation:
            self.eventName.setStyleSheet('color: red')
            self.addEventStatus.setStyleSheet('color: red')
            self.addEventStatus.setText('Ошибка! Данное мероприятие было добавлено ранее.')
            dbase.rollback()

    def event_site_type_ticket_choose(self):
        event_site_type = self.eventSiteTypeTicket.currentText()
        event_site_list = event_sites_list(event_site_type)
        self.eventSiteTicket.clear()
        self.eventSiteTicket.addItems(event_site_list)
        self.eventTypeTicket.clear()
        self.eventTicket.clear()

    def event_site_ticket_choose(self):
        event_site_type = self.eventSiteTypeTicket.currentText()
        self.eventTypeTicket.clear()
        self.eventTypeTicket.addItems(self.types[event_site_type])
        self.eventTicket.clear()

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

    def event_ticket_choose(self):
        self.addTicketsButton.setEnabled(True)
        self.addTicketsStatus.setStyleSheet('color: blue')
        self.addTicketsStatus.setText('Добавление...')

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
                    self.addTicketsStatus.setStyleSheet('color: red')
                    self.addTicketsStatus.setText('Ошибка! Укажите диапазон рядов для категории.')
                    break

                try:
                    if price > 0.0:
                        add_ticket(event_site, event_site_type, event_type, event, row, place, price)
                    else:
                        self.addTicketsStatus.setStyleSheet('color: red')
                        self.addTicketsStatus.setText('Ошибка! Укажите цену для категории.')
                        break

                except psycopg2.errors.UniqueViolation:
                    self.addTicketsStatus.setStyleSheet('color: red')
                    self.addTicketsStatus.setText('Ошибка! Билеты были добавлены ранее.')
                    dbase.rollback()
                    break

            else:
                self.addTicketsStatus.setStyleSheet('color: green')
                self.addTicketsStatus.setText('Билеты успешно добавлены!')

    def apply_discount_button_clicked(self):
        discount = 1.0 - self.discountPercentage.value() / 100.0
        self.update_price(discount)

    def price_increase_button_clicked(self):
        increase = 1.0 + self.increasePercentage.value() / 100.0
        self.update_price(increase)

    def update_price(self, value):
        event = self.eventChoice.currentText()
        event_type = self.eventTypeChoice.currentText()
        tickets = unsold_tickets_list(event, event_type)
        for ticket, price in tickets:
            update_ticket_price(ticket, round(price * value, 2))

    def show_nearest_event_button_clicked(self):
        event_site_type = self.eventSiteTypeNearest.currentText()
        event_site = self.eventSiteNearest.currentText()
        if self.allEventSitesBox.isChecked():
            event = find_nearest_event_all(str(datetime.date.today()))
        else:
            event = find_nearest_event(str(datetime.date.today()), event_site_type, event_site)

        if event is not None:
            self.eventNameNearest.setText(event[0])
            self.eventTypeNearest.setText(event[1])
            self.eventDateNearest.setText(event[2])
            self.eventTimeNearest.setText(event[3])

    def find_order_button_clicked(self):
        email = self.emailFindOrders.text()
        uin_client = find_client(email)
        orders = orders_list(uin_client)
        self.ordersList.clear()
        self.ordersList.addItems(orders)

    def orders_list_item_clicked(self):
        uin_order = int(self.ordersList.currentItem().text())
        tickets = find_tickets_by_order(uin_order)
        for row_number, uin_ticket in enumerate(tickets):
            self.ticketsListRecovery.setRowCount(row_number)
            info = get_ticket_info(uin_ticket)
            for idx, i in enumerate(info):
                self.ticketsListRecovery.setItem(row_number - 1, idx, QtWidgets.QTableWidgetItem(str(i)))

    def tickets_list_recovery_select_row(self):
        row = self.ticketsListRecovery.currentItem().row()
        self.ticketsListRecovery.selectRow(row)
        uin_order = int(self.ordersList.currentItem().text())
        tickets = find_tickets_by_order(uin_order)
        self.ticketsToRecoveryList.addItem(str(tickets[row]))
        uniq = self.remove_duplicates()
        uniq = [str(i) for i in uniq]
        self.ticketsToRecoveryList.clear()
        self.ticketsToRecoveryList.addItems(uniq)

    def tickets_recovery_button_clicked(self):
        tickets = self.remove_duplicates()
        recovery_tickets = get_a4(tickets)
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix='.pdf')
        recovery_tickets[0].save(tmp, format='PDF', resolution=100.0, save_all=True, append_images=recovery_tickets[1:])
        tmp.close()
        if platform.system() == 'Linux':
            os.system('xdg-open ' + tmp.name)
        elif platform.system() == 'Windows':
            os.system(tmp.name)

    def remove_duplicates(self):
        tickets = []
        for row in range(self.ticketsToRecoveryList.count()):
            tickets.append(int(self.ticketsToRecoveryList.item(row).text()))
        tickets = list(set(tickets))
        return tickets

    def event_site_type_nearest_choose(self):
        event_site_type = self.eventSiteTypeNearest.currentText()
        event_sites = event_sites_list(event_site_type)
        self.eventSiteNearest.clear()
        self.eventSiteNearest.addItems(event_sites)

    def all_event_sites_box_change_state(self):
        if self.eventSiteTypeNearest.isEnabled():
            self.eventSiteTypeNearest.setEnabled(False)
            self.eventSiteNearest.setEnabled(False)
        else:
            self.eventSiteTypeNearest.setEnabled(True)
            self.eventSiteNearest.setEnabled(True)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = TicketAgencyAdmin()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
