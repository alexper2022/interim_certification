import sqlite3

db = sqlite3.connect('database.lite')
cur = db.cursor()

# Создание таблицы
cur.execute("""CREATE TABLE notebook (
            note_title text,
            note_body text,
            note_datetime text NOT NULL
            )""")
# Добавление данных
cur.execute("""
INSERT INTO notebook (note_title, note_body, note_datetime) VALUES
('01 note title 01', '01 note body 01 01 note body 01 01 note body 01 01 note body 01', '2023-01-23 18:03:19.353077'),
('02 note title 02', '02 note body 02 02 note body 02 02 note body 02 02 note body 02', '2023-02-23 18:03:19.359109'),
('03 note title 03', '03 note body 03 03 note body 03 03 note body 03 03 note body 03', '2023-03-23 18:03:19.365086'),
('04 note title 04', '04 note body 04 04 note body 04 04 note body 04 04 note body 04', '2023-04-23 18:03:19.371226'),
('05 note title 05', '05 note body 05 05 note body 05 05 note body 05 05 note body 05', '2023-05-23 18:03:19.377135'),
('06 note title 06', '06 note body 06 06 note body 06 06 note body 06 06 note body 06', '2023-06-23 18:03:19.382656'),
('07 note title 07', '07 note body 07 07 note body 07 07 note body 07 07 note body 07', '2023-07-23 18:03:19.388227'),
('08 note title 08', '08 note body 08 08 note body 08 08 note body 08 08 note body 08', '2023-08-23 18:03:19.393895'),
('09 note title 09', '09 note body 09 09 note body 09 09 note body 09 09 note body 09', '2023-09-23 18:03:19.400015'),
('10 note title 10', '10 note body 10 10 note body 10 10 note body 10 10 note body 10', '2023-10-23 18:03:19.406060'),
('11 note title 11', '11 note body 11 11 note body 11 11 note body 11 11 note body 11', '2023-11-23 18:03:19.411346'),
('12 note title 12', '12 note body 12 12 note body 12 12 note body 12 12 note body 12', '2023-12-23 18:03:19.417445'),
('01 note title 01', '01 note body 01 01 note body 01 01 note body 01 01 note body 01', '2023-01-23 18:03:19.353077'),
('02 note title 02', '02 note body 02 02 note body 02 02 note body 02 02 note body 02', '2023-02-23 18:03:19.359109'),
('03 note title 03', '03 note body 03 03 note body 03 03 note body 03 03 note body 03', '2023-03-23 18:03:19.365086'),
('04 note title 04', '04 note body 04 04 note body 04 04 note body 04 04 note body 04', '2023-04-23 18:03:19.371226'),
('05 note title 05', '05 note body 05 05 note body 05 05 note body 05 05 note body 05', '2023-05-23 18:03:19.377135'),
('06 note title 06', '06 note body 06 06 note body 06 06 note body 06 06 note body 06', '2023-06-23 18:03:19.382656'),
('07 note title 07', '07 note body 07 07 note body 07 07 note body 07 07 note body 07', '2023-07-23 18:03:19.388227'),
('08 note title 08', '08 note body 08 08 note body 08 08 note body 08 08 note body 08', '2023-08-23 18:03:19.393895'),
('09 note title 09', '09 note body 09 09 note body 09 09 note body 09 09 note body 09', '2023-09-23 18:03:19.400015'),
('10 note title 10', '10 note body 10 10 note body 10 10 note body 10 10 note body 10', '2023-10-23 18:03:19.406060'),
('11 note title 11', '11 note body 11 11 note body 11 11 note body 11 11 note body 11', '2023-11-23 18:03:19.411346'),
('12 note title 12', '12 note body 12 12 note body 12 12 note body 12 12 note body 12', '2023-12-23 18:03:19.417445')
""")
# Применяем изменения и закрываем базу
db.commit()
db.close()
