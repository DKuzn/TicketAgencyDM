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

import psycopg2

dbase = psycopg2.connect(
    host='localhost',  # ip-address to server with PostgresQL
    database='ticketagencydb',
    user='postgres',
    password='mypass',
    port='5432')

cursor = dbase.cursor()


def event_site_types_list():
    cursor.execute('SELECT main."Площадка"."Тип" FROM main."Площадка"')
    event_site_types = cursor.fetchall()
    event_site_type_list = [i[0] for i in event_site_types]
    event_site_type_list = list(set(event_site_type_list))
    return event_site_type_list


def event_sites_list(event_site_type: str):
    cursor.execute('SELECT main."Площадка"."Название" FROM main."Площадка" '
                   'WHERE main."Площадка"."Тип" = %s', (event_site_type,))
    event_sites = cursor.fetchall()
    event_site_list = [i[0] for i in event_sites]
    return event_site_list


def event_types_list(event_site: str, date_from: str, date_to: str, time_from: str, time_to: str):
    cursor.execute('SELECT main."Площадка"."УИН_Площадки" FROM main."Площадка" '
                   'WHERE main."Площадка"."Название" = %s', (event_site,))
    uin_event_site = cursor.fetchone()
    cursor.execute('SELECT main."Мероприятие"."Тип_мероприятия" FROM main."Мероприятие" '
                   'WHERE main."Мероприятие"."УИН_Площадки" = %s AND main."Мероприятие"."Дата" BETWEEN %s AND %s '
                   'AND main."Мероприятие"."Время" BETWEEN %s AND %s',
                   (uin_event_site[0], date_from, date_to, time_from, time_to,))
    event_types = cursor.fetchall()
    event_type_list = [i[0] for i in event_types]
    event_type_list = list(set(event_type_list))
    return event_type_list


def events_list(event_site: str, event_type: str, date_from: str, date_to: str, time_from: str, time_to: str):
    cursor.execute('SELECT main."Площадка"."УИН_Площадки" FROM main."Площадка" '
                   'WHERE main."Площадка"."Название" = %s', (event_site,))
    uin_event_site = cursor.fetchone()
    cursor.execute('SELECT main."Мероприятие"."Название" FROM main."Мероприятие" '
                   'WHERE main."Мероприятие"."УИН_Площадки" = %s AND main."Мероприятие"."Тип_мероприятия" = %s '
                   'AND main."Мероприятие"."Дата" BETWEEN %s AND %s '
                   'AND main."Мероприятие"."Время" BETWEEN %s AND %s',
                   (uin_event_site[0], event_type, date_from, date_to, time_from, time_to,))
    events = cursor.fetchall()
    event_list = [i[0] for i in events]
    return event_list


def available_tickets_list(event: str):
    cursor.execute('SELECT main."Мероприятие"."УИН_Мероприятия" FROM main."Мероприятие" '
                   'WHERE main."Мероприятие"."Название" = %s', (event,))
    uin_event = cursor.fetchone()
    cursor.execute('SELECT main."Билет"."Номер_билета" FROM main."Билет" '
                   'WHERE main."Билет"."УИН_Мероприятия" = %s AND main."Билет"."Забронирован" = 0', (uin_event,))
    tickets = cursor.fetchall()
    ticket_list = [i[0] for i in tickets]
    return ticket_list


def tickets_list(event: str):
    cursor.execute('SELECT main."Мероприятие"."УИН_Мероприятия" FROM main."Мероприятие" '
                   'WHERE main."Мероприятие"."Название" = %s', (event,))
    uin_event = cursor.fetchone()
    cursor.execute('SELECT main."Билет"."Номер_билета" FROM main."Билет" '
                   'WHERE main."Билет"."УИН_Мероприятия" = %s', (uin_event,))
    tickets = cursor.fetchall()
    ticket_list = [i[0] for i in tickets]
    return ticket_list


def sold_tickets_list(event: str):
    cursor.execute('SELECT main."Мероприятие"."УИН_Мероприятия" FROM main."Мероприятие" '
                   'WHERE main."Мероприятие"."Название" = %s', (event,))
    uin_event = cursor.fetchone()
    cursor.execute('SELECT main."Билет"."Номер_билета" FROM main."Билет" '
                   'WHERE main."Билет"."УИН_Мероприятия" = %s AND "УИН_Заказа" IS NOT NULL', (uin_event,))
    tickets = cursor.fetchall()
    ticket_list = [i[0] for i in tickets]
    return ticket_list


def event_date_time(event: str):
    cursor.execute('SELECT main."Мероприятие"."Дата", main."Мероприятие"."Время" '
                   'FROM main."Мероприятие" WHERE main."Мероприятие"."Название" = %s', (event,))
    date_time = cursor.fetchone()
    return date_time


