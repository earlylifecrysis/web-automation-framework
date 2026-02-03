# web-automation-framework

Automated login tests for saucedemo.com using Python, Selenium, Allure, Docker



Проект содержит набор автоматизированных тестов для сайта \[Sauce Demo](https://www.saucedemo.com/) - демонстрационного интернет-магазина для тестирования. Реализовано 5 тестовых сценариев проверки авторизации с использованием современных инструментов автоматизации.



Проект реализует автоматизированное тестирование функциональности авторизации на сайте Sauce Demo. Все тесты написаны с использованием паттерна Page Object Model для обеспечения читаемости, поддерживаемости и повторного использования кода.



Основные цели проекта:

\- Автоматизация 5 сценариев авторизации

\- Использование современных инструментов тестирования

\- Интеграция с Allure для отчетов

\- Контейнеризация с помощью Docker



**Технологии**



\- Python 3.10 - основной язык программирования

\- Selenium WebDriver 4.15.0 - автоматизация браузера

\- Pytest 7.4.3 - фреймворк для тестирования

\- Allure Framework 2.27.0 - система отчетности

\- Docker - контейнеризация приложения

\- Page Object Pattern - архитектурный паттерн



**Структура проекта**

web-automation-framework/

├── pages/              # Страницы сайта

│   ├── login\_page.py    # Страница логина

│   └── inventory\_page.py # Главная страница

│

├── tests/              # Тесты

│   └── test\_login.py    # 5 тестов логина

│

├── utils/              # Вспомогательные файлы

│   └── config.py       # Настройки (URL, логины)

│

├── requirements.txt    # Библиотеки Python

├── Dockerfile         # Настройка Docker

├── conftest.py        # Настройки тестов

└── README.md          # Эта инструкция



**Тестовые сценарии**



Проект содержит 5 тестов проверки разных сценариев авторизации:



Тест 1: Успешный логин

\- Пользователь: `standard_user`

\- Пароль: `secret_sauce`

\- Ожидаемый результат: Успешный переход на страницу товаров (`/inventory.html`)



Тест 2: Логин с неверным паролем

\- Пользователь: `standard_user`

\- Пароль: `invalid_password`

\- Ожидаемый результат: Сообщение об ошибке "Username and password do not match"



Тест 3: Логин заблокированного пользователя

\- Пользователь: `locked_out_user`

\- Пароль: `secret_sauce`

\- Ожидаемый результат: Сообщение об ошибке "Sorry, this user has been locked out"



Тест 4: Логин с пустыми полями

\- Пользователь: (пусто)

\- Пароль: (пусто)

\- Ожидаемый результат: Сообщение об ошибке "Username is required"



Тест 5: Логин пользователем с задержками

\- Пользователь: `performance_glitch_user`

\- Пароль:\*\* `secret_sauce`

\- Ожидаемый результат: Успешный переход на страницу товаров, несмотря на возможные задержки



**Установка и запуск**

Для локального запуска:

* Python 3.10
* Chrome браузер
* Chromedriver (автоматически устанавливается через webdriver-manager)
* Allure CLI (для генерации отчетов)



Для Docker запуска:

* Docker Desktop или Docker Engine



Локальный запуск (Windows)

1. Скачать проект

git clone https://github.com/earlylifecrysis/web-automation-framework.git

cd web-automation-framework

2.Установить библиотеки

pip install -r requirements.txt

3.Запустить тесты

py -3.10 -m pytest tests/test\_login.py --alluredir=allure-results -v

4\. Посмотреть отчет (Статический)

allure generate allure-results -o allure-report --clean

allure open allure-report



Запуск в Docker

1. Скачать проект

git clone https://github.com/earlylifecrysis/web-automation-framework.git

cd web-automation-framework

2\. Запуск Docker образа

docker build -t saucedemo-tests .

3\. Запустить тесты в контейнере

docker run --rm -it -p 8080:8080 --name tests sauce-tests

4\. Открыть браузер и перейти по адресу

http://localhost:8080



Важные моменты:



1\. Порт 8080 должен быть свободен на вашем компьютере

2\. Контейнер будет работать, пока открыт отчет (не завершится сам)

3\. Чтобы остановить: нажмите `Ctrl+C` в терминале

4\. Если порт занят, измените на другой:

```bash

docker run --rm -it -p 8888:8080 --name tests sauce-tests

\# Тогда отчет будет: http://localhost:8888



FAQ

1\.Docker не запускается

Проверьте, что Docker запущен: docker --version

Перезапустите Docker Desktop

2\.Не хватает прав

На Linux может понадобиться sudo: sudo docker build -t saucedemo-tests .

3.Ошибка с ChromeDriver

Убедитесь, что в requirements.txt есть webdriver-manager, она автоматически скачает правильный драйвер

4.Allure не установлен

Windows: Откройте Windows Power Shell и напишите команду: scoop install allure

Linux: sudo apt-add-repository ppa:qameta/allure \&\& sudo apt-get update \&\& sudo apt-get install allure





