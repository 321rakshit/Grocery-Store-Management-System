
from sql_connection import get_sql_connection

def get_all_products(connection):
    cursor = connection.cursor()
    query = ("select products.product_id, products.name, products.uom_id, products.priceperunit, uom.uom_name from products inner join uom on products.uom_id=uom.uom_id")
    cursor.execute(query)
    response = []
    for (product_id, name, uom_id, priceperunit, uom_name) in cursor:
        response.append({
            'product_id': product_id,
            'name': name,
            'uom_id': uom_id,
            'priceperunit': priceperunit,
            'uom_name': uom_name
        })
    return response

def insert_new_product(connection, product):
    cursor = connection.cursor();
    query = ("INSERT INTO products (name, uom_id, priceperunit) VALUES(%s, %s, %s)")
    data = ( product['product_name'], product['uom_id'], product['priceperunit'])
    cursor.execute(query,data)
    connection.commit()

    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products where product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()

    return cursor.lastrowid

if __name__ == '__main__':
    connection = get_sql_connection()
    print(get_all_products(connection))
    #print(delete_product(connection,2))
    print(insert_new_product(connection, {
        'product_name': 'potatoes',
        'uom_id': '1',
        'priceperunit': '10',
    }))
