def tea_order(customer_name, tea_type, milk=None):
    print(customer_name, "ordered a", tea_type, "tea")
    if milk!=None:
        print("  - Add:", milk)

tea_order("Alice", "chamomile")
tea_order("Bob", "chao", "with a side of milk")


def tea_order_deluxe(customer_name2, tea_type2, *args):
    print(customer_name2, "ordered a", tea_type2, "tea")
    for arg in args:
        print("  - Add:", arg)

tea_order_deluxe("Alice", "chamomile")
tea_order_deluxe("Bob", "black", "oat")
tea_order_deluxe("Cindy", "black", "oat", "honey")


def tea_order_ultra(customer_name3, tea_type3, **kwargs):
    print(customer_name3, "ordered a", tea_type3, "tea")
    for key, value in kwargs.items():
        print("  - Add", key, ":", value)

tea_order_ultra("Anby", "chamomile")
tea_order_ultra("Billy", "black", milk="oat")
tea_order_ultra("Carol", "black", milk="oat", sweetener="honey")


def tea_order_super_deluxe(customer_name4, tea_type4, *args, **kwargs):
    print(customer_name4, "ordered a", tea_type4, "tea")
    for arg in args:
        print("  - Add:", arg)
    for key, value in kwargs.items():
        print("  - Add", key, ":", value)

tea_order_super_deluxe("Dillon", "black", "oat", sweetener="honey")

# Indefinite Arguments (*args) Practice #1
# Create a function called sum_squares that takes any number of numeric arguments, and returns the sum of their values squared.
# For example for the arguments sum_squares(1,2,3) it should return 14 (1+4+9).

def sum_squares(*args):
    sum = 0
    for num in args:
        sum += num ** 2
    
    return sum

print(sum_squares(1, 2, 6))

# This isn't performance task ready because it doesn't have SELECTION. DO NOT CONFUSE SELECTION WITH SEQUENCING!


# Indefinite Arguments (*args) Practice #2
# Create a function called absolute_sum, which takes any number of arguments, and returns the sum of their absolute values (that is, it takes the non-negative values and adds them together, in other words, considers them all - negative and positive - as positive).

def absolute_sum(*args):
    abs_sum = 0
    for nums in args:
        abs_sum += abs(nums)

    return abs_sum

print(absolute_sum(-1, 0, 6, 4, 5))

# Indefinite Arguments (*args) Practice #3
# Create a function called personal_numbers that receives, as its first argument, a name, and then an indefinite number of values.

# The function should return the following message:

# "{name}, the sum of your numbers is {sum_numbers}"