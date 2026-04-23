def tower_of_hanoi_working_but_wrong(count, stacks=None, source=0, auxiliary=1, destination=2, moves=0):
    if not stacks:
        stacks = [['ABCDEFGHIJKLMNOPQRSTUVWXYZ'[i] for i in range(count-1, -1, -1)], [], []]
        moves = 1
        print(stacks)
    # COMPLETE FROM HERE
        source = stacks[source]
        auxiliary = stacks[auxiliary]
        destination = stacks[destination]

        oddStep = 0
        while len(destination) < count:

            #move a top piece A -> B -> C -> A
            if moves % 2 == 1:
                #assert stacks[ (oddStep + 1) % 3 ] < stacks[oddStep]
                stacks[ (oddStep + 2) % 3 ].append( stacks[oddStep].pop() )
                oddStep = (oddStep + 2) % 3

            #move another
            elif moves % 2 == 0:
                filledStacks = []
                emptyStacks = []

                for stack in stacks:
                    if len(stack) > 0:
                        if stack[len(stack) - 1] != 'A':
                            filledStacks.append(stack)
                    else:
                        emptyStacks.append(stack)

                #move from one to other
                if len(filledStacks) == 1 and len(emptyStacks) == 1:
                    emptyStacks[0].append( filledStacks[0].pop() )

                elif len(filledStacks) == 2:
                    if filledStacks[0][len(filledStacks[0])-1] < filledStacks[1][len(filledStacks[1])-1]:
                        filledStacks[1].append( filledStacks[0].pop() )

                    elif filledStacks[0][len(filledStacks[0])-1] > filledStacks[1][len(filledStacks[1])-1]:
                        filledStacks[0].append( filledStacks[1].pop() )

                elif len(emptyStacks) == 2:
                    pass

                else:
                    raise ValueError()




            else:
                raise ValueError

            moves = moves + 1
            print(stacks)

    #print(moves)
    return moves

def tower_of_hanoi(count, stacks=None, source=0, auxiliary=1, destination=2, moves=0):
    if not stacks:
        stacks = [['ABCDEFGHIJKLMNOPQRSTUVWXYZ'[i] for i in range(count-1, -1, -1)], [], []]
        moves = 1
        print(stacks)
    # COMPLETE FROM HERE
        source = stacks[source]
        auxiliary = stacks[auxiliary]
        destination = stacks[destination]

        oddStep = 0
        while len(destination) < count:

            #move a top piece A -> B -> C -> A
            if moves % 2 == 1:
                #assert stacks[ (oddStep + 1) % 3 ] < stacks[oddStep]
                stacks[ (oddStep + 2) % 3 ].append( stacks[oddStep].pop() )
                oddStep = (oddStep + 2) % 3

            #move another
            elif moves % 2 == 0:

                for index in range(0, 3):
                    first_stack = stacks[index]
                    next_stack = stacks[(index+1)%3]

                    if len(first_stack) > 0 and len(next_stack) > 0:
                        if first_stack[len(first_stack)-1] > next_stack[len(next_stack)-1]:
                            if len(next_stack) > 0 and next_stack[len(next_stack)-1] != 'A':
                                first_stack.append( next_stack.pop() )

                        elif first_stack[len(first_stack)-1] < next_stack[len(next_stack)-1]:
                            if len(first_stack) > 0 and first_stack[len(first_stack)-1] != 'A':
                                next_stack.append( first_stack.pop() )

                    elif len(first_stack) > 0 and first_stack[len(first_stack)-1] == 'A':
                        continue



            else:
                raise ValueError

            moves = moves + 1
            print(stacks)

    #print(moves)
    return moves







#main
print(tower_of_hanoi(3))
