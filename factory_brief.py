
from abc import  ABC, abstractmethod

# define the product interface
class Notification(ABC):
    @abstractmethod
    def notify(self,message):
        pass

# define the notification creator interface
class NotificationCreator(ABC):
    # Factory method.
    @abstractmethod
    def create_notification(self):
        pass
    # common logic using the factory method.
    def notify(self, message):
        ntfy = self.create_notification()
        ntfy.notify(message)

# implement concrete products
class EmailNotification(Notification):
    def notify(self, message):
        print(f"Sending Email : {message}")

class SMSNotification(Notification):
    def notify(self,message):
        print(f"Sending SMS : {message}")

# implement concrete notification creator
class EmailNotificationCreator(NotificationCreator):
    def create_notification(self):
        return EmailNotification()

class SMSNotificationCreator(NotificationCreator):
    def create_notification(self):
        return SMSNotification()


if __name__ == "__main__":

    creator = EmailNotificationCreator()
    creator.notify("Hello - via Email")

    creator = SMSNotificationCreator()
    creator.notify("Hello - via SMS")

