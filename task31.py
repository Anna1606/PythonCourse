# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию

def fib(n):
    if n in [0, 1]:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(int(input("Введите число: "))))

# рекурсия при помощи анонимной функции
fib = lambda N: N if N in (0, 1) else fib(N - 1) + fib(N - 2)
