"""
You probably know the "like" system from Facebook and other pages.
People can "like" blog posts, pictures or other items.
We want to create the text that should be displayed next to such an item.
Implement the function which takes an array containing the names of people that like an item.
It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
"""


# My solution:
# def likes(names):
#     """Accepts a list of likers and returns their compact notation."""
#     counter = int(len(names))
#     if counter > 3:
#         return f"{names[0]}, {names[1]} and {counter - 2} others like this"
#     elif counter > 2:
#         return f"{names[0]}, {names[1]} and {names[2]} like this"
#     elif counter > 1:
#         return f"{names[0]} and {names[1]} like this"
#     elif counter > 0:
#         return f"{names[0]} likes this"
#     else:
#         return "no one likes this"


# Best solution:
def likes(names):
    """Accepts a list of likers and returns their compact notation."""
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)


print(likes([]))
print(likes(["Peter"]))
print(likes(["Jacob", "Alex"]))
print(likes(["Max", "John", "Mark"]))
print(likes(["Alex", "Jacob", "Mark", "Max"]))
