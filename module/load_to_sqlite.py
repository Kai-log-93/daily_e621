import sqlite3
from sqlite3.dbapi2 import Cursor


def load_to_sqlite(images_key_info):
    # load to e621today.db
    connection = sqlite3.connect('e621today.db')
    cursor = connection.cursor()

    # create if not exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS E621today
        (Width INT, Height INT, Ext TEXT, Url TEXT)''')

    # clear yesterday data before load new
    cursor.execute('''DELETE FROM E621today''')
    #only for print
    records = cursor.execute('''SELECT * FROM E621today''')
    print('from database: ')
    
    
    # load data for today
    cursor.executemany('''INSERT INTO E621today VALUES (?,?,?,?)''', images_key_info)

    # print all
    records = cursor.execute('''SELECT * FROM E621today''')

    print('from database: ')
    print(cursor.fetchall())

    # must close the dataset after manipulation
    connection.commit()
    connection.close()
