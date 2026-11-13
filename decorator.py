def smart_div(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a,b)
    return inner

@smart_div            # Либо реализация с помощью синт. сахара как @
def div(a,b):
    print(a/b)


div = smart_div(div)  # Либо делаем объект с декоратором который принимает функцию

div(2, 4)

# Декоратор возвращает новую функцию расширяя ее поведение но не меняя исходник