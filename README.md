
<img src="https://github.com/Esspiritus/email_sender/assets/164971431/fdee3f1b-191f-4fe8-bd84-ff0b1648704c" alt="Описание изображения" style="width: 700px; height: 550px;">

Файл email_sender.py должен находится в том же каталоге, что и ваш скрипт.
Или используйте правильный путь при импорте - 
```python
from путь.до.email.sender import EmailSender
```
Далее добавляете в свою программу, логи которой нужны, данный код:

```python
from email_sender import EmailSender

#Здесь указываете параметры SMTP сервера и учетные данные отправителя

smtp_server = 'smtp.example.com'
smtp_port = 465
sender_email = 'email@example.com
sender_password = 'password'

#Объект класса EmailSender
email_sender = EmailSender(smtp_server, smtp_port, sender_email, sender_password)

#Переменная для сохранения логов
logs = []


#Отправляем все логи по email
email_body = '\n'.join(logs)
email_sender.send_email('mail@example.com', 'Логи работы скрипта', email_body)
```
