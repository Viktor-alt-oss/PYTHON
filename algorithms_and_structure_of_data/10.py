def is_balanced_single_pass(s):
    balance = 0
    for i in s:
        if i in '[{(':
            balance += 1
        elif i in ']})':
            balance -= 1

    return balance == 0

print(is_balanced_single_pass("()"))        # True
print(is_balanced_single_pass("{[()]}"))    # True
print(is_balanced_single_pass("{[(])}"))    # False
print(is_balanced_single_pass("((()))"))     # True
print(is_balanced_single_pass("((())"))      # False
