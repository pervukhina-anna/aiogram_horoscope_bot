# Aiogram Horoscope Bot <img src="https://img.icons8.com/color/344/crystal-ball.png" height="24"/>


### Описание
Телеграм-бот, позволяющий узнать гороскоп для выбранного знака зодиака и на выбранный день.

![starting_img](https://user-images.githubusercontent.com/101391679/174481937-3ab10367-e3dd-4071-b3fe-de7395e6acd2.png)

Имеет предопределенный набор команд, в случае получения неизвестной команды просит уточнить введенные данные.

![command_list](https://user-images.githubusercontent.com/101391679/174482007-f44ef77a-fa77-4264-9448-cceaf394dbf3.png)


Выбор знака зодиака и дня обеспечены за счет ReplyKeyboard - клавиатуры, которая появляется после ввода определенной
команды:

![button_list](https://user-images.githubusercontent.com/101391679/174482349-97ce1dba-6b5b-4658-a129-c4468b15e172.png)

После получения необходимых данных для формирования гороскопа (знак зодиака и день) обращается к API-сервису и формирует ответ:

![result](https://user-images.githubusercontent.com/101391679/174482176-a29ce9a1-fa7a-4106-9ea5-653a48915e37.png)

### Технологии в проекте;  
Python 3.9.13  
Aiogram 2.20  

### Установка, настройка:  
* Клонируйте репозиторий
* Установите и активируйте виртуальное окружение:

Win:
```python
python -m venv venv
venv/Scripts/activate
```
Mac:
```python
python3 -m venv venv
source venv/bin/activate
```
* Установите зависимости из файла requirements.txt
```python
pip install -r requirements.txt
```
* Создайте файл `.env` и сохраните в нем `TELEGRAM_TOKEN` (токен бота) и `TELEGRAM_CHAT_ID` (ваш id в телеграм)
* Запустите бота

### Документация:  
[Telegram Bot API](https://core.telegram.org/bots/api)   
[Документация Aiogram](https://docs.aiogram.dev/en/latest/index.html)   

### Полезные статьи:  
[Пишем Telegram-ботов на Python (v2)](https://mastergroosha.github.io/telegram-tutorial-2/)  
[Aiogram. Разбираем FSM простыми словами](https://lolz.guru/threads/3769612/)  
[Всё, о чём должен знать разработчик Телеграм-ботов](https://habr.com/ru/post/543676/)  
[Асинхронный Telegram бот на языке Python 3 с использованием библиотеки aiogram](https://surik00.gitbooks.io/aiogram-lessons/content/)  

