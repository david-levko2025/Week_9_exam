from typing import List, Dict, Any
from db import get_db_connection


def get_customers_by_credit_limit_range():
    conn = get_db_connection()
    cursor = conn.cursor()

    sql_query = """
    SELECT 
    customerName,
    creditLimit
    FROM customers
    WHERE creditLimit < 10000
    OR creditLimit > 100000
        """
    cursor.execute(sql_query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def get_orders_with_null_comments():
    conn = get_db_connection()
    cursor = conn.cursor()

    sql_query = """
    SELECT 
    orderNumber,
    comments
    FROM orders
    WHERE comments IS NOT NULL
    ORDER BY requiredDate
        """
    cursor.execute(sql_query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def get_first_5_customers():
    conn = get_db_connection()
    cursor = conn.cursor()
    sql_query = """
    SELECT 
    customerName,
    contactFirstName,
    contactLastName
    FROM customers
    ORDER BY contactLastName
    LIMIT 5
    """
    cursor.execute(sql_query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def get_payments_total_and_average():
    conn = get_db_connection()
    cursor = conn.cursor()

    sql_query = """
    SELECT
    SUM(amount) AS sumOfPayments,
    AVG(amount) AS avgOfPayments,
    MIN(amount) AS minOfPayments,
    MAX(amount) AS maxOfPayments
    FROM payments
    """
    cursor.execute(sql_query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def get_employees_with_office_phone():
    conn = get_db_connection()
    cursor = conn.cursor()
    sql_query = """
    SELECT 
    employees.firstName,
    employees.lastName,
    offices.phone
    FROM employees
    INNER JOIN offices
    ON offices.officeCode = employees.officeCode
    """
    cursor.execute(sql_query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def get_customers_with_shipping_dates():
    conn = get_db_connection()
    cursor = conn.cursor()
    sql_query = """
    SELECT 
    customers.customerName,
    orders.shippedDate
    FROM customers
    INNER JOIN orders
    ON orders.customerNumber = customers.customerNumber
    """
    cursor.execute(sql_query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def get_customer_quantity_per_order():
    conn = get_db_connection()
    cursor = conn.cursor()

    sql_query = """
    SELECT 
    customers.customerName,
    orderdetails.quantityOrdered
    FROM customers
    INNER JOIN orders
    ON customers.customerNumber = orders.customerNumber
    INNER JOIN orderdetails
    ON orderdetails.orderNumber = orders.orderNumber
    ORDER BY customerName
    """
    cursor.execute(sql_query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def get_customers_payments_by_lastname_pattern(pattern: str = "son"):
    conn = get_db_connection()
    cursor = conn.cursor()
    sql_query = """
    SELECT 
    customers.customerName,
    customers.contactFirstName,
    customers.contactLastName,
    SUM(payments.amount) 
    FROM customers
    INNER JOIN payments
    ON customers.customerNumber = payments.customerNumber
    WHERE customers.contactFirstName LIKE '%Mu%' 
    OR customers.contactFirstName LIKE '%ly%'
    GROUP BY customers.customerName
    ORDER BY SUM(payments.amount) DESC
    """
    cursor.execute(sql_query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result
