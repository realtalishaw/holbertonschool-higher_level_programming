#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            sum = my_list_1[i] / my_list_2[i]
        except (ValueError, TypeError):
            print("wrong type")
            sum = 0
        except ZeroDivisionError:
            print("division by zero")
            sum = 0
        except IndexError:
            print("out of range")
            sum = 0
        finally:
            new_list += [sum]
    return new_list
