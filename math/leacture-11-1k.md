# Дифференциальное исчисление

## 1.1 Определение производной

Пусть функция y = f(x) определена на интервале (a; b). Аргументу x придадим некоторое приращение Δx:

```
x + Δx ∈ (a; b)
```

Найдём соответствующее приращение функции

```
Δy = f(x + Δx) - f(x)
```

![img](https://sun9-67.userapi.com/impg/0amKPqd4z-fIoESsYk9ecIUcWkkWlLCr2et5sA/Ps-6gjLJ8C8.jpg?size=645x242&quality=96&sign=a0c5046f2a6f12c2d9e7d59e02999261&type=album)

Итак, по определению

```
          f(x + Δx) - f(x)
y' = lim  ________________
    Δx->0       Δx
```

Функция y = f(x), имеющая производную в каждой точке интервала (a; b), называется **дифференцируемой** в этом интервале; операция нахождения производной функции называется **дифференцированием**

Значение производной y = f(x) в точке x0 обозначается одним из символов: 

```
y'(x0); f'(x0); y'|
                   x0
```

Если функция y = f(x) описывает какой-либо физический процесс, то f'(x) есть скорость протекания этого процесса - физический смысл производной

## 1.2 Геометрический смысл производной

Возьмём на непрерывной кривой две точки M и M1:

![img](https://sun9-3.userapi.com/impg/hDt9TllQC2vbHzrKF-QpeVF_qIDEXOgHCkzz_Q/1fwTdQvXgzc.jpg?size=396x263&quality=96&sign=ded3f1ef7514bca586d67a8b7b23fa55&type=album)

Через точки M и M1 проведём секущую и обозначим через φ угол наклона секущей

```
       Δy   f(x + Δx) - f(x)
tg φ = __ = ________________
       Δx          Δx
```

При Δx -> 0 в силу непрерывности функции Δy также стремится к нулю, поэтому точка M1 неограниченно приближается по кривой к точке M, а секущая MM1 переходит в касательную

```

φ -> α => lim  φ = α  => lim  tg φ = tg α =>
          Δx->0         Δx->0



         f(x + Δx) - f(x)
=> lim   ________________ = tg α = k = y'
   Δx->0        Δx
```


Производная равна угловому коэффициенту касательной к графику функции y = f(x) в точке, абсцисса которой равна x: f'(x) = k

Если точка касания M имеет координаты (x0; y0), угловой коэффициент касательной есть k = f'(x0)

y - y0 = f'(x0)(x - x0)

Прямая, перпендикулярная касательной в точке касания, называется нормалью к кривой

```
             1
y - y0 = - ______ (x-x0)
           f'(x0)
```

## 1.3 Связь между непрерывностью и дифференцируемостью функции

**Теорема:** Если функция f(x) дифференцируема в некоторой точке, то она непрерывна в ней

**Обратное утверждение не верно:** непрерывная функция может не иметь производной

Пример:

![img](https://sun9-1.userapi.com/impg/cw3QYlmOvj5FQce0FmjVQg7poSc3-CYbBgE7Hw/PnxiMlXBJ7g.jpg?size=569x211&quality=96&sign=d25d96e61643e0673560ce6ee0b4d733&type=album)

## 1.4 Правила дифференцирования

Пусть u(x), v(x) и w(x) - дифференцируемые в некотором интервале (a; b) функции, C - постоянная

```
(C)' = 0

(u ± v)' = u' ± v'

(u * v)' = u' * v + u * v' => (C * u)' = C * u'

(u * v * w)' = u' * v * w + u * v' * w + u * v * w'

           u' * v - u * v'              -C * v'
(u / v)' = ______________ => (C / v)' = _______
                 2                          2
                v                          v
```

## 1.5 Таблица производных

![img](https://sun9-63.userapi.com/impg/aPpwztLWAxV2SaSqKg8NFtNYyQ0XbACRZ3-FbQ/fIKEvQ6TixU.jpg?size=344x511&quality=96&sign=886b2002614a02fcf0d6196d7a2d9b05&type=album)

## 1.6 Производная сложной функции

Пусть y = f(u) и u = φ(x), тогда y = f(φ(x)) - сложная функция с промежуточным аргументом u и независимым аргументом x

**Теорема:**

![img](https://sun9-31.userapi.com/impg/IBQPEeUXV3laX9o2lMNJ8C84TzQvrs_D2LbXxQ/l6qhHFcj6qo.jpg?size=499x252&quality=96&sign=4de65e5ba42b20e9db11ea2a92f7c953&type=album)

Пример:

![img](https://sun9-32.userapi.com/impg/DzSbrmZ7NU8XNHhTBj5CJwYBFlm9Lp8a08W-JQ/uuIohlMnDjw.jpg?size=549x395&quality=96&sign=dd7353864d62834063c8c1c34df7dbd4&type=album)

![img](https://sun9-80.userapi.com/impg/7g1hKoRz83nJkfdL4t3EI8JmtYXM7eratgdeEA/5BlluBEhafs.jpg?size=543x398&quality=96&sign=1beab0e2a0119cfb1b824a194a47f9d3&type=album)

## 1.7 Производная неявно заданной функции

Если функция задана уравнением y = f(x), разрешенным относительно y, то говорят, что функция задана в явном виде. Под неявным заданием функции понимают задание функции в виде уравнения не разрешенного относительно y:

F(x; y) = 0

```
Для нахождения производной неявно заданной функции необходимо продифференцировать уравнение по x, рассматривая при этом y как функцию от x, и полученное выражение разрешить относительно производной
```

![img](https://sun9-58.userapi.com/impg/u4BE8dPDGf8G2DnPvGwEpa9T2eBAvh1t6eXB6Q/i1fq2hsM7As.jpg?size=658x182&quality=96&sign=c531d24675a07390587efe6ec3e61b2c&type=album)

## 1.8 Производная функции, заданной параметрически

Пусть зависимость между аргументом x и функцией y задана параметрически

```
 | x = x(t),
<               где t - параметр
 | y = y(t),
```

<div style="display: flex; align-items: center">Тогда: <img style="margin-left: 20px;" src="https://sun9-67.userapi.com/impg/JlA9_JGbg3WNLCpa23HVzuJ7n6NFTxOKE4ZBPQ/eqc6I0cAAiQ.jpg?size=63x54&quality=96&sign=d9697e69e9d9bd81a4cd85773e8290bf&type=album" /></div>

![img](https://sun9-71.userapi.com/impg/nV5OqGqWnsn3TA1V80GEOFpnjBEsWgoTLDoFVQ/IYMSAsvtd_o.jpg?size=596x199&quality=96&sign=aeb8be2ece3c106c1b17d3b09f357c6d&type=album)

## 1.9 Логарифмическое дифференцирование

В ряде случаев для нахождения производной целесообразно заданную функцию сначала ***прологарифмировать***, а затем результат ***продифференцировать***

Такую операцию называют ***логическим дифференцированием***

![img]()

Пусть u = u(x) и v = v(x) - дифференцируемые функции.
```
                v(x)
Функция y = u(x)     называется степенно-показательной
```

Производная такой функции находится только с помощью логарифмического дифференцирования

![img](https://sun9-48.userapi.com/impg/KmeQH1T5iBRa2hrmmoUOIOzfBPu3C-gnXZL2eg/pPLWxp5FdXM.jpg?size=1060x369&quality=96&sign=fbc18d9805eaadd891115ad73e015712&type=album)

## 1.10 Производные высших порядков

Производная y' = f'(x) называется производной первого порядка. Её можно рассмаривать как функцию от x и если эта функция f'(x) дифференцируема, то её производная называется производной второго порядка.


<div style="display: flex; align-items: center">Обозначается: <img style="margin-left: 20px;" src="https://sun9-33.userapi.com/impg/NkAXkeVY4rD6uDaFvecn7ADDrpUOmPTaBd8RFQ/GGJdmk-9icY.jpg?size=120x59&quality=96&sign=abeead76f28b3cdf66667baf0cf39654&type=album" /></div>

Аналогично y'''  = (y'')' - производная 3-го порядка

<div style="display: flex; align-items: center">Производная n-го порядка называется производная от производной (n - 1)-го порядка: <img style="margin-left: 20px;" src="https://sun9-30.userapi.com/impg/KbtxByyHzdGcIyNPrRpYChUyBE9Dbsi0E1xkUQ/WEl8z58I8tA.jpg?size=106x50&quality=96&sign=1f3a8192142ec525fcea539494c71bae&type=album" /></div>

Производные порядка выше первого называются **производными высших порядков**

![img](https://sun9-27.userapi.com/impg/1FwM2I40QGTMxPjqg1qWC3Ok-STp8jI2xEBtFA/qlLH5YebwtI.jpg?size=613x551&quality=96&sign=685e141bc32a5fe2df1d51ac21705562&type=album)

## 1.11 Дифференциал функции

Пусть функция y = f(x) имеет в точке х0 отличную от нуля производную:

```
               Δf
f'(x0) = lim  ____ ≠ 0
        Δx->0  Δx
```

По теореме 3.1. в теме "Предел функции", в окрестности точки х0 имеет место равенство:

![img](https://sun9-47.userapi.com/impg/YYtzT7bbxqif2MAJ90YV2w7vqWUo-BLuTj16gA/dqcngkCsnUA.jpg?size=554x173&quality=96&sign=919c789f9c37c3837c24af737fc3a948&type=album)

Следовательно, f'(x0)Δx - главная часть приращения функции

Дифференциалом функции y = f(x) в точке x0 называется главная часть приращения этой функции в точке x0 и обозначается dy

dy = f'(x0)Δx

Дифференциал независимой переменной x равен приращению Δx

dy = dx = x' * Δx = 1 * Δx, => dx = Δx

dy = f'(x)dx

Следовательно, dy/dx = f'(x)

т.е. значение производной равно отношению дифференциалов

![img](https://sun9-24.userapi.com/impg/gOa_GFFfwk-1p0qbcmGPnotCPYS3HQ8It3J4zQ/4YIIfFZBBiY.jpg?size=707x736&quality=96&sign=af143346dc3f0fc4ca31e1f38e4b8dde&type=album)