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
                stacks[ (oddStep + 1) % 3 ].append( stacks[oddStep].pop() )
                oddStep = (oddStep + 1) % 3

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

    print(moves)





#main
print(tower_of_hanoi(3))
if 'A' > 'B':
    print('A')
else:
    print('B')
