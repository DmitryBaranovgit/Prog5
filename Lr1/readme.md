#Лабораторная работа 1
"Реализация удаленного импорта собственного пакета"
#Создаём файл myremotemodule.py
```

```
#Размещаем файл в каталоге rootserver
```

```
#Добавляем URL сервер в sys.path:
```
immport sys
sys.path.append("http://localhost:8000")
```
#Импортируем модуль:
```
import myremotemodule
myremotenodule.myfoo()
```
Результат:
