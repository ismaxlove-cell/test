def fibonacci(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result


if __name__ == "__main__":
    numbers = fibonacci(10)
    print(f"피보나치 수열 (10개): {numbers}")