def rows_list(event: str):
    cursor.execute('SELECT main."Мероприятие"."УИН_Мероприятия" '
                   'FROM main."Мероприятие" WHERE main."Мероприятие"."Название" = %s', (event,))
    uin_event = cursor.fetchone()
    cursor.execute('SELECT main."Билет"."Номер_ряда" FROM main."Билет" '
                   'WHERE main."Билет"."УИН_Мероприятия" = %s AND main."Билет"."Забронирован" = 0', (uin_event[0],))
    rows = cursor.fetchall()
    row_list = [i[0] for i in rows]
    row_list = sorted(list(set(row_list)))
    row_list = ([str(i) for i in row_list])
    return row_list


def places_list(event: str, row: str):
    cursor.execute('SELECT main."Мероприятие"."УИН_Мероприятия" '
                   'FROM main."Мероприятие" WHERE main."Мероприятие"."Название" = %s', (event,))
    uin_event = cursor.fetchone()
    cursor.execute('SELECT main."Билет"."Номер_места" FROM main."Билет" WHERE main."Билет"."УИН_Мероприятия" = %s '
                   'AND main."Билет"."Номер_ряда" = %s AND main."Билет"."Забронирован" = 0', (uin_event[0], int(row),))
    places = cursor.fetchall()
    place_list = [str(i[0]) for i in places]
    return place_list


def find_ticket(event: str, row: str, place: str):
    row = int(row)
    place = int(place)
    cursor.execute('SELECT main."Мероприятие"."УИН_Мероприятия" '
                   'FROM main."Мероприятие" WHERE main."Мероприятие"."Название" = %s', (event,))
    uin_event = cursor.fetchone()
    cursor.execute('SELECT main."Билет"."Номер_билета", main."Билет"."Цена" '
                   'FROM main."Билет" WHERE main."Билет"."УИН_Мероприятия" = %s '
                   'AND main."Билет"."Номер_ряда" = %s AND main."Билет"."Номер_места" = %s',
                   (uin_event[0], row, place,))
    ticket = cursor.fetchone()
    return ticket


def ticket_reservation(ticket: int):
    cursor.execute('UPDATE main."Билет" SET "Забронирован" = 1 '
                   'WHERE main."Билет"."Номер_билета" = %s', (ticket,))
    dbase.commit()


def ticket_unreserved(ticket: int):
    cursor.execute('UPDATE main."Билет" SET "Забронирован" = 0 '
                   'WHERE main."Билет"."Номер_билета" = %s AND main."Билет"."УИН_Заказа" IS NULL', (ticket,))
    dbase.commit()


def buy_ticket(ticket: int, order: int):
    cursor.execute('UPDATE main."Билет" SET "УИН_Заказа" = %s '
                   'WHERE main."Билет"."Номер_билета" = %s AND main."Билет"."Забронирован" = 1', (order, ticket,))
    dbase.commit()


def add_client(email: str, first_name: str, last_name: str):
    cursor.execute('INSERT INTO main."Клиент" ("Email") VALUES (%s)', (email,))
    if not first_name == '':
        cursor.execute('UPDATE main."Клиент" SET "Имя" = %s '
                       'WHERE main."Клиент"."Email" = %s', (first_name, email,))
    if not last_name == '':
        cursor.execute('UPDATE main."Клиент" SET "Фамилия" = %s '
                       'WHERE main."Клиент"."Email" = %s', (last_name, email,))
    dbase.commit()


def find_client(email: str):
    cursor.execute('SELECT main."Клиент"."УИН_Клиента" FROM main."Клиент" '
                   'WHERE main."Клиент"."Email" = %s', (email,))
    uin_client = cursor.fetchone()
    if uin_client is None:
        return uin_client
    else:
        return uin_client[0]


def find_last_order(uin_client: int):
    cursor.execute('SELECT main."Заказ"."УИН_Заказа" FROM main."Заказ" '
                   'WHERE main."Заказ"."УИН_Клиента" = %s', (uin_client,))
    uin_orders = cursor.fetchall()
    uin_orders = [i[0] for i in uin_orders]
    if uin_orders:
        return uin_orders.pop()
    else:
        return None


def add_order(uin_client: int):
    cursor.execute('INSERT INTO main."Заказ"("УИН_Клиента", "Оплачен") '
                   'VALUES (%s, 0)', (uin_client,))
    dbase.commit()


def pay_order(uin_order: int):
    cursor.execute('UPDATE main."Заказ" SET "Оплачен" = 1 '
                   'WHERE main."Заказ"."УИН_Заказа" = %s', (uin_order,))
    dbase.commit()


