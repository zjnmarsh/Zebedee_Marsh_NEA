import sqlite3
import os.path


def initial_setup():
    """Sets up clean database with users table and ca_param table. Users table contains username and
    whether user can see all parameters previously used, and ca_param table contains the history of
    parameters used as well as the user who executed them"""
    conn = sqlite3.connect('my_database.db')
    c = conn.cursor()
    # c.execute("DROP TABLE users")
    # c.execute("DROP TABLE ca_param")
    c.execute("CREATE TABLE users (username text PRIMARY KEY, see_all integer)")

    c.execute("""CREATE TABLE ca_param (
                user string,
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
    c.execute("INSERT INTO users VALUES (:username, :see_all)", {'username': 'admin', 'see_all': 1})

    c.execute("""CREATE TABLE sir_param (
                user string,
                sus0 integer,
                inf0 integer,
                rec0 integer,
                beta integer,
                gamma integer,
                time integer
                )""")

    conn.commit()
    conn.close()


def enter_username(in_user):
    """If new username entered, it will create a record in the users table for that user, if username
    entered already exists nothing happens. Username is returned"""
    conn = sqlite3.connect('my_database.db')
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO users VALUES (:username, :see_all)",
              {'username': in_user, 'see_all': 0})  # don't add if duplicate username
    conn.commit()
    conn.close()
    return in_user


def ca_enter_param(in_user, up):
    """Inserts new parameters entered by the user into the CA parameter database"""
    conn = sqlite3.connect('my_database.db')
    c = conn.cursor()
    c.execute("""INSERT INTO ca_param VALUES (:user, :no_cells, :generations, :size_x, :size_y,
                                            :infection_radius, :no_infected, :recovered_can_be_infected,
                                            :days_until_recovered, :use_immunity, :days_of_immunity)""",
              {'user': in_user, 'no_cells': up[0], 'generations': up[1], 'size_x': up[2], 'size_y': up[3],
               'infection_radius': up[4], 'no_infected': up[5], 'recovered_can_be_infected': up[6],
               'days_until_recovered': up[7], 'use_immunity': up[8], 'days_of_immunity': up[9]})
    conn.commit()
    conn.close()


def ca_return_history(in_user):
    """Returns entered parameter history depending on current user"""
    conn = sqlite3.connect('my_database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM ca_param WHERE user=:curr_user", {'curr_user': in_user})
    # conn.close()
    return c.fetchall()


def sir_enter_param(in_user, up):
    """Inters new parameters entered by the user into the SIR parameter database"""
    conn = sqlite3.connect('my_database.db')
    c = conn.cursor()
    c.execute("""INSERT INTO sir_param VALUES (:user, :sus0, :inf0, :rec0, :beta, :gamma, :time)""",
              {'user': in_user, 'sus0': up[0], 'inf0': up[1], 'rec0': up[2], 'beta': up[3], 'gamma': up[4], 'time': up[5]
               })
    conn.commit()
    conn.close()

def sir_return_history(in_user):
    conn = sqlite3.connect('my_database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM sir_param WHERE user=:curr_user", {'curr_user':in_user})
    return c.fetchall()

# initial_setup()

# enter_username("Alice")

# conn = sqlite3.connect('my_database.db')
# c = conn.cursor()
#
# c.execute("SELECT * FROM users")
# print(c.fetchall())

# ca_enter_param('chase', [10, 25, 50, 50, 3, 3, True, 5, True, 5])
# ca_enter_param('chase', [1, 2, 5, 5, 1, 3, True, 5, True, 5])
# ca_enter_param('Alice', [33, 5, 80, 30, 3, 3, True, 5, True, 5])
# c.execute("SELECT * FROM ca_param")
# print(c.fetchall())

