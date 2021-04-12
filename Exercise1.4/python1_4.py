# Function defined by the exercise
def count_if(file_name,condition):
    with open(file_name, 'r') as f:
        return sum([True for number in f.read().split() if condition(int(number))])


# Condition defined by the exercise
def is_odd(value):
    if value % 2 != 0:
        return True
    else:
        return False

odds = count_if('test.txt',is_odd)
print(odds)