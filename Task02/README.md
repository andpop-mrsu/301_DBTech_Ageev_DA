# Требования к окружению

Для корректной работы скрипта `db_init.bat` на компьютере должны быть установлены:

- **Python версии 3.x**
- **SQLite** (утилита командной строки `sqlite3`)

## Как запустить

1. Убедитесь, что файлы `movies.csv`, `ratings.csv`, `tags.csv`, `users.txt` находятся в той же папке, что и скрипт.
2. Запустите `db_init.bat`.
3. После выполнения скрипта в папке появится база данных `movies_rating.db` и SQL-скрипт `db_init.sql`.

## Структура базы данных

- **movies**: id, title, year, genres
- **ratings**: id, user_id, movie_id, rating, timestamp
- **tags**: id, user_id, movie_id, tag, timestamp
- **users**: id, name, email, gender, register_date, occupation