import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        database="company_db",
        user="postgres",
        password="Gnanamuma@2003"
    )

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()

    print("Employees")
    for row in employees:
        print(row)

    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    print("\nProducts")
    for row in products:
        print(row)

except Exception as e:
    print("Error:", e)

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()