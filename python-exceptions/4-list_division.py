#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for idx in range(list_length - 1):
        try:
            num1 = my_list_1[i]          # May raise IndexError
            num2 = my_list_2[i]          # May raise IndexError
            result = num1 / num2         # May raise ZeroDivisionError or TypeErrorst_2[idx])
        except IndexError:
            print("out of range")
            result = 0
        except (TypeError, ValueError):
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        finally:
            new_list.appedn(result)
    return new_list


