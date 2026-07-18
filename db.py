import psycopg2


def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="company_db",
        user="postgres",
        password="Gnanamuma@2003"
    )


def employees():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employees")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data


def products():
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

    print("\nProducts")
    for row in products():
        print(row)