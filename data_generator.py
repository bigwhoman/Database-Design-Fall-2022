import psycopg2
from faker import Faker
from random import randint
import datetime
import time

conn1 = psycopg2.connect(
    database="postgres", user='postgres', password='Hooman114', host='127.0.0.1', port='5433'
)
fake = Faker()
conn = conn1.cursor()
conn1.autocommit = True

for i in range(20):
    try:
        sql = f'''INSERT INTO Employee VALUES({i+1}, '{fake.name().split()[0]}', '{fake.sentence().split()[0]}', {10000*(i+1)}) '''
        conn.execute(sql)
    except:
        pass

for i in range(10):
    try:
        sql = f'''INSERT INTO TimeSchedule VALUES({i+1}, {(i+1)*5})'''
        conn.execute(sql)
    except:
        pass

for i in range(5):
    try:
        sql = f'''INSERT INTO SecurityLevel VALUES({i+1}, {(i+1)*5000})'''
        conn.execute(sql)
    except:
        pass

for i in range(10):
    try:
        sql = f'''INSERT INTO OptionalService VALUES('{fake.job()}', {(i+1)*1000})'''
        conn.execute(sql)
    except:
        pass

for i in range(10):
    try:
        sql = f'''INSERT INTO PriceGroup VALUES({(i+1)*10})'''
        conn.execute(sql)
    except:
        pass

    for i in range(10):
        try:
            sql = f'''INSERT INTO CommercialSuggest VALUES({(i+1)*3})'''
            conn.execute(sql)
        except:
            pass

    for i in range(20):
        try:
            sql = f'''INSERT INTO Customer VALUES({i+1}, '{fake.name().split()[0]}', '{fake.name().split()[0]}', '{fake.address()}', {randint(20, 40)},'{fake.simple_profile()["sex"]}', {(i+1)*1000})'''
            conn.execute(sql)
        except:
            pass

    for i in range(10):
        try:
            sql = f'''INSERT INTO BCustomer VALUES({i+21}, '{fake.name().split()[0]}', '{fake.name().split()[0]}', '{fake.address()}', {randint(20, 40)},'{fake.simple_profile()["sex"]}', {(i+1)*2500}, {randint(1, 10)*3})'''
            conn.execute(sql)
        except:
            pass

    for i in range(20):
        for j in range(5):
            try:
                sql = f'''INSERT INTO Account VALUES({i+1}, {j+1})'''
                conn.execute(sql)
            except:
                pass

    for i in range(6):
        try:
            sql = f'''INSERT INTO Salon VALUES({i+1}, {randint(1, 7)}, {5}, {randint(1, 10)}, {randint(1, 5)}, {randint(1, 20)})'''
            conn.execute(sql)
        except:
            pass

    for i in range(6):
        for j in range(5):
            try:
                sql = f'''INSERT INTO SafeBox VALUES({j+1}, {i+1}, {randint(1, 10)*10})'''
                conn.execute(sql)
            except:
                pass

    for i in range(20):
        try:
            ts = int(time.mktime(datetime.datetime.strptime(
                str(fake.date_time_this_year()), "%Y-%m-%d %H:%M:%S").timetuple()))
            sql = f'''INSERT INTO Contract VALUES({i+1}, {randint(1, 20)}, {randint(1, 5)}, {randint(1, 6)}, {randint(1, 10)}, '{fake.date_time_this_year()}', {randint(1, 10)*5000})'''
            conn.execute(sql)
        except:
            pass

for i in range(20):
    try:
        sql = f'''INSERT INTO Report VALUES({i+1}, {randint(1, 20)}, {randint(1, 20)}, '{fake.date_this_year()}')'''
        conn.execute(sql)
    except:
        pass

conn1.close()
