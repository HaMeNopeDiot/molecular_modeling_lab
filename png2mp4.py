import cv2
import os
import glob

def images_to_video(image_folder='pct', output_video='output.mp4', fps=10, pattern='dislin_*.png'):
    """
    Преобразует изображения вида dislin_XXXX.png из папки image_folder в MP4 видео.

    Аргументы:
        image_folder (str): Путь к папке с изображениями (по умолчанию 'pct').
        output_video (str): Имя выходного видеофайла (по умолчанию 'output.mp4').
        fps (int): Количество кадров в секунду (по умолчанию 10).
        pattern (str): Шаблон имени файлов (по умолчанию 'dislin_*.png').
    """
    # Получаем список файлов по шаблону
    image_files = glob.glob(os.path.join(image_folder, pattern))
    
    # Сортируем по номеру в имени (dislin_0001.png → 1, и т.д.)
    image_files.sort(key=lambda x: int(os.path.splitext(os.path.basename(x))[0].split('_')[-1]))

    if not image_files:
        print("⚠️ Нет изображений по заданному шаблону!")
        return

    # Определяем размеры видео по первому изображению
    first_image = cv2.imread(image_files[0])
    if first_image is None:
        raise ValueError("Не удалось прочитать первое изображение.")
    
    height, width, layers = first_image.shape
    size = (width, height)

    # Выбираем кодек для MP4
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # или 'avc1' для H.264, но может не работать везде
    video = cv2.VideoWriter(output_video, fourcc, fps, size)

    if not video.isOpened():
        raise RuntimeError("Не удалось создать видеофайл. Проверьте путь и кодек.")

    # Добавляем каждый кадр в видео
    for img_path in image_files:
        print(f"Bugaga  {img_path}")
        frame = cv2.imread(img_path)
        if frame is None:
            print(f"⚠️ Пропущен файл: {img_path} (не удалось прочитать)")
            continue
        # Убедимся, что размер совпадает
        if frame.shape[1] != width or frame.shape[0] != height:
            frame = cv2.resize(frame, size)
        video.write(frame)

    # Освобождаем ресурсы
    video.release()
    cv2.destroyAllWindows()

    print(f"✅ Видео сохранено: {output_video}")