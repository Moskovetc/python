#Задача 1
name='Елена'
litra=5
math=4.5
print(name, 'получила ', math, 'по математике', 'и ', litra, 'по литературе')
chest=input('Сколько в доме стульев? \n')
print('Стульев: ', chest)
#Задача 2
chest=int(chest)
print('я привез еще 2 стула, теперь в доме ', chest+2, 'стульев' )
#Задача 3
age=float(input('введите свой возраст\n'))

if age>=18:
    print('Доступ разрешен\n')
else:
    print('Извините, пользование данным ресурсом только с 18 лет')