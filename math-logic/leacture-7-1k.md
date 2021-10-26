# Полином Жегалкина

![img](https://sun9-33.userapi.com/impg/h9uSNYpwWyfP98wwqNw1ribFSAXoLKSgaK57mw/Z1MAYIDC78Q.jpg?size=754x560&quality=96&sign=9ab7caf0999e1622ec9200b49797a47c&type=album)

Жегалкин предложил полином в качестве одного из способов представления булевых функций.

**Элементарная конъюнкция** на множестве булевых переменных {0; 1} называется монотонной, если она не содержит отрицание переменных

Монотонная конъюнкция имеет вид:

```
x  * x   * ... * x   
 i1   i2          im

где m >= 1 

i ∈ {1, 2, ..., n}
 k


либо является константной 1
```

**Полином Жегалкина** - это полином, коэффициенты которого это либо числа 0, либо 1, в качестве операции в полиноме выступает конъюнкция и сложение по модулю 2 

![img](https://sun9-72.userapi.com/impg/Zid9DmrVWzSpzV3clLATZI0_Q9M81HMiTcOiVg/P-bjT-EWPtI.jpg?size=756x565&quality=96&sign=09e7e92ae37acba8dde515ccb8d34861&type=album)

## Cвойства операции по сложению модулю 2

![img](https://sun9-8.userapi.com/impg/rzD6PcKA01M2yR3W-GaSyE2bbbbXgdUTtyVceQ/TiLUxeUwjS0.jpg?size=665x427&quality=96&sign=cb30ba1752c9bffaebb03ead83ccea23&type=album)

![img](https://sun9-76.userapi.com/impg/qzw97NFHrY36TQyT3JVzsI5IDG6CrTGbIRwSWg/0HhU29WZDL4.jpg?size=713x419&quality=96&sign=84fbba34462634c58f963e8dc0a39efc&type=album)

## Теорема

Любая функция алгебры логики от n переменных может быть представлена полиномом Жегалкина и это представление единственно

___

![img](https://sun9-27.userapi.com/impg/GQkrFEAVX6Xwx3YwgXk--oJluyMIMNV0k7eiig/ma6c1zU-oxc.jpg?size=749x567&quality=96&sign=4c63402121d39a5baf76832af37833c4&type=album)

![img](https://sun9-8.userapi.com/impg/jTlzgpTv68M8mJaOANcBQGUT1oR-IfsoXuNQtA/TSmh3_y67N0.jpg?size=752x565&quality=96&sign=75a9aa3315fcaef1f2d18af11b8b54eb&type=album)

## Способы разложения булевой функции в Полиноме Жигалкина

1. Метод неопределённых коэффициентов

Булевая функция записывается в виде полинома Жигалкина с неопределёнными коэффициентами. Далее приравниваются значения функции к значению полинома на соответствующих наборах переменных. Из этих равенств составляется система уравнений, решая которую находим неизвестные коэффициенты полинома.

2. Метода треугольника Паскаля

Составляется таблица истинности булевой функции. Записывается вектор этой функции F. Строится треугольник Паскаля. В каждой строке треугольника Паскаля ставится в соответствии монотонная конъюнкция полинома. Для этого, двигаясь по сторонам треугольника сверху-вниз ставим в соответствии в каждой строке двоичный набор из таблицы истинности. По значению F=1 записывается монотонная конъюнкция. В полином войдут те конъюнкции, коэффициенты которых равны 1 на левой стороне треугольника Паскаля.

Замечание: переменная булевой функции является несущественной тогда и только тогда, когда полином Жигалкина не содержит

3. С помощью преобразования СДНФ

![img](https://sun9-48.userapi.com/impg/XoPBeLtoGSGKKxGc2T9lzwgz7sPDYRAIin-gSA/Vh8zia3Y-iQ.jpg?size=754x565&quality=96&sign=12d86cd3539f8ad0739b5b30ff812ab3&type=album)