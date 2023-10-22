# YaCut
##### Сервис для получения коротких ссылок.

Для начала работы необходимо:
* Клонировать репозиторий и перейти в него в командной строке:
   ```
   git clone git@github.com:Sobiyk/yacut.git
   ```

  ```
  cd yacut
  ```

* Cоздать и активировать виртуальное окружение:

  ```
  python3 -m venv venv
  ```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

* Установить зависимости из файла requirements.txt:

  ```
  python3 -m pip install --upgrade pip
  ```

  ```
  pip install -r requirements.txt
  ```
 
* Шаблон заполнения файла .env
  ```
  FLASK_APP=yacut
  FLASK_ENV=development
  DATABASE_URI='sqlite:///db.sqlite3'
  SECRET_KEY='SECRET_KEY'
  ```
* Создайте базу данных и таблицы
  ```
  flask shell
  from yacut import db
  db.create_all()
  ```
* Запустите проект
   ```
   flask run
   ```

##### Автор: [Sobiy](https://github.com/Sobiyk)