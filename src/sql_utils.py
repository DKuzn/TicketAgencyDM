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


def event_sites_list():
    cursor.execute("SELECT Название FROM Площадка")
    event_sites = cursor.fetchall()
    event_site_list = [i[0] for i in event_sites]
    return event_site_list


def events_list(event_site: str):
    cursor.execute("SELECT УИН_Площадки FROM Площадка WHERE Название = '%s'" % event_site)
    uin_event_site = cursor.fetchone()
    cursor.execute("SELECT Название FROM Мероприятие WHERE УИН_Площадки = '%s'" % uin_event_site)
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
    cursor.execute("UPDATE Билет SET Забронирован = 0 WHERE Номер_билета = '%s'" % ticket)
    dbase.commit()


def buy_ticket(ticket: int, order: int):
    cursor.execute("UPDATE Билет SET УИН_Заказа = '%s' "
                   "WHERE Номер_билета = '%s' AND Забронирован = 1" % (order, ticket))
    dbase.commit()


def add_client(email: str, first_name: str = None, last_name: str = None):
    cursor.execute("INSERT INTO Клиент (Email) VALUES ('%s')" % email)
    if first_name is not None:
        cursor.execute("UPDATE Клиент SET Имя = '%s' WHERE Email = '%s'" % (first_name, email))
    if last_name is not None:
        cursor.execute("UPDATE Клиент SET Фамилия = '%s' WHERE Email = '%s'" % (last_name, email))
    dbase.commit()


if __name__ == '__main__':
    event_site = event_sites_list()
    event = events_list(event_site[0])
    print(tickets_list(event[0]))
    row = rows_list(event[0])
    print(places_list(event[0], row[0]))
    print(find_ticket(event[0], '1', '1'))
