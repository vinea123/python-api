# def product_table(connection):
#     # check table
#     cursor = connection.cursor()
#     cursor.execute("SHOW TABLES LIKE 'product'")
#     result = cursor.fetchone()
    
#     if result:
#         # if have table is alert already
#         print("Table 'product' already exists.")
#     else:
#         # data for table
#         query = """
#         CREATE TABLE IF NOT EXISTS product (
#             id INT AUTO_INCREMENT PRIMARY KEY,
#             name VARCHAR(50) NOT NULL,
#             category_id INT DEFAULT NULL,
#             create_date DATETIME DEFAULT CURRENT_TIMESTAMP,
#             modify_date DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
#             FOREIGN KEY (category_id) REFERENCES category(id) ON DELETE SET NULL ON UPDATE CASCADE
#         );
#         """
#         cursor.execute(query)
#         connection.commit()
#         # if  have table is alert created
#         print("Table 'product' created successfully.")
    
#     cursor.close()
