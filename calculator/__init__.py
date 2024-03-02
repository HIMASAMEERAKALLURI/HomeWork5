# calculator/__init__.py

from .calculator import Calculator

def main():
    calc = Calculator()
    calc.load_plugins()

    while True:
        try:
            user_input = input("Enter command (or 'exit' to quit): ")
            if user_input.lower() == 'exit':
                break

            parts = user_input.split()
            command_name = parts[0]
            arguments = [float(arg) for arg in parts[1:]]

            result = calc.execute_command(command_name, *arguments)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
