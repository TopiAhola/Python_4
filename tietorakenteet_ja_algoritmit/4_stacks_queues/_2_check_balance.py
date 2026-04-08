'''

If everything checks, the function should return the text "Ok - C", being C the number of pairs found.

If not, it should return the text: "Match error at position X", being X the position of the character relative to the beginning of the text.
'''


from _1_push_pop import Stack



def check_balance(text):
    pair_count = 0
    cursor_position = 0
    stack = Stack()

    matching_braces = { '(':')', '[':']', '{':'}' }


    for char in text:
        if char == '(' or char == '[' or char == '{':
            stack.push(char)

        elif char == ')' or char == ']' or char == '}':
            if stack.peek() != None and char == matching_braces[stack.pop()]:
                pair_count += 1
            else:
                return f'Match error at position {cursor_position}'


        #if not enough chars to close all braces
        if (len(text) - cursor_position) <= stack._size:
            return f'Match error at position {cursor_position}'

        #iterate cursor
        cursor_position += 1


    if stack._size == 0:
        return f'Ok - {pair_count}'

    else:
        return f'Match error at position {cursor_position}'



#main
if __name__ == '__main__':
    print(check_balance('a(b)c[d]e{f}g'))
    print(check_balance('a(b)c[)d]e{f}g'))
    print(check_balance('a(b)c(([d][e{f}])g)('))
    print(check_balance(']a(b)c(([d][e{f}])g)'))


