# Растровая графика

**Растровое изображение** представляется в виде прямоугольной матрицы, каждая ячейка которой представлена цветной точкой. Основой растрового представления является пиксель (точка) с указанием его цвета. Изображение представляется ввиде большого количества точек. Чем их больше - тем визуально качественнее изображение и больше размер файла. Т.е. одна и та же картинка может быть представленна с лучшим/худшим качеством в соответствии с количеством точек на единицу длины. Количество точек на единицу длины называется разрешением (DPI). PPI - количество точек на дюйм. 

**Цифровое изображение** - это совокупность пикселей. Каждый пиксель характеризуется координатами X и Y и яркостью V(x, y). Т.к. пиксели имеют дискретный характер, то координаты их дискретной величины обычно целые и рациональные числа. В случае цветного изображения каждый пиксель характеризуется координатами X и Y b и тремя яркостями:
- Яркость красного Vr
- Яркость синего Vb
- Яркость зеленого Vg

Комбинируя данные три цвета можно получить большое количество различных оттенков. В случае если хотя бы одна из характеристик изображения не является числом, то изображение относится к виду аналоговых. Например: фотографии и голограммы. Для работы с такими изображениями существуют специальные методы в частности оптические преобразования. Цвет любого пикселя запоминается с помощью комбинаций видов. Чем больше видов используется, тем больше оттенков цветов можно получить. 

Для градации обычно отводится один байт (1 байт = 256 градаций), причем 0 - это черный цвет, а 255 - белый. В случае цветного изображения отводится по байту на градации яркостей всех трёх цветов. Возможно кодирование и другие количество бит, но человеческий глаз способен различать 8 градаций на каждый цвет. Хотя специальная аппаратура может потребовать и больно точную передачу цветов. Цвета описываемые 24 битами обеспечивают более 16млн доступных цветов и их часто называют естественными цветами

В цветовой палитре каждый пиксель описан цветовым кодом. Поддерживается связь этого кода с таблицей цветов, состоящей из 256 ячеек. Разрядность каждой ячейки - 24 разряда. На выходе каждой ячейки - по 8 разрядов на красный, зелёный и синего цветов. Цветовое пространство, образуемое интенсивностями красного, зеленого и синего представляют в виде цветового круга.

![img](https://studfile.net/html/2706/1276/html_n8l3Dzht2h.oFkE/htmlconvd-HvnFj5_html_fbea4bc08adbe5.jpg)

Вершины куба A, B, C являются максимальными интенсивностями зеленого, синего и красного соответственно, а треугольник, которые они образуют, называется треугольником Паскаля. Периметр этого треугольника соответствует максимально насыщенным цветам. Цвет максимальной насыщенности содержит всегда только две компоненты. На отрезке OD находятся оттенки серого, причем тока O соответствует черному, а точка D белому цвету.

## Виды растров

**Растр** – это порядок расположения точек (растровых элементов). На рис. 2. изображен растр, элементами которого являются квадраты, такой растр называется прямоугольным, именно такие растры наиболее часто используются.

Наиболее часто используются прямоугольные растры. Также в качестве растрового элемента могут использоваться фигуры другой формы. Например: треугольные, шестиугольные... При этом все фигуры должны отвечать следующим требованиям:

1. все фигуры должны быть одинаковые
2. должны полностью покрывать плоскость без наезжания и дырок

Файлы растровой графики занимают большое количество памяти компьютера. Некоторые картинки занимают большой объем памяти из–за большого количества пикселов, любой из которых занимает некоторую часть памяти. Наибольшее влияние на количество памяти занимаемой растровым изображением оказывают три факта:

1. размер изображения
2. битовая глубина цвета
3. формат файла, используемого для хранения изображения.

Существует прямая зависимость размера файла растрового изображения. Чем больше в изображении пикселей, тем больше размер файла. Разрешающая способность изображения на величину файла никак не влияет. Разрешающая способность оказывает эффект на размер файла только при сканировании или редактировании изображений.

Связь между битовой глубиной и размером файла непосредственная. Чем больше битов используется в пикселе, тем больше будет файл. Размер файла растровой графики сильно зависит от формата выбранного для хранения изображения. При прочих равных условиях, таких как размеры изображения и битовая глубина существенное значение имеет схема сжатия изображения. Например, BMP файл имеет, как правило, большие размеры, по сравнению с файлами PCX и GIF, которые в свою очередь больше JPEG файла.

## Достоинства и недостатки растровой графики

### Недостатки:

1. Растровые изображения занимают большое количество памяти. 
2. Проблема редактирования растровых изображений, так как большие растровые изображения занимают значительные массивы памяти, то для обеспечения работы функций редактирования таких изображений потребляются так же значительные массивы памяти и другие ресурсы компьютера.

### Достоинства:

1. Эффективно представляет реальные образы.
2. Растровые изображения могут быть очень легко распечатаны на таких принтерах, потому что компьютерам легко управлять устройством вывода для представления отдельных пикселов с помощью точек.

## Сжатие растровой графики

Иногда характеристики растрового изображения записывают в такой форме: 1024x768x24. Это означает, что ширина изображения равна 1024 пикселям, высота – 768 и глубина цвета равна 24. 1024x768 – рабочее разрешение для 15 – 17 дюймовых мониторов. Несложно посчитать, что размер несжатого изображения с такими параметрами будет равен 1024*768*24 = 18874368 байт. Это более 18 мегабайт – слишком много для одной картинки, особенно если требуется хранить несколько тысяч таких картинок – это не так уж много по компьютерным меркам. Поэтому компьютерную графику используют почти всегда в сжатом виде.

RLE (Run Length Encoding) – метод сжатия, заключающийся в поиске последовательностей одинаковых пикселей в сточках растрового изображения.

LZW (Lempel–Ziv–Welch) – более сложный метод, ищет повторяющиеся фразы – одинаковые последовательности пикселей разного цвета. Каждой фразе ставится в соответствие некоторый код, при расшифровке файла код замещается исходной фразой.

При сжатии файлов формата JPEG (с потерей качества) изображение разбивается на участки 8x8 пикселей, и в каждом участке их значение усредняется. Усреднённое значение располагается в левом верхнем углу блока, остальное место занимается меньшими по яркости пикселями. Затем большинство пикселей обнуляются. При расшифровке нулевые пиксели получают одинаковый цвет. Затем к изображению применяется алгоритм Хаффмана. Он основан на теории вероятности. Начало элемента изображения сортируется по частоте случайности. Затем строется кодовое дерево Хаффмана. Каждому элементу предоставляется кодовое слово. При стремлении размера изображения к бесконечности. Достигается максимальное сжатие. Этот алгоритм также применяется в архиваторах