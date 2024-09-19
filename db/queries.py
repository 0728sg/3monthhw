CREATE_TABLE_PRODUCTS = """
    CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name_product VARCHAR(255),
    size VARCHAR(255),
    price VARCHAR(255),
    product_id VARCHAR(255),
    category VARCHAR(255),
    info_product VARCHAR(255),
    photo TEXT
    )
"""


INSERT_PRODUCTS_QUERY = """
    INSERT INTO products (id, name_product, size, price, product_id, category, info_product, photo)
    VALUES (?, ?, ?, ?, ?)
"""

CREATE_TABLE_COLLECTION_PRODUCTS = """
    CREATE TABLE IF NOT EXISTS products_details (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    product id VARCHAR(255),
    collection VARCHAR(255),
    )
"""

INSERT_PRODUCTS_QUERY_DETAILS = """
    INSERT INTO products (id, product_id, collection)
    VALUES (?, ?, ?)
"""