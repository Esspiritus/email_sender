Добавьте импорт класса EmailSender в начало вашего скрипта
#from EmailSender import EmailSender

После успешного входа с паролем, вызовите метод send_email для отправки результатов на электронную почту. 
Замените receiver@example.com на адрес, на который вы хотите отправить результаты.
# Example usage:
# sender = EmailSender("smtp.example.com", 465, "your_email@example.com", "your_password")
# sender.send_email("receiver@example.com", "Test Subject", "This is a test email.")
