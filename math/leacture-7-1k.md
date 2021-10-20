# Тема 5. Плоскость и прямая в пространсте.

## Уравнение в плоскости, проходящая через заданную точку, перпендикулярную заданному вектору.

```
Пусть в пространстве точка M0(x0, y0, z0) ∈ α

_
n = {A, B, C} ⟂ α
```
![img](https://sun9-9.userapi.com/impg/8Le9mHAz-5OuR1oLHpCudgQe8RxkDMfsqzRJyA/ffWMcd2TXXo.jpg?size=1280x667&quality=96&sign=9e7e121ed8aadadc2a2c1d0cad5b0901&type=album)
```
Пусть точка M(x, y, z) ∈ α

___
M0M = {x - x0; y - y0; z - z0}

_   ___     _   ___
n ⟂ M0M <=> n * M0M = 0

A * (x - x0) + B * (y - y0) + C * (z - z0) = 0

_
n = {A, B, C} ⟂ α - нормальный вектор плоскости
```

## Общее уравнение плоскости

```
Ax + By + Cz + (-Ax0 - By0 - Cz0) = 0

Ax + By + Cz + D = 0
```

Частные случаи:
```
1) A = 0, α || Ox
   B = 0, α || Oy
   C = 0, α || Oz

2) A = B = 0, α || Oxy
   A = C = 0, α || Oxz
   B = C = 0, α || Oyz

3) D = 0, то плоскость проходит через начало координат, O(0, 0, 0) ∈ α
```

## Уравнение плоскости, проходящей через три точки

```
Пусть в точке M1(x1, y1, z1), M2(x2, y2, z2), M3(x3, y3, z3) не лежат на одной прямой. Составим уравнение плоскости α, проходящей через эти три точки. Возьмём произвольную точку плоскости M(x, y, z) ∈ α
         ___________________
        /    M3       M1   /
       /     .________.   /
      /              /|  /
     /              / M2/
    /              /   /
   /              M   /
  /__________________/

___
M1M = {x - x1; y-y1; z - z1}
____
M1M2 = {x2 - x1; y2 - y1; z2 - z1}
____
M1M3 = {x3 - x1; y3 - y1; z3 - z1}

Векторы компланарны, их смешанное произведение равно 0

|   x - x1, y - y1, z - z1  |
| x2 - x1, y2 - y1, z2 - z1 | = 0
| x3 - x1, y3 - y1, z3 - z1 |
```

## Уравнение плоскости в отрезках
![img](https://sun9-38.userapi.com/impg/p-z57gIyfWHH7Nz15W42zhG0BKsd3OUDpn-YYQ/3Dwe0KFkSDc.jpg?size=1011x1080&quality=96&sign=bc83d011937886515a4f1201862ad7a7&type=album)
```
Пусть плоскость α отсекает на плоскостях отрезки a, b, c.

A(a; 0; 0)
B(0; b; 0)
C(0; 0; c)

x   y   z
_ + _ + _ = 1
a   b   c
```

Пример
```
Дано:

M0(2; 3; -4) ∈ α
     _
α || a = {-3; 2; -1}
     _
α || b = {0; 3; 1}

Найти:
α = ?

Решение:

          _  _  _
_   _   | i  j  k |   _
a x b = |-3  2 -1 | = i * | 2 -1 | - j * |-3 -1 | + k * |-3 2 | = 5i + 3j - 9k 
        | 0  3  1 |       | 3  1 |       | 0  1 |       | 0 3 |

n = {5; 3; -9} ⟂ α

α = A(x - x0) + B(y - y0) + C(z - z0) = 0

M0 (2; 3; -4) ∈ α

5 * (x - 2) + 3 * (y - 3) - 9(z + 4) = 0

5x - 10 + 3y - 9 -9z - 36 = 0

5x + 3y - 9z - 55 = 0
```
![img](https://sun9-77.userapi.com/impg/G6radU0pSzdGV-250wSuqGllromNQ_0uWAzX9g/FdYbG9xaRmU.jpg?size=1280x727&quality=96&sign=c630965384c077ddf8c41fa6262359c1&type=album)

## Плоскость. Основные задачи

```
α1 : A1x + B1y + C1z + D1 = 0;

α2 : A2x + B2y + C2z + D2 = 0;
                 __   __
φ = (α1 ^ α2) = (n1 ^ n2)

                A1 * A2 + B1 * B2 + C1 * C2
cos φ = ____________________________________________
          _________________       __________________ 
         /  2      2      2      /   2      2      2
        √ A1  +  B1  +  C1   *  √  A2  +  B2  +  C2
            __   __     __   __
α1 ⟂ α2 <=> n1 ⟂ n2 <=> n1 * n2 = 0

A1 * A2 + B1 * B2 + C1 * C2 = 0
```
![img](https://sun9-34.userapi.com/impg/0d6aBAx9mOaYSFzgyk2Ca6VzSJOFh8xQAccuBQ/gO4ZjzpLvRo.jpg?size=654x785&quality=96&sign=c14b20bedafc4b8b67a28d3fdc23b427&type=album)

```

M1(1; -3; 2) ∈ α

α1: 3x -2y + 4z - 3 = 0 || α

α = ?

В качестве нормального вектора в плоскости α можно взять нормальный вектор плоскости α1

Т.к. α || α1, то {3; -2; 4} ⟂ α

α: A(x - x0) + B(y - y0) + C(z - z0) = 0
     ||           ||         ||
      3           -2          4

M0(1; -3; 2) ∈ α

α: 3(x - 1) - 2(y + 3) + 4(z - 2) = 0

3x - 2y + 4z - 17 = 0
```

## Прямая в пространстве

```
                                                                                                      _
Положение прямой в пространстве определяется точкой M0(x0; y0; z0), лежащей на этой прямой и векторам s = {m; n; p}, || L
```

### Канонические уравнения прямой в пространстве

```
Пусть точка M(x; y; z) произвольная

              /
             M
 _  /       /
 s /       / L
  /       /
         M0
        /

       _
M0M || s


x - x0   y - y0   z - z0
______ = ______ = ______
  m        n        p
```

### Параметрические уравнение прямой в пространстве

```
x - x0   y - y0   z - z0
______ = ______ = ______ = t
  m        n        p

x = m * t + x0
y = n * t + y0
z = p * t + z0

t - параметр
```

### Уравнение прямой в пространстве, проходящей через две точки

```

M1 (x1; y1; z1) ∈ L
M2 (x2; y2; z2) ∈ L
M  (x; y; z) - произвольная точка прямой

              /
             M2
 _  /       /
 s /       M
  /       /
         M1
        /
       / L
___
M1M = {x - x1; y - y1; z - z1}
____
M1M2 = {x2 - x1; y2 - y1; z2 - z1}

___    ____    x  - x1   y  - y1   z  - z1
M1M || M1M2 => _______ = _______ = _______
               x2 - x1   y2 - y1   z2 - z1
```

### Общее уравнение прямой в пространстве

Прямую в пространстве можно задать как линию пересечения как линию пересечения двух параллельных плоскостей
```

 |A1x + B1y + C1z + D1 = 0
<
 |A2x + B2y + C2z + D2 = 0  (5. 5)

Замечание: от общего уравнения прямой можно перейти к каноническому

Координаты точки M0 можно получить, если придать системе (5.5) одной из координат придать произвольное значение,
например: z = 0 и решить систему с двумя неизвестными.
_   __   __
s = n1 * n2
    __
где n1 = (A1, B1, C1)
    __
где n2 = (A2, B2, C2)
```

## Прямая в пространстве. Основные задачи.

```
Дано:

      x - x1   y - y1   z - z1
L1 =  ______ = ______ = ______
        m1       n1       p1
      
      x - x2   y - y2   z - z2
L2 =  ______ = ______ = ______
        m2       n2       p2

                 __   __
φ = (L1 ^ L2) = (s1 ^ s2)
__
s1 = {m1; n1; p1}
__
s2 = {m2; n2; p2}

                m1 * m2 + n1 + n2 + p1 * p2
cos φ = ____________________________________________
          _________________       __________________ 
         /  2      2      2      /   2      2      2
        √ m1  +  n1  +  p1   *  √  m2  +  n2  +  p2

            __   __
L1 ⟂ L2 <=> s1 ⟂ s2


m1 * m2 + n1 + n2 + p1 * p2 = 0

            __   __      m1    n1    p1
L1 ⟂ L2 <=> s1 ⟂ s2 <=> ___ = ___ = ___ 
                         m2    n2    p2

```
### Условие при котором две прямые лежат в одной плоскости
```
                                            __  __   ____
Прямые лежат в одной плоскости если векторы s1, s2 и M1M2 компланарны
```
![img](https://sun9-85.userapi.com/impg/9nuHO7ew9AmNmdu8NVirRyQQDAi_3KAVdXDkrw/kSAWYFC-XdA.jpg?size=1280x791&quality=96&sign=cbd1ee00c98d3c56af1899ae1fc51532&type=album)
```

| x2 - x1  y2 - y1  z2 - z1 |
|   m1        n1       p1   | = 0
|   m2        n2       p2   |

L: x - x0   y - y0   z - z0
   ______ = ______ = ______
     m        n        p

α: Ax + By + Cz + D = 0
```

### Угол между прямой и плоскостью

![img](https://sun9-16.userapi.com/impg/PifSYOZXRA8jra7KDHVnYoKAyQHi6jBZQDRYAQ/xX-Bnzn8XCs.jpg?size=1280x545&quality=96&sign=e5b327d10ac32dd2be10a7ec4243dd7c&type=album)

![img](https://sun9-21.userapi.com/impg/RyQeW6f84fAE_oT7FaiiaECmz3IUHt8jrQnJ9g/AbgIUvkHktg.jpg?size=717x1080&quality=96&sign=ab4e8e45264f10cc7f3f5f213ddab62a&type=album)

### Условие параллельности прямой и плоскости

```
                _
                s
L -----------*------->
       ^
    ___|___________
   /   |          /
  /    |_        /
 /     |s       /   
/______________/
           _   _
L || α <=> n ⟂ s <=>  A * m + B * n + C * p = 0
```

### Условие перпендикулярности прямой и плоскости

![img](https://sun9-39.userapi.com/impg/QSMd9EH1dqv-mQd7xSfVuy78K9NlhuMjYruSkQ/GocnRWM8yrg.jpg?size=1280x414&quality=96&sign=dcd476101b5f4460687fe3517662019d&type=album)

### Условие принадлежности прямой плоскости

![img](https://sun9-23.userapi.com/impg/HbtSIPIGt6Qmi3LyHAf4_N7yoVUXG3fvNo-qtQ/eOR6ix8sxcs.jpg?size=1280x448&quality=96&sign=675279bb8e2a008abb358af31bd684f1&type=album)

```

 | Am + Bn + Cp = 0
<
 | Ax0 + By0 + Cz0 + D = 0
```

### Пересечение прямой с плоскостью

![img](https://sun9-51.userapi.com/impg/0eanx7PfyGDDFn_NE3ZvcqYkAprBH6SGRxxHFg/EfeeCfy9aUU.jpg?size=1039x1080&quality=96&sign=f8bb1f0766975cc8701516fecfff2cf2&type=album)
Чтобы решить эту систему, уравнение прямой надо написать в параметрическом виде и подставить x, y, z в уравнение плоскости.
Найти параметр t. Найденный параметр опять подставить в параметрические уравнения. Найдем координату точек