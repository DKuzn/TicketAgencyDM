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


if __name__ == '__main__':
    event_site = event_sites_list()
    event = events_list(event_site[0])
    print(tickets_list(event[0]))
    row = rows_list(event[0])
    print(places_list(event[0], row[0]))
    print(find_ticket(event[0], '1', '1'))
