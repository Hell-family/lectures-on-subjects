# Кванторы

Ɐ - квантор всеобщности (для любого, для всех)

∃ - квантор существования (существуют, некоторый)

Пусть P(x) - одноместный предикат, определённый на множестве M, тогда для всех X выражение P(x) означает истинное высказывание, если P(x) - истинное для любого X из множества M

ⱯxP(x) - означает область истинности с область значений переменной X

∃xP(x) - истинна, если ∃x ∈ M, для каждого P(x) - истинно.

Истинность высказывания ∃xP(x) означает, что область истинности предиката не является пустой (Ip ≠ ∅)

Отметим, что если некоторый предикат P(x) определён на конечном множестве M, то выражение для любого X:
```
ⱯxP(x) = P(a1) ^ P(a2) ... ^ P(an)

∃xP(x) = P(a1) v P(a2) ... v P(an)
```

Кванторы можно рассматривать как обобщение логических связок.

Квантор всеобщности обозначает конъюнкцию, а кванторы существования - дизъюнкцию

Для высказываний ⱯxP(x), ∃xP(x) говорят, что они получены из предиката P навешиванием кванторов всеобщности (или квантор существования)

Переменная, на которую навешен квантор, называется **связной** пременной.

Навешивать квантры можно и на многоместные предикаты и вообще на любые логические выражения.

Выражения на которые навешивается квантр всеобщности или существования называется **областью действия квантра**. Все входящие переменные в это логическое выражение являются связными.

Переменные которые не являются связными называются **свободными**.

Рассмотрим предикат двух переменных. К этому предикату можно применять квантовые операции либо к X либо к Y, либо к обеим переменным одновременно. При этом получим следующее высказывание.

```
ⱯxP(x, y) ⱯyP(x, y)
∃xP(x, y) ∃yP(x, y)

ⱯxⱯyP(x, y) ⱯyⱯxP(x, y)
∃x∃yP(x, y) ∃y∃xP(x, y)

Ɐx∃yP(x, y) ∃xⱯyP(x, y)
Ɐy∃xP(x, y) ∃yⱯxP(x, y)
```

В общем случае изменение порядка следования кванторов изменяет смысл высказывания и его логическое значение.

## Формулы логики предикатов

1) Всякая логическая переменная - это _формула_.
2) Если P - n-местный предикат, то P(x1, x2, ... , xn) - формула, причём все переменные будут свободные.
3) Если A - формула, то ¬A - тоже формула с теми же свободными и связанными переменными
4) Если A и B - формулы, то выражением A ^ B, A v B, A -> B, A <-> B, A ⊕ B, в которых свободные переменные формул A и B остаются свободными, а связанные остаются связанными. В формулах A и B нет таких переменных, которые были бы связанными в одной формуле и свободными в другой.
5) Если A - это некоторая формула, содержащее некоторую свободную переменную X, то выражение ⱯxA и ∃xⱯ - тоже формулы. При этом переменная X теперь является связанной переменной

_Замечание:_ Каждая формула алгебры высказываний является формулой логики предикатов

_Пример 1:_

(Ɐx∃yP(x, y, u)) -> ExQ(x, w) - формула

_Пример 2:_

(ⱯxP(x, y)) <-> Q(x, z) - не является формулой