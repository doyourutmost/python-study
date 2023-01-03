def multiplier(factor):
    def multiplyByFactor(number):
        return number * factor

    return multiplyByFactor


print(multiplier(2)(5))
