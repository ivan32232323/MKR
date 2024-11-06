from datetime import datetime
import base64
class Message:
    def __init__(self, text):
        self.text = text

    def get_text(self):
        return self.text
class MessageDecorator(Message):
    def __init__(self, message):
        self._message = message

    def get_text(self):
        return self._message.get_text()
class EncryptedMessage(MessageDecorator):
    def get_text(self):
        text = self._message.get_text()
        encrypted_text = base64.b64encode(text.encode()).decode()
        return encrypted_text
class CompressedMessage(MessageDecorator):
    def get_text(self):
        text = self._message.get_text()
        compressed_text = ''.join(char for char in text if not char.isupper())
        return compressed_text
class DateTimeMessage(MessageDecorator):
    def get_text(self):
        text = self._message.get_text()
        date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"{date_time} - {text}"
class AuthorMessage(MessageDecorator):
    def get_text(self):
        text = self._message.get_text()
        author = "Шведенко Іван"
        return f"{text} - Автор: {author}"
if __name__ == "__main__":
    base_message = Message("Це Тестове Повідомлення з Пробілами.")
    encrypted_message = EncryptedMessage(base_message)
    print("Зашифроване повідомлення:", encrypted_message.get_text())
    compressed_message = CompressedMessage(encrypted_message)
    print("Зашифроване та стиснене повідомлення:", compressed_message.get_text())
    datetime_message = DateTimeMessage(compressed_message)
    print("Зашифроване, стиснене повідомлення з датою:", datetime_message.get_text())
    author_message = AuthorMessage(datetime_message)
    print("Повідомлення з усім що потрібно :", author_message.get_text())
