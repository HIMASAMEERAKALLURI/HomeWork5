import importlib
import os

class Command:
    def execute(self, *args):
        raise NotImplementedError("You should implement this method")

class AddCommand(Command):
    def execute(self, a, b):
        return a + b

class SubtractCommand(Command):
    def execute(self, a, b):
        return a - b

class MultiplyCommand(Command):
    def execute(self, a, b):
        return a * b

class DivideCommand(Command):
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

class Calculator:
    def __init__(self):
        self.commands = {
            "add": AddCommand(),
            "subtract": SubtractCommand(),
            "multiply": MultiplyCommand(),
            "divide": DivideCommand()
        }

    def execute_command(self, command_name, *args):
        command = self.commands.get(command_name)
        if command:
            return command.execute(*args)
        else:
            raise ValueError(f"Command '{command_name}' not recognized")
        
    def load_plugins(self, plugin_dir='plugins'):
       if os.path.exists(plugin_dir):
           for filename in os.listdir(plugin_dir):
               if filename.endswith('.py') and not filename.startswith('__'):
                   module_name = filename[:-3]
                   module = importlib.import_module(f'{plugin_dir}.{module_name}')
                   command_name = module_name
                   command_class = getattr(module, f'{command_name.capitalize()}Command')
                   self.register_command(command_name, command_class())