import csv
import os
import sqlite3

DB_NAME = "movies_rating.db"
SQL_SCRIPT = "db_init.sql"

TABLES = {
    "movies": {
        "file": "movies.csv",
        "columns": ["id", "title", "year", "genres"],
        "types": ["INTEGER PRIMARY KEY", "TEXT", "INTEGER", "TEXT"],
        "auto_id": False
    },
    "ratings": {
        "file": "ratings.csv",
        "columns": ["user_id", "movie_id", "rating", "timestamp"],
        "types": ["INTEGER", "INTEGER", "REAL", "INTEGER"],
        "auto_id": True
    },
    "tags": {
        "file": "tags.csv",
        "columns": ["user_id", "movie_id", "tag", "timestamp"],
        "types": ["INTEGER", "INTEGER", "TEXT", "INTEGER"],
        "auto_id": True
    },
    "users": {
        "file": "users.txt",
        "columns": ["name", "email", "gender", "register_date", "occupation"],
        "types": ["TEXT", "TEXT", "TEXT", "TEXT", "TEXT"],
        "auto_id": True
    }
}

def escape_sql(value):
    if value is None:
        return "NULL"
    return "'" + str(value).replace("'", "''") + "'"

def main():
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)
        print(f"Старая база {DB_NAME} удалена.")

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    with open(SQL_SCRIPT, "w", encoding="utf-8") as sql_file:
        sql_file.write("-- SQL скрипт для создания и заполнения базы данных\n\n")

        for table_name, info in TABLES.items():
            file_name = info["file"]
            columns = info["columns"]
            types = info["types"]

            if not os.path.exists(file_name):
                print(f"Файл {file_name} не найден, пропускаем таблицу {table_name}.")
                continue

            col_defs_list = []
            if info.get("auto_id"):
                col_defs_list.append("id INTEGER PRIMARY KEY AUTOINCREMENT")
            col_defs_list.extend([f"{col} {typ}" for col, typ in zip(columns, types)])
            col_defs = ", ".join(col_defs_list)
            create_sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({col_defs});"
            
            cursor.execute(f"DROP TABLE IF EXISTS {table_name};")
            cursor.execute(create_sql)
            sql_file.write(create_sql + "\n")

            print(f"Загрузка данных в таблицу {table_name} из {file_name}...")
            with open(file_name, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                header = next(reader)

                for row in reader:
                    while len(row) < len(columns):
                        row.append("")
                    
                    values = ", ".join([escape_sql(val) for val in row[:len(columns)]])
                    insert_sql = f"INSERT OR IGNORE INTO {table_name} ({', '.join(columns)}) VALUES ({values});"
                    
                    cursor.execute(insert_sql)
                    sql_file.write(insert_sql + "\n")

            conn.commit()
            print(f"Таблица {table_name} заполнена.")

    conn.close()
    print(f"База данных {DB_NAME} успешно создана и заполнена.")
    print(f"SQL-скрипт сохранен в {SQL_SCRIPT}.")

if __name__ == "__main__":
    main()