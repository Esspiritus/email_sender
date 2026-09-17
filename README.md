📧 Email Sender
Python-класс для отправки email через SMTP с поддержкой SSL. Удобно использовать для пересылки логов работы скрипта на почту.

<img src="https://github.com/Esspiritus/email_sender/assets/164971431/fdee3f1b-191f-4fe8-bd84-ff0b1648704c" alt="Описание изображения" style="width: 700px; height: 550px;">


📋 Что вам понадобится

Python 3.6+	python.org
SMTP-сервер	Например, smtp.gmail.com, smtp.yandex.ru, smtp.mail.ru
Логин и пароль от почты	Логин — адрес почты, пароль — пароль приложения (не обычный!)
Порт	Обычно 465 (SSL) или 587 (STARTTLS)


Для Gmail, Яндекс.Почты и Mail.ru обычный пароль не подойдёт. Нужно создать пароль приложения в настройках безопасности почты:

Gmail: myaccount.google.com/apppasswords

Яндекс: Настройки → Безопасность → Пароли приложений

Mail.ru: Настройки → Безопасность → Пароли для внешних приложений

🗂 Шаг 1. Разложите файлы
Создайте папку проекта и положите туда два файла рядом:

```text
my_project/
├── email_sender.py   ← с GitHub
└── main.py           ← ваш скрипт, который шлёт логи
```
[!TIP]
Если email_sender.py лежит в другой папке, используйте импорт с путём:

```python
from путь.до.email_sender import EmailSender
Но проще положить рядом.
```
🚀 Шаг 2. Проверьте, что импорт работает
В main.py добавьте первую строку:

```python
from email_sender import EmailSender
```
Запустите:

```bash
python main.py
```
Если ошибок нет переходите дальше.
Если видите ModuleNotFoundError: No module named 'email_sender', значит файл лежит не рядом или запускаете не из той папки.

🔑 Шаг 3. Укажите данные SMTP
В main.py заполните четыре переменные своими значениями:

```python
# --- Настройки SMTP ---
smtp_server = 'smtp.yandex.ru'      # адрес SMTP-сервера
smtp_port   = 465                   # порт (обычно 465 для SSL)
sender_email    = 'you@yandex.ru'   # ваша почта
sender_password = 'abcd efgh ijkl'  # пароль приложения, НЕ обычный!
Провайдер	smtp_server	smtp_port
Яндекс	smtp.yandex.ru	465
Gmail	smtp.gmail.com	465
Mail.ru	smtp.mail.ru	465
Outlook	smtp.office365.com	587 (STARTTLS)
```
[!WARNING]
Никогда не коммитьте пароль в GitHub. Используйте переменные окружения:

```python
import os
sender_password = os.getenv("SMTP_PASSWORD")
```
🧩 Шаг 4. Создайте объект-отправитель
Сразу после настроек:

```python
email_sender = EmailSender(
    smtp_server,
    smtp_port,
    sender_email,
    sender_password
)
```
Этот объект создаётся один раз и переиспользуется для всех писем.

📝 Шаг 5. Собирайте логи в список
В том месте скрипта, где вы хотите логировать события, добавляйте строки в список:

```python
logs = []

logs.append("Начало работы скрипта")
# ... ваш код ...
logs.append(f"Обработано записей: {count}")
logs.append("Скрипт завершён")
```
[!NOTE]
Список logs — обычный Python-список. Можете писать туда что угодно: статусы, ошибки, числа, traceback при исключениях.

📤 Шаг 6. Отправьте логи на почту
В конце скрипта соберите список в одну строку и отправьте:

```python
email_body = '\n'.join(logs)

email_sender.send_email(
    receiver_email='boss@example.com',
    subject='Логи работы скрипта',
    body=email_body
)
```
Готово — письмо уйдёт на указанный адрес.

📄 Лицензия
MIT
