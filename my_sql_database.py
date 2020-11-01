import sqlite3
import os.path


def initial_setup():
    conn = sqlite3.connect('my_database.db')
    c = conn.cursor()
    c.execute("DROP TABLE users")
    c.execute("DROP TABLE ca_param")
    c.execute("CREATE TABLE users (username text PRIMARY KEY, see_all integer)")
    c.execute("""CREATE TABLE ca_param (
                no_cells integer,
                generations integer,
                size_x integer,
                size_y integer,
                infection_radius integer,
                no_infected integer,
                recovered_can_be_infected integer,
                days_until_recovered integer,
                use_immunity integer,
                days_of_immunity integer    
                )""")
    conn.commit()

    # if not os.path.isfile('my_database.db'):
    #     # print("Creating new table")
    #     new_table()
    #
    # if reset:
    #     conn = sqlite3.connect('my_database.db')
    #     c = conn.cursor()
    #
    #     new_table()


def enter_username(in_user):
    conn = sqlite3.connect('my_database.db')
    c = conn.cursor()
    # c.execute("INSERT INTO users VALUES (:username, :see_all) ON DUPLICATE KEY UPDATE id=id",
    #           {'username': in_user, 'see_all': 0})
    c.execute("INSERT OR IGNORE INTO users VALUES (:username, :see_all)",
              {'username': in_user, 'see_all': 0})  # don't add if duplicate username
    conn.commit()


# initial_setup()

# enter_username("chase")


# conn = sqlite3.connect('my_database.db')
# c = conn.cursor()
#
# c.execute("SELECT * FROM users")
# print(c.fetchall())
