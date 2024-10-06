class Employee:

    def __init__(self):
        print('Employee created')

    def __del__(self):
        print("Destructor called")


def Created_obj():
    print('Starting Function...')
    obj = Employee()
    print('function end...')
    return obj

obj = Created_obj()
print('Program End...')