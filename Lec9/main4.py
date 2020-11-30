"""
Сравнение строковых литералов.
В Python строки хранятся в unicode. 
"""
print("A" < "a") # 65 > 97
print("a" > "ABCDEFGH")

# Как сравниваются односимвольные строки?
print("A ordinal:", ord("A"))
print("Z ordinal:", ord("Z"))
print("91, 92, 93", chr(91), chr(92), chr(93))
print("a ordinal:", ord("a"))
print("b ordinal:", ord("b"))

# Сравнение строк проивзольной длины
print("abcd" < "abcf") # "a" == "a" => "b" == "b" => "c" == "c" => "d" < "f"

print("a" > "ABCDEFGH") # "a" > "A"

print("abcd" < "abcdefg") # "" < "e"

"""
Строки в Python сравниваются посимвольно (выхватая попарно совпадающие индексы у двух сравниваемых строк)
Сравнение продолжается до тех пор, пока не установится знак > или < между парой символов.
"""

print("a" == "a") # 97 == 97
print("a" != "A")  # 97 != 65