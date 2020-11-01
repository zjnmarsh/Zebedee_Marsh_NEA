import sqlite3
from test_functions.sqlite_test.employee import Employee

# https://www.youtube.com/watch?v=pd-0G0MigUA

# connects to database
# conn = sqlite3.connect('user_test.db')

conn = sqlite3.connect(':memory:')  # when in memory

# cursor allows us to execute commands
c = conn.cursor()

# c.execute("""DROP TABLE employees""")

# creating database
c.execute("""CREATE TABLE employees (
            first text,
            last text,
            pay integer
            )""")


def insert_emp(emp):
    with conn:  # no need to commit anytime
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)",
                  {'first': emp.first, 'last': emp.last, 'pay': emp.pay})


def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last",
              {'last': lastname})  # select statements don't need to be committed
    return c.fetchall()


def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                    WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': pay})


def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first = :first AND last = :last", {'first': emp.first, 'last': emp.last})


emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Doe', 90000)

insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emps_by_name('Doe')
print(emps)

update_pay(emp_2, 9500)
remove_emp(emp_1)

emps = get_emps_by_name('Doe')
print(emps)


# # inserting data into database
# c.execute("INSERT INTO employees VALUES ('Mary', 'Smith', 70000)")
# c.execute("INSERT INTO employees VALUES ('Mike', 'Smith', 70000)")
# # inserting from class object
# c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay))
# c.execute("INSERT INTO employees VALUES (:first, :last, :pay)",
#           {'first': emp_2.first, 'last': emp_2.last, 'pay': emp_2.pay})

# conn.commit()

# c.execute("SELECT * FROM employees WHERE last=:last", {'last': 'Doe'})
# print(c.fetchall())

# c.execute("DELETE FROM employees WHERE last='Smith'")

# conn.commit()

# c.execute("SELECT * FROM employees WHERE last='Smith'")

# gets next row in results and only returns that row; no rows returns none
# print(c.fetchone())

# takes argument of number and returns that number of rows as list; no row
# print(c.fetchmany(3))

# gets remaining rows
# print(c.fetchall())

# commits current transaction
# conn.commit()

conn.close()
