table = [[1, 2, 3, 4, 5, 6], [0.571, 0.889, 1.091, 1.231, 1.333, 1.412]]
# Абажаю хардкод)))))

def leftSideDerivative(yValues, xValues):
    answer = ['-', ]

    for i in range(1, len(yValues)):
        answer.append(yValues[i] - yValues[i - 1])

    return answer

def main():
    yValues = table[1]
    xValues = table[0]
    firstColumn = leftSideDerivative(yValues, xValues)
    print("LeftSideDerivative:", firstColumn)




main()
