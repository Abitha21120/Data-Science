def solution(inputArray):
    moves = 0
    for i in range(1, inputArray.length):
        if inputArray[i] <= inputArray[i - 1]:
            moves += (inputArray[i - 1] - inputArray[i] + 1)
            inputArray[i] = inputArray[i - 1] + 1
    return moves

# Example usage:
inputArray = [1, 1, 1]
print(solution(inputArray))  # Output: 3
