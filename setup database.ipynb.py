#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3
print(sqlite3.sqlite_version)


# In[2]:


def create_database():
    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()

    print("Database created successfully!")

    # Create Employees table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Employees (
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        Name TEXT NOT NULL,
                        Department TEXT NOT NULL,
                        Salary INTEGER NOT NULL,
                        Hire_Date TEXT NOT NULL
                    )''')

    # Create Departments table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Departments (
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        Name TEXT NOT NULL,
                        Manager TEXT NOT NULL
                    )''')

    # Insert sample data
    cursor.executemany('''INSERT INTO Employees (Name, Department, Salary, Hire_Date) VALUES (?, ?, ?, ?)''', [
        ("Alice", "Sales", 50000, "2021-01-15"),
        ("Bob", "Engineering", 70000, "2020-06-10"),
        ("Charlie", "Marketing", 60000, "2022-03-20"),
    ])

    cursor.executemany('''INSERT INTO Departments (Name, Manager) VALUES (?, ?)''', [
        ("Sales", "Alice"),
        ("Engineering", "Bob"),
        ("Marketing", "Charlie"),
    ])

    conn.commit()

    # Fetch Employees Data
    cursor.execute("SELECT * FROM Employees")
    employees = cursor.fetchall()
    print("Employees:\n", employees)

    # Fetch Departments Data
    cursor.execute("SELECT * FROM Departments")
    departments = cursor.fetchall()
    print("\nDepartments:\n", departments)


    
    conn.close()
    print("Database setup completed!")

if __name__ == "__main__":
    create_database()

