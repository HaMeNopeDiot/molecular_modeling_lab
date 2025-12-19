#! /usr/bin/env python
import dislin
import load_data
import shutil


atoms = load_data.load_data()


def create_graph(atoms, iteration):
    # Координаты точек в 3D-пространстве для сфер и концов соединений
    x = [10., 20., 10., 20., 5., 15., 25., 5., 15., 25., 
        5., 15., 25., 10., 20., 10., 20.]
    y = [10., 10., 20., 20., 5., 5., 5., 15., 15., 15.,
        25., 25., 25., 10., 10., 20., 20.]
    z = [5., 5., 5., 5., 15., 15., 15., 15., 15., 15.,
        15., 15., 15., 25., 25., 25., 25.]  

    # Установка формата страницы А4 В портретной ориентации
    dislin.setpag ('da4p')
    # Режим отображения: белый на черном (Фон)
    dislin.scrmod ('revers') # 'norev' 'auto' 'revers'
    # Вывод
    dislin.metafl ('png') # 'pdf' 'png' 'cons'
    # Инициализация DISLIN
    dislin.disini ()
    # Рисование рамки вокруг страницы
    dislin.pagera ()
    # Использование аппаратных шрифтов
    dislin.hwfont ()
    # Включение освещения для 3D-объектов
    dislin.light ('on')
    # Настройка материала: слабое зеркальное отражение
    dislin.matop3 (0.02, 0.02, 0.02, 'diffuse') # 'diffuse' 'ambient' 'specular' 'emission'

    # Отключение отсечения в 3D
    dislin.clip3d ('none')
    # Позиция и размер системы координат
    dislin.axspos (200, 2500)
    dislin.axslen (1800, 1800)
    dislin.nograf()

    # Автоматическое определение количества цифр в метках осей
    # dislin.labdig (-1, 'xyz')
    # Горизонтальное расположение меток осей
    # dislin.labl3d ('hori')
    # Определение диапазонов осей: X(0-30), Y(0-30), Z(0-30) с шагом 5
    dislin.graf3d (-2., 2., 0., 0.5, -2., 2., 0., 0.5, -2., 2., 0., 0.5)
    # Отображение заголовка
    #dislin.title ()

    # 'smooth' 'flat' 'none' / 'surface' 'lines' 'border'
    # Режим сглаженного затенения поверхностей
    dislin.shdmod ('smooth', 'surface')

    # Начало записи в Z-буфер (для правильного отображения 3D)
    iret = dislin.zbfini()
    # Настройка красного диффузного материала
    dislin.matop3 (1.0, 0.0, 0.0, 'diffuse')
    # Создание 17 красных сфер радиусом 2.0 с 50x25

    for i in range (0, len(atoms[0])):
        dislin.sphe3d (atoms[iteration][i].x, atoms[iteration][i].y, atoms[iteration][i].z, 0.25, 50, 25)        

    # Настройка 2 диффузного материала
    dislin.matop3 (0.0, 1.0, 0.0, 'diffuse')

    # Завершение работы с Z-буфером
    dislin.zbffin ()

    # Завершение работы с DISLIN
    dislin.disfin ()


from pathlib import Path
import shutil

from png2mp4 import images_to_video

for i in range(len(atoms)):
    create_graph(atoms, i)
    source = Path('dislin.png')
    srt_i = str(i)
    while len(srt_i) < 4:
        srt_i = "0" + srt_i
    destination = Path(f"pct/dislin_{srt_i}.png")
    # Создаём целевую директорию, если её нет
    destination.parent.mkdir(parents=True, exist_ok=True)
    # Перемещаем файл
    shutil.move(str(source), str(destination))

images_to_video(image_folder="pct", output_video="result.mp4", fps=20)
    