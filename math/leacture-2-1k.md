# Глава 2 - Элементы векторной алгебры

## Векторы

Величины, которые определяются своим численным значением, называются скалярными.

Пример скалярной величины: площадь, температура ...

Величины, которые определяются не только числовым значением, но и направлением, называются векторными.

**Вектор** - направленный прямолинейный отрезок.

Обозначение:
```
__
AB

A - начало
B - конец
```

Вектор BA называется противоположным к вектору AB

Вектор, противоположный к вектору ***a***, обозначается: -а

Длиной или модулем вектора ***AB*** называется длина отрезка

Вектор, длина которого равна 0, называется нулевым вектором, который не имеет направления.

Вектор, длина которого равна 1, называется единичным.

Единичный вектор, направление которого совпадает с вектором ***a*** называется орт вектора ***a***. Обозначение:

```
_     __
a°   |a°| = 1
```
        
Векторы ̿a̿ и ̿b̿ называются коллинеарными, если они лежат на одной прямой или на параллельных прямых.

Коллинеарные векторы могут быть направлены водну сторону -> сонаправленные
̿
Два вектора ̿b̿ и ̿a̿ называются равными, если они коллинеарны, сонаправлены и имеют одинаковые длины

![img](https://sun9-83.userapi.com/impg/gpd8rfii-sOOCLkkGOBV7s3ZkAnqokpkdxCHlw/YuSzeZXMIRY.jpg?size=810x1080&quality=96&sign=61a7269f09bb2b55db19b1900fca0d00&type=album)

Три вектора в пространстве называются компланарными если они лежат на одной или параллельных плоскостях

## Линейные операции

![img](https://lh3.googleusercontent.com/proxy/4Wz5XfsNNtqfzwqF7I44ycLnrKc4TvBf1dvpG6IT60P961gXCCQParRlwMZyoFMWU6x-gEFu-HM45XFdDjnEpss)

Свойства:
![img](https://sun9-45.userapi.com/impg/Vt7DTZCFoOtcKZbm5PfPffBQA6kawHsJvspSmw/cWz0_jP7Rwc.jpg?size=810x1080&quality=96&sign=b1b702b400cb282eb0b2a0f43db2b2eb&type=album)

## Проекция вектора на ось

```
Проекция точки M на ось l называется основание M1 перпендикуляра, опущенного из точки M на ось l
```

(рисунок левый)

```
Пусть AB произвольный вектор, точки А1 и B1 есть проекция точек A и B на ось l
```

(рисунок правый)

![img](https://sun9-15.userapi.com/impg/ZW_7gI0-H6eF2BPy-RbSZYYTyN3RTbJUXclObw/zbZYGwflOHY.jpg?size=810x1080&quality=96&sign=f64e64b0c2694be1bd74dcc243bff8e4&type=album)

```
Проекция вектора AB на ось l называется положительное число модуль |A1B1|, если вектор A1 B1 и ось l сонаправленные и отрицательное число -|A1B1| противоположнонаправленные.

Если точки A1 и B1 совпадают, 
```

Обозначение:
```
    __                   __
пр  AB -проекция вектора AB на ось l
  l
```
проекция вектора AB на ось l равна произведению модулю вектора A на произведение модуля вектора A на cos(f°) между вектором и осью

```
    _    _
пр  a = |a| * cos
  l
```

## Проекция вектора по координатному базису

Рассмотрим в пространстве прямоугольную систему координат Oxyz

На координатных осях Ox Oy Oz выделим векторы единичной длины (орты), обозначаемые
```
_  _  _
i, j, k
```

![img](https://sun9-88.userapi.com/impg/czDirSZVk6SwFbzNgey3Vn1FU8aA5NI3A9kkqA/qvDFk15MMx0.jpg?size=429x349&quality=96&sign=25c4e3608f29b800dfc0eb161feceeba&type=album)



# Элементы векторной алгебры

```
_   ___   ___   __
a = OM1 + M1N + NM

___   ___
M1N = OM2

__   ___
NM = OM3

_   ___   ___   ___
a = OM1 + OM2 + OM3

___    ___    _        _
OM1 = |OM1| * i = a  * i
                   x

___    ___    _   _    _ 
OM2 = |OM2| * j = a  * j
                   y

___    ___    _   _    _
OM3 = |OM3| * k = a  * k
                   z

_   _    _   _    _   _    _
a = a  * i + a  * j + a  * k   (1)
     x        y        z
```

Числа Ax Ay Az называются координатами вектора A, т.е. координаты А есть проекция на координатной оси

Равенство 1 можно записать в виде:

```
_    
a = (a , a  , a  )   (2)
      x   y    z
```

Длина вектора

```
       _________________
|a| = √a²  +  a²  +  a²       (3)
        x       y      z
```

![img](https://sun9-25.userapi.com/impg/mweifetF3O0DvYjSjaqEGSTciZIdzuk9BH4DyA/33iEJ2GVG3o.jpg?size=1280x960&quality=96&sign=696bd101c18f55b10bc28f0180397c75&type=album)




## Действия над векторами с задаными координатами


```
_    
a = (a , a  , a  )
      x   y    z

_    
b = (b , b  , b  )   (2)
      x   y    z


λ = R

```

Сложение векторов:

![img](https://sun9-47.userapi.com/impg/ECNEG91bGu_HBuBHoK_-01aTyk0eB3Z2JV6CAg/Fopb0JKnNeQ.jpg?size=1280x960&quality=96&sign=e26b50e6b596c9f1cde507e0d701d2d4&type=album)

![img](https://sun9-87.userapi.com/impg/deciUulkvZcCtmABw4H-s3NHhC9S4ZcqojEj0A/KnnNZATJU3c.jpg?size=1280x960&quality=96&sign=3430fbb6f24d9c113f581a7c818769f8&type=album)

Для любой точки M координаты вектора OM называются координатами точки M.


```
__
OM - радиус - вектор

_   __
ч = OM
```

![img](https://sun9-53.userapi.com/impg/c_FwsQDQMmxkNyESIAtXW8BC_d-NnbQTkPhYEA/M4BMFff6MnA.jpg?size=810x1080&quality=96&sign=b90921fd5ef937dfbd99342562911194&type=album)


```
A(x1; y1; z1)

B(x2; y2; z2)

__
AB = {x2-x1; y2-y1; z2-1}
```

2) Скалярное произведение

Скалярным произведением двух ненулевых векторов a и b называется число, равное произведению этих двух векторов на косинус угла между ними

```
             
Обозначение: 
_   _
a * b;

__
ab
 _  _ 
(a, b)

```

![img](https://sun9-61.userapi.com/impg/dddSPCNI4Y6W1ltSEJUz8rXY_DDiJCBKnbXLpA/-P6kN6zZveM.jpg?size=1280x960&quality=96&sign=70d8f99701471eccad2bbac10375ffa8&type=album)


### Свойства:

```
_   _   _   _
a * b = b * a

  _   _      _    _
λ(a * b) = (λa) * b

_    _   _    _   _   _   _
a * (b + c) = a * b + a * c

_       _
a²  =  |a|²

 _      _
|a| = √ a²

Условие перпендикулярности
      _        _
пусть a != 0,  b != 0

_   _      _   _
a ⟂ b  <=> a * b = 0

_    _    _
i² = j² = k² = 1

_   _   _   _   _   _
i * j = j * k = j * k = 0
```

Скалярный квадрат вектора равен квадрату его длины



Найдем скалярное произведение векторов, перемножая векторы как многочлены и пользуясь таблицей скалярного произведения i, j, k

![img](https://sun9-13.userapi.com/impg/pxRkuPB76Z_hxKcWE3YBTNRebZO8HuJ7Gb-Fxw/BJkAC7j7ItA.jpg?size=810x1080&quality=96&sign=492e298611aa7866b77215ffb7896e62&type=album)

![img](https://sun9-6.userapi.com/impg/eiYvfGV3ncSrhNjGPhF8gAZegAGhI-fLLYZnHQ/13GGjYldHV0.jpg?size=1280x960&quality=96&sign=bbe3a38c231f799fe5c7a7ac6792434f&type=album)

```
_   _
a * b = a  *  b  + a  *  b  +  a  *  b
         x     x    y     y     z     z
```


### Приложения

```
_
a = (a , a  , a  )
      x   y    z

_    
b = (b , b  , b  )  
      x   y    z

    _   _
φ = a ^ b
```


Пусть материальная точка перемещается из положения А в положение B под действием постоянной силы F, образующей угол φ с вектором перемещения AB, тогда

![img](https://sun9-57.userapi.com/impg/SG-TuYa_H5-LW6bOt31q_OTBktrwXix3o6erjQ/nzRqTe6mBS8.jpg?size=1280x960&quality=96&sign=2ad70d005730220e4d29eab9d5fd6c7c&type=album)

![img](https://sun9-47.userapi.com/impg/vZJAmqN7HbRMCi4q3Z7iJqSEjoBBFwSoP9qb4Q/rwChLd5AKVU.jpg?size=810x1080&quality=96&sign=92b88f907f424e589036f5e8d54df6e3&type=album)