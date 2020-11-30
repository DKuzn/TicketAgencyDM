# sql_utils.py
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

import sqlite3

dbase = sqlite3.connect('../resources/TicketAgencyDB.db')
cursor = dbase.cursor()


def event_site_types_list():
    cursor.execute("SELECT Тип FROM Площадка")
    event_site_types = cursor.fetchall()
    event_site_type_list = [i[0] for i in event_site_types]
    return event_site_type_list


def event_sites_list(event_site_type: str):
    cursor.execute("SELECT Название FROM Площадка WHERE Тип == '%s'" % event_site_type)
    event_sites = cursor.fetchall()
    event_site_list = [i[0] for i in event_sites]
    return event_site_list


def event_types_list(event_site: str, date_from: str, date_to: str, time_from: str, time_to: str):
    cursor.execute("SELECT УИН_Площадки FROM Площадка WHERE Название = '%s'" % event_site)
    uin_event_site = cursor.fetchone()
    cursor.execute("SELECT Тип_мероприятия FROM Мероприятие "
                   "WHERE УИН_Площадки = '%s' AND Дата BETWEEN '%s' AND '%s' "
                   "AND Время BETWEEN '%s' AND '%s'" % (uin_event_site[0], date_from, date_to, time_from, time_to))
    event_types = cursor.fetchall()
    event_type_list = [i[0] for i in event_types]
    event_type_list = list(set(event_type_list))
    return event_type_list


def events_list(event_site: str, event_type: str, date_from: str, date_to: str, time_from: str, time_to: str):
    cursor.execute("SELECT УИН_Площадки FROM Площадка WHERE Название = '%s'" % event_site)
    uin_event_site = cursor.fetchone()
    cursor.execute("SELECT Название FROM Мероприятие "
                   "WHERE УИН_Площадки = '%s' AND Тип_мероприятия = '%s' "
                   "AND Дата BETWEEN '%s' AND '%s' "
                   "AND Время BETWEEN '%s' AND '%s'"
                   % (uin_event_site[0], event_type, date_from, date_to, time_from, time_to))
    events = cursor.fetchall()
    event_list = [i[0] for i in events]
    return event_list


def tickets_list(event: str):
    cursor.execute("SELECT УИН_Мероприятия FROM Мероприятие WHERE Название = '%s'" % event)
    uin_event = cursor.fetchone()
    cursor.execute("SELECT Номер_билета FROM Билет WHERE УИН_Мероприятия = '%s' AND Забронирован = 0" % uin_event)
    tickets = cursor.fetchall()
    ticket_list = [i[0] for i in tickets]
    return ticket_list


def event_date_time(event: str):
    cursor.execute("SELECT Дата, Время FROM Мероприятие WHERE Название = '%s'" % event)
    date_time = cursor.fetchone()
    return date_time


def rows_list(event: str):
    cursor.execute("SELECT УИН_Мероприятия FROM Мероприятие WHERE Название = '%s'" % event)
    uin_event = cursor.fetchone()
    cursor.execute("SELECT Номер_ряда FROM Билет WHERE УИН_Мероприятия = '%s' AND Забронирован = 0" % uin_event[0])
    rows = cursor.fetchall()
    row_list = [str(i[0]) for i in rows]
    row_list = list(set(row_list))
    return row_list


def places_list(event: str, row: str):
    cursor.execute("SELECT УИН_Мероприятия FROM Мероприятие WHERE Название = '%s'" % event)
    uin_event = cursor.fetchone()
    cursor.execute("SELECT Номер_места FROM Билет WHERE УИН_Мероприятия = '%s' "
                   "AND Номер_ряда = '%s' AND Забронирован = 0" % (uin_event[0], int(row)))
    places = cursor.fetchall()
    place_list = [str(i[0]) for i in places]
    return place_list


