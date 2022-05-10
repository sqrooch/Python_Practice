"""
Your job is to write a function which increments a string, to create a new string.
If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.

Examples:
foo -> foo1
foobar23 -> foobar24
foo0042 -> foo0043
foo9 -> foo10
foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.
"""


# My decision:
# def increment_string(strng):
#     """Increases the number at the end of a string by one."""
#     if strng == "" or not strng[-1].isdigit():
#         strng += "0"
#     strng = "s" + strng
#     original_str_length = len(strng)
#     tail_of_nums = ""
#     for i in range(original_str_length-1, -1, -1):
#         if not strng[i].isdigit():
#             tail_of_nums = int(strng[i+1:])
#             tail_of_nums += 1
#             tail_of_nums = str(tail_of_nums)
#             strng = strng[1:i+1]
#             break
#     return strng + (original_str_length - 1 - len(strng + tail_of_nums)) * "0" + tail_of_nums


# Best decision:
def increment_string(strng):
    """Increases the number at the end of a string by one."""
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "": return strng + "1"
    return head + str(int(tail) + 1).zfill(len(tail))


print(increment_string("foo"))
print(increment_string("foobar23"))
print(increment_string("foo0042"))
print(increment_string("foo9"))
print(increment_string("foo099"))
print(increment_string("foo09f9"))
print(increment_string(""))
