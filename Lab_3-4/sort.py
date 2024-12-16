data = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]

if __name__ == '__main__':
    result = sorted(data, reverse=True, key=abs)
    print(result)
    result_with_lambda = sorted(data, key=lambda a: -1 * abs(a))
    print(result_with_lambda)