def get_ticket_info(uin_ticket: int):
    cursor.execute('SELECT main."Мероприятие"."Тип_мероприятия", '
                   'main."Мероприятие"."Название", main."Площадка"."Название", '
                   'main."Мероприятие"."Дата", main."Мероприятие"."Время", '
                   'main."Билет"."Номер_ряда", main."Билет"."Номер_места", main."Билет"."Цена" FROM main."Билет" '
                   'JOIN main."Мероприятие" ON main."Билет"."УИН_Мероприятия" = main."Мероприятие"."УИН_Мероприятия" '
                   'JOIN main."Площадка" ON main."Площадка"."УИН_Площадки" = main."Мероприятие"."УИН_Площадки" '
                   'WHERE main."Билет"."Номер_билета" = %s', (uin_ticket,))
    ticket_info = cursor.fetchone()
    return ticket_info


def get_ticket_info_form(uin_ticket: int):
    cursor.execute('SELECT main."Мероприятие"."Тип_мероприятия", '
                   'main."Мероприятие"."Название", main."Площадка"."Название", '
                   'main."Мероприятие"."Дата", main."Мероприятие"."Время", '
                   'main."Билет"."Номер_ряда", main."Билет"."Номер_места", '
                   'main."Билет"."Цена", main."Клиент"."Email" FROM main."Билет" '
                   'JOIN main."Мероприятие" ON main."Билет"."УИН_Мероприятия" = main."Мероприятие"."УИН_Мероприятия" '
                   'JOIN main."Площадка" ON main."Площадка"."УИН_Площадки" = main."Мероприятие"."УИН_Площадки" '
                   'JOIN main."Заказ" ON main."Билет"."УИН_Заказа" = main."Заказ"."УИН_Заказа" '
                   'JOIN main."Клиент" ON main."Клиент"."УИН_Клиента" = main."Заказ"."УИН_Клиента"'
                   'WHERE main."Билет"."Номер_билета" = %s', (uin_ticket,))
    ticket_info = cursor.fetchone()
    return ticket_info


def delete_order(uin_order: int):
    cursor.execute('DELETE FROM main."Заказ" WHERE main."Заказ"."УИН_Заказа" = %s '
                   'AND main."Заказ"."Оплачен" = 0', (uin_order,))
    dbase.commit()


def list_tables():
    cursor.execute(f'SELECT table_name FROM information_schema.tables WHERE table_schema = \'main\'')
    tables = cursor.fetchall()
    tables = [i[0] for i in tables]
    return tables


def get_table(table_name: str):
    cursor.execute(f'SELECT * FROM main.{table_name}')
    columns = tuple(desc[0] for desc in cursor.description)
    content = cursor.fetchall()
    content.insert(0, columns)
    return content


def add_event_site(event_site: str, event_site_type: str):
    cursor.execute('INSERT INTO main."Площадка"("Тип", "Название")  VALUES (%s, %s)', (event_site_type, event_site,))
    dbase.commit()


def add_event(event_site: str, event_site_type: str, event_type: str, event_name: str, event_date: str, event_time: str):
    cursor.execute('SELECT main."Площадка"."УИН_Площадки" FROM main."Площадка" '
                   'WHERE main."Площадка"."Название" = %s AND main."Площадка"."Тип" = %s', (event_site, event_site_type,))
    uin_event_site = cursor.fetchone()
    cursor.execute('INSERT INTO main."Мероприятие"("УИН_Площадки", '
                   '"Название", "Тип_мероприятия", "Дата", "Время") '
                   'VALUES (%s, %s, %s, %s, %s)', (uin_event_site[0], event_name, event_type, event_date, event_time))
    dbase.commit()


def add_ticket(event_site: str, event_site_type: str, event_type: str, event_name: str, row: int, place: int, price: float):
    cursor.execute('SELECT main."Площадка"."УИН_Площадки" FROM main."Площадка" '
                   'WHERE main."Площадка"."Название" = %s AND main."Площадка"."Тип" = %s',
                   (event_site, event_site_type,))
    uin_event_site = cursor.fetchone()
    cursor.execute('SELECT main."Мероприятие"."УИН_Мероприятия" FROM main."Мероприятие" '
                   'WHERE main."Мероприятие"."УИН_Площадки" = %s AND main."Мероприятие"."Тип_мероприятия" = %s '
                   'AND main."Мероприятие"."Название" = %s', (uin_event_site[0], event_type, event_name,))
    uin_event = cursor.fetchone()
    cursor.execute('INSERT INTO main."Билет"("УИН_Мероприятия", "Номер_ряда", '
                   '"Номер_места", "Цена", "Забронирован") VALUES (%s, %s, %s, %s, 0)',
                   (uin_event[0], row, place, price,))
    dbase.commit()


if __name__ == '__main__':
    print('Test')
    print(event_date_time('Звездные войны'))
    print(get_ticket_info(1))
    print(list_tables())
    print(get_table('Площадка'))
