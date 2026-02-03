FROM selenium/standalone-chrome:latest


WORKDIR /app


# 2. Устанавливаем Python зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN rm -rf /home/seluser/.wdm && pip uninstall -y webdriver-manager && pip install webdriver-manager

ADD https://github.com/allure-framework/allure2/releases/download/2.27.0/allure-2.27.0.tgz /app/

# 3. Копируем проект
COPY . .

RUN sudo chmod 777 allure-2.27.0.tgz && tar xvfz allure-2.27.0.tgz

CMD ["sh", "-c", "python3 -m pytest tests/ -v --alluredir=./allure-results && /app/allure-2.27.0/bin/allure serve ./allure-results -p 8080"]