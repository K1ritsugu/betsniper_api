import sqlite3


def create_table():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS events (
        id INTEGER PRIMARY KEY,
        type_bet TEXT,
        bookmaker TEXT,
        link TEXT,
        coef INTEGER,
        match_name TEXT,
        profit TEXT,
        first_time TEXT,
        sport TEXT
    )''')

    conn.commit()
    cursor.close()
    conn.close()


def insert_new_event(*args):
    if len(args) != 9:
        return {"message": "incorrect number of arguments", "success": False}

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    if args[-1] == 0:
        cursor.execute("DELETE FROM events")

    cursor.execute('''INSERT INTO events (type_bet, 
                       bookmaker, 
                       link, 
                       coef, 
                       match_name, 
                       profit, 
                       first_time, 
                       sport) VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                   args[:-1])

    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "success insert", "success": True}

def get_all_events():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM events")

    events = cursor.fetchall()
    count_events = len(events)

    if count_events == 1:
        events = events[0]

    dict_key = ["type_bet", "bookmaker", "link", "coef", "match_name", "profit", "first_time", "sport"]
    dict_events = []
    print(events)
    for event in events:
        event = event[1:]

        # Создаем словарь, сопоставляя ключи из dict_key со значениями из event
        event_dict = dict(zip(dict_key, event))

        # Добавляем словарь в список dict_events
        dict_events.append(event_dict)

    cursor.close()
    conn.close()

    return dict_events


create_table()
