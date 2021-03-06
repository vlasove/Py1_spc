"""
Модулем в языке Python называют любой файл с расширением .py
Рабочий модуль.
"""
#import funcs # Притягивает модуль funcs в рабочий модуль main
             # При импортировании притягиваемый модуль выполняется !!от начала до конца!!
             # Если при импортировании в модуле содежится ошибка - то и вся программа завершится с ошибкой

#print("Inside main!")
"""
Как обращаться к элементам, которые находятся внутри модуля funcs?
Существует 2 варианта:
* Разделенная область имен
* Совмещенная область имен


Разделенная область имен. Для обращения к элементу стороннего модуля
необходимо указывать имя модуля при импортировании, а затем, через точку, то, что мы хотим вызвать из
стороннего модуля. Пример:

import funcs

funcs.add(10, 20)

Разделенная область имен имеет ряд преимуществ в тех ситуациях, когда при разработке
могут возникать коллизии. То есть встречаться одинаковые имена в различных модулях.
"""

"""
Для решения проблемы разделения функционала модуля на функционал при вызове и функционал при импортировании,
используют переменную __name___.
__name__ => caller (кто вызвал данный модуль)
__name__ == "__main__" если модуль был запущен напрямую (python module.py)
__name__ == "module" (если модуль был импортирован)
"""

"""
А что если имя модуля длинное или неудобное?
В языке есть способность вешать местоимения на имена импортируемых
модулей.

import funcs as f 
"""

import funcs as f 

print("Funcs.add():", f.add(10, 20))
print("Funcs.DB_URI:", f.DB_URI)

