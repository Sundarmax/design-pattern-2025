from abc import  ABC,abstractmethod

# define command interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
    @abstractmethod
    def undo(self):
        pass

class Light:

    def on(self):
        print("Light turned on")

    def off(self):
        print("Light turned off")

class Thermostat:

    def __init__(self):
        self.current_temperature = 20

    def set_temperature(self, value):
        print(f"Thermostat set to {value} * C ")
        self.current_temperature = value

    def get_temperature(self):
        return  self.current_temperature


# implement concrete command class

class LightOnCommand(Command):

    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()

class LightOffCommand(Command):

    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()

# invoker class with undo support.

class SmartHome:

    def __init__(self):
        self.current_command = None
        self.history = []

    def set_command(self, command):
        self.current_command = command

    def press(self):
        if self.current_command:
            self.current_command.execute()
            self.history.append(self.current_command)
        else:
            print("No commands have been assigned")

    def undo_last(self):
        if self.history:
            last_cmd = self.history.pop()
            last_cmd.undo()
        else:
            print("Nothing to undo")

if __name__ == "__main__":
    # Receivers
    light = Light()
    # commands
    light_on = LightOnCommand(light)

    # invoker
    button = SmartHome()
    print("-> pressing light ON")
    button.set_command(light_on)
    button.press()
    print("-> undo latest action")
    button.undo_last()
