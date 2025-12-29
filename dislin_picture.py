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
    dislin.metafl ('pdf') # 'pdf' 'png' 'cons'
    # Инициализация DISLIN
    dislin.disini ()
    # Рисование рамки вокруг страницы
    dislin.pagera ()
    # Использование аппаратных шрифтов
    dislin.hwfont ()
    # Включение освещения для 3D-объектов
    dislin.light ('on')
    # Настройка материала: слабое зеркальное отражение
    dislin.matop3 (0.02, 0.02, 0.02, 'specular')

    # Отключение отсечения в 3D
    dislin.clip3d ('none')
    # Позиция и размер системы координат
    dislin.axspos (200, 2500)
    dislin.axslen (1600, 1600)
    dislin.nograf()

    # Автоматическое определение количества цифр в метках осей
    # dislin.labdig (-1, 'xyz')
    # Горизонтальное расположение меток осей
    # dislin.labl3d ('hori')
    dislin.graf3d (-2., 2., 0., 0.5, -2., 2., 0., 0.5, -2., 2., 0., 0.5)

    dislin.shdmod ('smooth', 'surface')

    iret = dislin.zbfini()
    dislin.matop3 (1.0, 0.0, 0.0, 'diffuse')
    

    for i in range (0, len(atoms[0])):
        dislin.sphe3d (atoms[iteration][i].x, atoms[iteration][i].y, atoms[iteration][i].z, 0.25, 50, 25)        



    # Завершение работы с Z-буфером
    dislin.zbffin ()

    # Завершение работы с DISLIN
    dislin.disfin ()


from pathlib import Path
import shutil
from pdf2image import convert_from_path
from png2mp4 import images_to_video
import os

def pdf_to_png(pdf_path, output_path, page_number=0, dpi=200):
    """
    Конвертирует одну страницу PDF в PNG
    
    Args:
        pdf_path: путь к PDF файлу
        output_path: путь для сохранения PNG
        page_number: номер страницы (начиная с 0)
        dpi: качество изображения
    """
    # Конвертируем PDF в список изображений
    images = convert_from_path(pdf_path, dpi=dpi)
    
    # Проверяем, существует ли запрашиваемая страница
    if page_number < len(images):
        # Сохраняем нужную страницу
        images[page_number].save(output_path, 'PNG')
        print(f"Страница {page_number+1} сохранена как {output_path}")
    else:
        print(f"Страница {page_number+1} не существует в PDF")
    
    return len(images)

if not os.path.exists("pct"):
        os.makedirs("pct")

for i in range(len(atoms)):
    create_graph(atoms, i)
    source = Path('dislin.pdf')
    srt_i = str(i)
    while len(srt_i) < 4:
        srt_i = "0" + srt_i
    destination = Path(f"pdf_dir/dislin_{srt_i}.pdf")
    # Создаём целевую директорию, если её нет
    destination.parent.mkdir(parents=True, exist_ok=True)
    # Перемещаем файл
    shutil.move(str(source), str(destination))

    pdf_to_png(destination, Path(f"pct/dislin_{srt_i}.png"))    

images_to_video(image_folder="pct", output_video="result.mp4", fps=20)
    