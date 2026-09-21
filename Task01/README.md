# Описание структуры файлов данных

В папке Task01 находятся следующие файлы:

## Исходные данные

- `ratings.csv` — оценки фильмов пользователями. Колонки: userId, movieId, rating, timestamp.
- `movies.csv` — информация о фильмах. Колонки: movieId, title, genres.
- `tags.csv` — теги, которые пользователи присваивали фильмам. Колонки: userId, movieId, tag, timestamp.
- `users.txt` — информация о пользователях. Колонки: userId, gender, age, occupation, zip-code.
- `occupation.txt` — расшифровка кодов профессий пользователей.
- `genres.txt` — список жанров фильмов.

## Созданные файлы

- `ratings_count.txt` — минимальный и максимальный ID пользователей и количество строк с ними.
- `sqlite.txt` — информация о версии SQLite и режимах вывода.
- `README.md` — этот файл.