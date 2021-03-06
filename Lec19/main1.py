"""
Генератор - это функция, которая вместо завршения может "заснуть" до момента ее следующего вызова.
Генератор - это ленивый итератор.
"""

def my_generator():
    """
    Генератор на 3 шага
    """
    yield 10
    yield 20
    yield 30
    
    # return None 


gen = my_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
for i in gen:
    print(i)

"""
Суровая правда про цикл  for - каждый раз (на каждой итерации) идет попытка вызвать next(gen) у итератора 
(Итератор - тот, по которму итерируются, перебирают циклом for). Если в результате вызова
возвращается какое-то значение - оно присваивается в переменную i,
а если вылетает исключение StopIteration - итератор исчерпан и выходим из цикла.



Основная фишка генератора - экономия памяти (генератор единовременно расчитывает только 1 значение)
 и удобство использование.

asyncio => yield используется для передачи управления другим тредам 
"""

    
    