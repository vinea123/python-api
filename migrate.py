# Run  python migrate.py

from database.database import connection
# from migration.category import category_table
# from migration.product import product_table
from migration.todo import todo_table

if connection:
    # category_table(connection)
    # product_table(connection)
    todo_table(connection)


