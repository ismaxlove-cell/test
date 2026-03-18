def fibonacci(n):
    """피보나치 수열의 처음 n개 항을 리스트로 반환한다.

    Args:
        n: 생성할 피보나치 수의 개수 (양의 정수)

    Returns:
        피보나치 수열 리스트

    Raises:
        TypeError: n이 정수가 아닌 경우
        ValueError: n이 양의 정수가 아닌 경우
    """
    if not isinstance(n, int):
        raise TypeError(f"정수가 필요합니다. 입력된 타입: {type(n).__name__}")
    if n <= 0:
        raise ValueError(f"양의 정수가 필요합니다. 입력된 값: {n}")

    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result


if __name__ == "__main__":
    numbers = fibonacci(10)
    print(f"피보나치 수열 (10개): {numbers}")
