import psycopg2
import time

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="company_db",
        user="postgres",
        password="Gnanamuma@2003"
    )


def employees():
    time.sleep(1)
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employees")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data


def products():
    time.sleep(1)
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data


if __name__ == "__main__":

    print("Employees")
    for row in employees():
        print(row)

    print("Products")
    for row in products():
        print(row)