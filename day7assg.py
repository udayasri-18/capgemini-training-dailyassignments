# Create multiple classes representing different notification channels (Email, SMS, and Push).
# Each channel class should implement the send method.

# Create a function that accepts any object and calls its send method. The object should be able to handle the notification, even if its class is unknown
# demonstrate the above irrespective of type

class Email:
    def send(self):
        print("Email is sent")
class SMS:
    def send(self):
        print("SMS is sent")
class Push:
    def send(self):
        print("Push is sent")
def func(obj):
    if hasattr(obj,'send'):
        obj.send()

e=Email()
func(e)

s=SMS()
func(s)

p=Push()
func(p)

print("\nUsing abstract class")
from abc import ABC, abstractmethod
class Notification(ABC):
    @abstractmethod
    def send(self):
        pass
class Email:
    def send(self):
        print("Email is sent")
class SMS:
    def send(self):
        print("SMS is sent")
class Push:
    def send(self):
        print("Push is sent")
def func(obj):
    if hasattr(obj,'send'):
        obj.send()

e=Email()
func(e)

s=SMS()
func(s)

p=Push()
func(p)