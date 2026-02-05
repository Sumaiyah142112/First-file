class Emplyee:
    def __init__(self):
        print('Emplyee Created')

    def __del__(self):
        print('Destructor called, Employee deleted')

obj = Emplyee()
del obj