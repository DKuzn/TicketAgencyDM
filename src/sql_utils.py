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


if __name__ == '__main__':
    event = event_sites_list()
    print(events_list(event[1]))
