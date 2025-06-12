def todo_table(connection):
    # check table
    cursor = connection.cursor()
    cursor.execute("SHOW TABLES LIKE 'todo'")
    result = cursor.fetchone()
    
    if result:
        # if have table is alert already
        print("Table 'todo' already exists.")
    else:
        # data for table
        query = """
            CREATE TABLE todo (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(50) NOT NULL,
                create_date DATETIME DEFAULT CURRENT_TIMESTAMP,
                modify_date DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
            );
        """
        cursor.execute(query)
        connection.commit()
        # if don't have table is alert created
        print("Table 'todo' created successfully.")
    
    cursor.close()
