# Системы булевых функций

Любую формулу можно рассматривать как суперпозицию нескольких БФ

Систему функций F={F1, F2, ..., Fn} называют **полной системой**, если любую булевую функцию можно представить формулой, содержащей только эти функции F1, F2, ..., Fn, т.е. реализовать функцию F в виде суперпозиции этих функций

**Замыкание** множества функции F называется множество всех булевых функций, являющихся суперпозициями функции из F. Обозначается [F]

Система называется полной, если её замыкание совпадает с пространством всех булевых функций

## Примеры полных систем

1. F1 = {v, ^, ¬} - стандартный базис
2. F2 = {v, ¬}
3. F3 = {^, ¬}
4. F4 = {->, ¬}
5. F5 = {⊕, 0, 1, ^} - базис Жегалкина

## Специальные классы булевых функций

1. Булевые функции, сохраняющие константу 0

Булевая функция сохраняет константу 0, если F(0, 0, ..., 0) (если значение функции на НУЛЕВОМ наборе = 0)
Обозначим Т0 - класс булевой функции, сохраняющий константу 0

[Т0] - замыкание
[Т0]=Т0 - замыкание совпадает с множеством этих функций

Примеры:

К классу Т0 относятся: 0, X v Y, X ^ Y, X ⊕ Y

2. Булевые функции, сохраняющие константу 1

Булевая функция сохраняет константа 1, если значение F(1, 1, ..., 1) (если значение функции на ЕДИНИЧНОМ наборе = 1)

Обозначим Т1 - класс булевой функции, сохраняющий константу 1

[Т1] - замыкание
[Т1]=Т1 - замыкание совпадает с множеством этих функций

Примеры:

К классу Т1 относятся: 1, X v Y, X ^ Y, X <=> Y, X -> Y

3. Самодвойственные функции

Функция F*(X1, X2, ..., Xn) называется двойственной функцией F(X1, X2, ..., Xn), если выполняется следующее равенство:

F*(X1, ..., Xn) = ¬F(¬X1, ..., ¬Xn)

Замечание: Отношение двойственности является симметричным, т.е. если F* - двойственная к F, то F - двойственная к F*

Построим двойственную функцию к булевой функции F(X1, X2)

```
_______________________________________________
 x1 | x2 | F | ¬x1 | ¬x2 | F(¬x1, ¬x2) |  ¬F  | <- двойственная функция
____|____|___|_____|_____|_____________|______|
  0 |  0 | 0 |  1  |  1  |      0      |   0  |
____|____|___|_____|_____|_____________|______|
  0 |  1 | 0 |  1  |  0  |      0      |   1  |
____|____|___|_____|_____|_____________|______|
  1 |  0 | 0 |  0  |  1  |      0      |   1  |
____|____|___|_____|_____|_____________|______|
  1 |  1 | 1 |  0  |  0  |      0      |   1  |
____|____|___|_____|_____|_____________|______|
```

**Замечание.** Булевая функция является двойственной к дизъюнкции и наоборот

**Определение.** Булевая функция называется САМОДВОЙСТВЕННОЙ, если она двойственна сама к себе, т.е. выполняется следующее равенство F(X1, ..., Xn) = ¬F(¬X1, ..., ¬Xn)

**Пример:** F(X) = ¬X

Множество всех самодвойственных функций обозначим S(класс самодвойственных функций), [S]=S

Наборы F(X1, X2, ..., Xn) и ¬F(¬X1, ¬X2, ..., ¬Xn) называются противоположными, т.е. для самодвойственной функции на любой паре противоположных наборов она принимает противоположные значения.

**Принцип двойственности**: если в формуле, представляющей функцию F, все знаки заменить на соответствующие знаки двойственной функции, то полученная формула будет представлять функцию F*, которая является двойственной к функции F

В частности, если в булевой функции заменить все конъюнкции на дизъюнкции, дизъюнкции на конъюнкции, 0 на 1, 1 на 0, то полученная функция является двойственной к функции F

4. Монотонные булевые функции

**Определение:** если в двух наборах значений переменных X~=(X1, X2, ..., Xn) и X~* =(X1*, X2*, ..., Xn*) выполняется условие Xi >= Xi* для любого i от 1 до n, то говорят, что набор X~ >= X~* (значок обозначает предпочтительнее, больше)

Пример:

1) (0, 0) <= (0, 1)

2) (1, 1) >= (1, 0)

3) (1, 0)  (0, 1) - такие наборы сравнивать нельзя!

**Определение:** функция F(X1, X2, ..., Xn) = F(X~) называется монотонной, если для двух наборов X~ и X~* таких, что X~ >= X~*, выполняется условие F(X~) >= F(X~*)

Пример: F = X1 v X2 - монотонная функция

Теорема: всякая булевая функция, не содержащая отрицаний, представляет собой монотонную функцию, отличную от 0 и 1

Теорема: для любой монотонной функции, отличной от 0 и 1, найдется представляющая её булевая функция без отрицания.

M - класс монотонных функций
[M]=M