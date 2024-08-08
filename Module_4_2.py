def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

test_function()  # при вызове видим текст
inner_function()  # при вызове видим ошибку: "name 'inner_function' is not defined"