1. установить пакеты из requirements.txt
2. создать файл db/local_settings.py.
Содержимое файла:

```
dbconfig = {'host': 'host_name',
            'user': 'user_name',
            'port': '3306',
            'password': 'pass',
            'database': 'database_name'}
```

3. программа запускается из файла main.py, функция main()
4. 