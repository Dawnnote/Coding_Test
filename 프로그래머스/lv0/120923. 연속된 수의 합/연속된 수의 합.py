def solution(num, total):
    result = list(range(num))

    while True:
        if sum(result) < total:
            for i in range(len(result)):
                result[i] += 1
        elif sum(result) > total:
            for i in range(len(result)):
                result[i] -= 1

        if sum(result) == total:
            break

    return result