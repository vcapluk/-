and - И
or - ИЛИ
not - Не
!= - Не равно
== - Равно
>= - Больше или равно
<= - меньше или равно
True - Истина
False - Ложь

not 
    not False     True                 # не ложь - истина
    not True      False                # не истина - ложь

OR                            СУММА
    True or False     True            # истина или ложь - истина
    True or True      True            # истина или истина - истина
    False or True     True            # ложь или истина - истина
    False or False    False           # ложь или ложь - ложь

AND                          УМНОЖЕНИЕ
    True and False     False           # истина и ложь - ложь
    True and True      True            # истина и истина - истина
    False and True     False           # ложь и истина - ложь
    False and False    False           # ложь и ложь - ложь

NOT OR 
    not (True or False)      False     # не (истина или ложь) - ложь
    not (True or True)       False     # не (истина или истина) - ложь
    not (False or True)      False     # не (ложь и истина) - ложь
    not (False or False)     True      # не (ложь и ложь) - истина

NOT AND  
    not (True and False)     True      # не (истина или ложь) - истина
    not (True and True)      False     # не (истина или истина) - ложь
    not (False and True)     True      # не (ложь и истина) - истина
    not (False and False)    True      # не (ложь и ложь) - истина

!=                             НЕ РАВНО
    1 ! = 0                  True      #
    1 ! = 1                  False     #
    0 ! = 1                  True      #
    0 ! = 0                  False     #

==                               РАВНО
    1 == 0                   False     #
    1 == 1                   True      #
    0 == 1                   False     #
    0 == 0                   True      #
