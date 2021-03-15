import psycopg2


def get_cursor(database: str, user: str, password: str, host: str, port: str = '5432'):
    dbase = psycopg2.connect(
        database=database,
        user=user,
        password=password,
        host=host,
        port=port)
    dbase.autocommit = True
    cursor = dbase.cursor()
    return cursor


def get_database(host: str = 'localhost'):
    conn = get_cursor(database='postgres',
                      user='postgres',
                      password='mypass',
                      host=host)

    conn.execute('create database ticketagencydb;')

    conn = get_cursor(database='ticketagencydb',
                      user='postgres',
                      password='mypass',
                      host=host)

    conn.execute('create schema main;')

    conn.execute("""
    create table main."Площадка"
    (
        "УИН_Площадки" serial not null
            constraint площадка_pk
                primary key,
        "Тип"          text    not null,
        "Название"     text    not null,
        unique         ("Тип", "Название")
    );
    
    alter table main."Площадка"
        owner to postgres;
    
    create unique index площадка_уин_площадки_uindex
        on main."Площадка" ("УИН_Площадки");
    
    create table main."Мероприятие"
    (
        "УИН_Мероприятия" serial not null
            constraint мероприятие_pk
                primary key,
        "УИН_Площадки"    integer not null
            constraint мероприятие_площадка_уин_площадки
                references main."Площадка",
        "Название"        text    not null,
        "Тип_мероприятия" text    not null,
        "Дата"            text    not null,
        "Время"           text    not null,
        unique            ("Название", "Тип_мероприятия")
    );
    
    alter table main."Мероприятие"
        owner to postgres;
    
    create unique index мероприятие_уин_мероприятия_uindex
        on main."Мероприятие" ("УИН_Мероприятия");
    
    create table main."Клиент"
    (
        "УИН_Клиента" serial not null
            constraint клиент_pk
                primary key,
        "Email"       text   not null,
        "Имя"         text,
        "Фамилия"     text
    );
    
    alter table main."Клиент"
        owner to postgres;
    
    create unique index клиент_email_uindex
        on main."Клиент" ("Email");
    
    create unique index клиент_уин_клиента_uindex
        on main."Клиент" ("УИН_Клиента");
    
    create table main."Заказ"
    (
        "УИН_Заказа"  serial not null
            constraint заказ_pk
                primary key,
        "УИН_Клиента" integer not null
            constraint заказ_клиент_уин_клиента_fk
                references main."Клиент",
        "Оплачен"     integer not null
    );
    
    alter table main."Заказ"
        owner to postgres;
    
    create unique index заказ_уин_заказа_uindex
        on main."Заказ" ("УИН_Заказа");
    
    create table main."Билет"
    (
        "Номер_билета"    serial not null
            constraint билет_pk
                primary key,
        "УИН_Мероприятия" integer not null
            constraint билет_мероприятие_уин_мероприятия
                references main."Мероприятие",
        "Номер_ряда"      integer not null,
        "Номер_места"     integer not null,
        "Цена"            real    not null,
        "Забронирован"    integer not null,
        "УИН_Заказа"      integer
            constraint билет_заказ_уин_заказа_fk
                references main."Заказ"
    );
    
    alter table main."Билет"
        owner to postgres;
    
    create unique index билет_номер_билета_uindex
        on main."Билет" ("Номер_билета");
    
    """)


if __name__ == '__main__':
    get_database()