def find_ticket(event: str, row: str, place: str):
    row = int(row)
    place = int(place)
    cursor.execute("SELECT УИН_Мероприятия FROM Мероприятие WHERE Название = '%s'" % event)
    uin_event = cursor.fetchone()
    cursor.execute("SELECT Номер_билета, Цена FROM Билет WHERE УИН_Мероприятия = '%s' "
                   "AND Номер_ряда = '%s' AND Номер_места = '%s'" % (uin_event[0], row, place))
    ticket = cursor.fetchone()
    return ticket


def ticket_reservation(ticket: int):
    cursor.execute("UPDATE Билет SET Забронирован = 1 WHERE Номер_билета = '%s'" % ticket)
    dbase.commit()


def ticket_unreserved(ticket: int):
    cursor.execute("UPDATE Билет SET Забронирован = 0 WHERE Номер_билета = '%s' AND УИН_Заказа IS NULL" % ticket)
    dbase.commit()


def buy_ticket(ticket: int, order: int):
    cursor.execute("UPDATE Билет SET УИН_Заказа = '%s' "
                   "WHERE Номер_билета = '%s' AND Забронирован = 1" % (order, ticket))
    dbase.commit()


def add_client(email: str, first_name: str, last_name: str):
    cursor.execute("INSERT INTO Клиент (Email) VALUES ('%s')" % email)
    if not first_name == '':
        cursor.execute("UPDATE Клиент SET Имя = '%s' WHERE Email = '%s'" % (first_name, email))
    if not last_name == '':
        cursor.execute("UPDATE Клиент SET Фамилия = '%s' WHERE Email = '%s'" % (last_name, email))
    dbase.commit()


def find_client(email: str):
    cursor.execute("SELECT УИН_Клиента FROM Клиент WHERE Email = '%s'" % email)
    uin_client = cursor.fetchone()
    if uin_client is None:
        return uin_client
    else:
        return uin_client[0]


def find_last_order(uin_client: int):
    cursor.execute("SELECT УИН_Заказа FROM Заказ WHERE УИН_Клиента = '%s'" % uin_client)
    uin_orders = cursor.fetchall()
    uin_orders = [i[0] for i in uin_orders]
    if uin_orders:
        return uin_orders.pop()
    else:
        return None


def add_order_for_old(uin_client: int):
    uin_order = find_last_order(uin_client) + 1
    cursor.execute("INSERT INTO Заказ (УИН_Заказа, УИН_Клиента, Оплачен) "
                   "VALUES ('%s', '%s', 0)" % (uin_order, uin_client))
    dbase.commit()


def add_order_for_new(uin_client: int):
    uin = str(uin_client) + '0000000001'
    uin_order = int(uin)
    cursor.execute("INSERT INTO Заказ (УИН_Заказа, УИН_Клиента, Оплачен) "
                   "VALUES ('%s', '%s', 0)" % (uin_order, uin_client))
    dbase.commit()


def pay_order(uin_order: int):
    cursor.execute("UPDATE Заказ SET Оплачен = 1 WHERE УИН_Заказа = '%s'" % uin_order)
    dbase.commit()


def get_ticket_info(uin_ticket: int):
    cursor.execute("SELECT Тип_мероприятия, Мероприятие.Название, Площадка.Название, "
                   "Дата, Время, Номер_ряда, Номер_места, Цена FROM Билет "
                   "JOIN Мероприятие ON Билет.УИН_Мероприятия = Мероприятие.УИН_Мероприятия "
                   "JOIN Площадка on Площадка.УИН_Площадки = Мероприятие.УИН_Площадки "
                   "WHERE Номер_билета = '%s'" % uin_ticket)
    ticket_info = cursor.fetchone()
    return ticket_info


def delete_order(uin_order: int):
    cursor.execute("DELETE FROM Заказ WHERE УИН_Заказа = '%s' AND Оплачен = 0" % uin_order)
    dbase.commit()


if __name__ == '__main__':
    print('Test')
    print(event_date_time('Звездные войны'))
    print(get_ticket_info(10010001))
