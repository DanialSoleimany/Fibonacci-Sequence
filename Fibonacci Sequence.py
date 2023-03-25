# First twenty items of fibonacci sequence
def fibonacci_sequence():
    
    sequence = [0, 1]
    while True:
        sum = sequence[-1] + sequence[-2]
        sequence.append(sum)
        if len(sequence) > 20:
            break

    print(f"Fibonacci sequence = {sequence}")

    num, count = 0, 0
    for num in sequence:
        Fi = f"F{count} = {num}"
        count += 1
        print(Fi)

fibonacci_sequence()



