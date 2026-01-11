# aa no use value ne jaru pade tayre run karavi saki chi like
#  peli var run karta vardan made che em ..
#  yield - keyword that is use for generator
def vip_generator():
    list=("vardan\n","pratik\n","smit\n")
    for i in list:
        yield i*2


# gene=vip_generator()

# for v in gene:
#     print(v)


def ngenerator():
    vr = int(input("noo : "))
    for i in range(vr):
        if (i%2==0):
          yield i

g=ngenerator()

# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
print(next(g))
for k in g:
    print(k)
          
# def fibonacci_generator(limit):
#     a, b = 0, 1
#     count = 0
#     while count < limit:
#         yield a
#         a, b = b, a + b
#         count += 1

# # Example usage:
# fib_limit = 10
# fibonacci_gen = fibonacci_generator(fib_limit)

# print(f"Fibonacci numbers up to {fib_limit}:")
# for number in fibonacci_gen:
#     print(number, end=" ")
