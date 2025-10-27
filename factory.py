
from abc import  ABC, abstractmethod

# define the product interface
class Notification(ABC):
    @abstractmethod
    def notify(self,message):
        pass

# implement concrete products
class EmailNotification(Notification):
    def notify(self, message):
        print(f"Sending Email : {message}")

class SMSNotification(Notification):
    def notify(self,message):
        print(f"Sending SMS : {message}")

# Create a factory class.

class NotificationFactory:
    def create_notification(self, notification_type):
        if notification_type == "email":
            return EmailNotification()
        elif notification_type == "sms":
            return SMSNotification()
        else:
            raise ValueError(f"Unknown notification type : {notification_type}")


if __name__ == "__main__":
    factory = NotificationFactory()

    # create email notification
    email_notifier = factory.create_notification("email")
    email_notifier.notify("Hello Via Email")

    # create sms notification
    sms_notifier = factory.create_notification("sms")
    sms_notifier.notify("Hello Via SMS")

