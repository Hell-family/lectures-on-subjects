## Оценка согласованности суждений экспертов

Для оценки степени согласованности мнения экспертов используются статистические показатели.

**Дисперсия** ($\sigma^2$) - средняя из квадраирв отклонений значений оценки объекта экспертом $S(x_s)$ от средней оценкий ($\overline{x}$):

$\displaystyle{\sigma^2=\frac{\sum^d_{s=1}(x_s-\overline{x})^2}{d}}$

Среднее квадратическое отклонение $\sigma=\sqrt{\sigma^2}$

Коэффициент вариации $V=\frac{\sigma}{\overline{x}}\cdot 100\%$

Степень согласованности мнений экспертовц считается удовлетворительной, если коэффициент вариации не превышает значения $30\%$, и хорошей, когда коэффициент вариации не более $20\%$.

## Коэффицикет конкордации

$\displaystyle{W=\frac{12\times\sum^m_{i=1}(\sum^d_{s=1}r_{is}-\overline{r})^2}{d^2\times(m^3-m)}}$

$\displaystyle{\overline{r}=\frac{1}{m}\sum^m_{i-1}\sum^d_{s=1}r_{is}}$

$W$ - коэффициент (от $0$ до $1$)

$r_{is}$ - ранг, присваиваемый объекту $i$ экспертом $s$

$d$ - количество экспертов

$m$ - количество объектов

Мнение экспертов можно считать согласованным, при выполенении следующего условия:

$\xi^2_{набл}>\xi^2(\alpha,m-1)\\\xi^2_{набл}=m(d-1)W$

$\xi$ - критерий согласия Пирсона

$\alpha$ - уровень значимости

$m-1$ - число степенеей свободы