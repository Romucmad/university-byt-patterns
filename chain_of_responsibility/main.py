from chain_of_responsibility.classes import AddDo, SubtractDo, MultiplyDo, DivideDo, NumberRequest


def main():
    first = int(input('Write first number please\n'))
    second = int(input('Write first second please\n'))
    do = str(input('Write  do please\n'))
    numbers = NumberRequest(first, second, do)
    divide = DivideDo()
    multiply = MultiplyDo()
    subtract = SubtractDo()
    add = AddDo()
    add.set_next_chain(subtract)
    subtract.set_next_chain(multiply)
    multiply.set_next_chain(divide)

    result = add.calculate(numbers)
    print(result)


if __name__ == '__main__':
    main()
