# Last-in, First-out (LIFO)
# Stack data are mutable. e.g. Python list
class Stack:
    def __init__(self):
        self.items = []

    # add a item onto stack
    def push(self, item):
        self.items.append(item)

    # remove the last item from stack
    def pop(self):
        if self.items:
            return self.items.pop()
        return None
    
    # to know the next item to be removed
    def peek(self):
        if self.items:
            return self.items[-1]
        return None

    # to know how many items are in stack
    def size(self):
        return len(self.items)

    # to know if stack is empty
    def is_empty(self):
        return self.items == []

# balance symbol solution
def match_symbols(symbol_str):
    symbol_pairs = {
    '(':')',
    '[':']',
    '{':'}',
    }

    openers = symbol_pairs.keys()
    my_stack = Stack()

    index = 0
    while index < len(symbol_str):
        symbol = symbol_str[index]

        if symbol in openers:
            my_stack.push(symbol)
        else: #the symbol is closer

            # if the Stack is already empty,  the symbols are not balanced
            if my_stack.is_empty():
                return False
            # if there are still items in the Stack, check for the mis-match
            else:
                top_item = my_stack.pop()
                if symbol != symbol_pairs[top_item]:
                    return False
        index += 1

    if my_stack.is_empty():
        return True
    return False

print('Balance symbols:',match_symbols('([{}])'))
print('Unbalance symbols:',match_symbols('(([{}]})'))




