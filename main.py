# # # Модуль numpy
# # import numpy as np
# #
# # # функция активации: f(x) = 1 / (1 + e^(-x))
# # def sigmoid(x):
# #     return 1 / (1 + np.exp(-x))
# #
# # # Создание класса "Нейрон"
# # class Neuron:
# #     def __init__(self, w):
# #         self.w = w
# #
# #     def y(self, x):
# #         s = np.dot(self.w, x)  # Сумматор
# #         return sigmoid(s)       # функция активации
# #
# # Xi = np.array([2, 2, 2, 2])
# # xi = np.array([1, 1, 1, 1]) # Задание значений входам
# # Wi = np.array([5, 4, 3, 1])    # Веса входных сенсоров
# #
# # n = Neuron(Wi)                 # Создание объекта из класса
# # print('Y= ', n.y(Xi+xi))          # Вывод результата
# # from turtledemo.sorting_animate import instructions1
#
# # #Листинг 4.3--------------------------104 стр.
# #
# # # Искусственный нейрон (персептрон)
# # def perceptron(Sensor):
# #     b = 7  # Порог функции активации
# #     s = 0  # Начальное значение суммы
# #     for i in range(15):  # цикл суммирования сигналов от сенсоров
# #         # Преобразуем сигнал ('0' или '1') в число и умножаем на вес связи
# #         s += int(Sensor[i]) * weights[i]
# #
# #     if s >= b:
# #         return True  # Сумма превысила порог
# #     else:
# #         return False  # Сумма меньше порога
# #
# #
# # # Проверка работы искусственного нейрона (персептрона)
# # num1 = list('001001001001001')
# # num2 = list('111001111100111')
# # weights = [1 for _ in range(15)]  # Присвоение значений всем связям w=1
# #
# # print(f"Сигналы: {num1}")
# # print(f"Ответ персептрона: {perceptron(num1)}")
# # print(f"Сигналы: {num2}")
# # print(f"Ответ персептрона: {perceptron(num2)}")
#
# # import cv2
# # import numpy as np
# #
# # img = cv2.imread('image/1234.jpg')
# #
# # img = cv2.resize(img,(img.shape[1] // 2,img.shape[0] // 2))
# # img = cv2.GaussianBlur(img,(9,9),0)
# # img = cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)
# #
# # img = cv2.Canny(img,100,100)
# #
# #
# # kernel = np.ones((5,5), np.uint8)
# # img = cv2.dilate(img, kernel, iterations=1)
# # img = cv2.erode(img, kernel, iterations=1)
# #
# # cv2.imshow('Result', img)
# #
# # cv2.waitKey(0)
# #
# #
# #
#
# #
# # import cv2
# # import numpy as np
# #
# #
# # photo = np.zeros((450,450,3) , dtype = 'uint8')
# #
# # # RGB -  стандарт
# # # BGR - формат в OpenCV
# #
# #
# # # photo[:] = 171,77,255
# # # photo[100:150,280:280] = 171,77,255
# #
# # # cv2.rectangle(photo, (0,0),(100, 100),(171,77,255),thickness=3)
# # cv2.rectangle(photo, (0,0),(100, 100),(171,77,255),thickness=cv2.FILLED)
# #
# # cv2.line(photo,(0,photo.shape[0]//2),(photo.shape[1], photo.shape[0]//2),(171,77,255),thickness=3)
# #
# #
# # # cv2.circle(photo,(photo.shape[1]//2, photo.shape[0]//2), photo.shape[0]//2),(171,77,255),thickness=3)
# #
# # cv2.putText (photo, 'itProgger',(100,150), cv2.FONT_HERSHEY_TRIPLEX,1,(255,0,0),3)
# #
# # cv2.imshow('Photo',photo)
# # cv2.waitKey(0)
# #
#
#
# # import cv2
# # import numpy as np
# #
# # cap = cv2.VideoCapture("vid/pzr.mp4")
# #
# # while True:
# #     success, img = cap.read()
# #     if not success:
# #         break
# #
# #     # img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
# #
# #     # 1. Размытие по Гауссу (убирает шум)
# #     img = cv2.GaussianBlur(img, (9, 9), 0)
# #
# #     # 2. Перевод в оттенки серого
# #     img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# #
# #     # 3. Выделение границ (контуров) методом Кэнни
# #     img = cv2.Canny(img, 30, 30)
# #
# #     # 4. Создание ядра для морфологических операций
# #     kernel = np.ones((5, 5), np.uint8)
# #
# #     # 5. Расширение (утолщение линий)
# #     img = cv2.dilate(img, kernel, iterations=1)
# #
# #     # 6. Сжатие (эрозия — утончение линий)
# #     img = cv2.erode(img, kernel, iterations=1)
# #
# #     cv2.imshow('Result', img)
# #
# #     # Ожидание нажатия клавиши (в оригинале урока строка ниже)
# #     if cv2.waitKey(1) & 0xFF == ord('q'):
# #         break
# #
# # cap.release()
# # cv2.destroyAllWindows()
#
# # img =cv2.imread("image/1234.jpg")
# #
# #
# # # img = cv2.flip(img, -1)
# # def rotate(img_param,angle):
# #     height,width = img.shape[:2]
# #     point =  (width//2,height//2)
# #
# #     mat = cv2.getRotationMatrix2D(point,angle,1)
# #     return  cv2.warpAffine(img_param,mat,(width,height))
# #
# # img = rotate(img,90)
# #
# # cv2.imshow("res",img)
# #
# # cv2.waitKey(0)
#
#
# #
# # import cv2                  # код не работает - (исправить по возможности!)
# # image_path = "image\s.jpg"
# # face_cascade = cv2.CascadeClassifier('# не рбаотает код')
# # image = cv2.imread(image_path)
# # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# # faces = face_cascade.detectMultiScale(
# #     gray,
# #     scaleFactor= 1.1,
# #     minNeighbors= 5,
# #     minSize=(10, 10)
# # )
# # faces_detected = "Лиц обнаружено: " + format(len(faces))
# # print(faces_detected)
# # # Рисуем квадраты вокруг лиц
# # for (x, y, w, h) in faces:
# #     cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 0), 2)
# # viewImage(image,faces_detected)
# #
# #
#
# # import cv2
# # from ultralytics import YOLO
# # import numpy as np
# # import os
# #
# #
# # def create_test_video(filename):
# #     """Создает простое тестовое видео программно"""
# #     print("Создание тестового видео...")
# #     width, height = 640, 480
# #     fps = 30
# #     duration_sec = 5  # длительность 5 секунд
# #
# #     fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# #     out = cv2.VideoWriter(filename, fourcc, fps, (width, height))
# #
# #     for i in range(duration_sec * fps):
# #         img = np.zeros((height, width, 3), dtype=np.uint8)
# #
# #         # Рисуем "человека" (просто прямоугольник, чтобы модель его увидела как объект,
# #         # но лучше использовать реальное фото. Для теста нарисуем похожие фигуры)
# #         # Центр экрана
# #         cx, cy = width // 2, height // 2
# #
# #         # Двигаем объект
# #         offset = int(100 * np.sin(i / 10))
# #
# #         # Рисуем зеленый прямоугольник (имитация человека)
# #         cv2.rectangle(img, (cx - 50 + offset, cy - 100), (cx + 50 + offset, cy + 100), (0, 255, 0), -1)
# #
# #         # Рисуем красный круг (имитация предмета)
# #         cv2.circle(img, (cx + 150, cy), 30, (0, 0, 255), -1)
# #
# #         out.write(img)
# #
# #     out.release()
# #     print(f"Тестовое видео создано: {filename}")
# #
# #
# # def process_video(input_path, output_path):
# #     # 1. Загружаем модель сегментации
# #     print("Загрузка модели YOLOv8...")
# #     model = YOLO('yolov8n-seg.pt')
# #
# #     # 2. Открываем видеофайл
# #     cap = cv2.VideoCapture(input_path)
# #
# #     if not cap.isOpened():
# #         print(f"Ошибка: Не удалось открыть файл {input_path}")
# #         return
# #
# #     # Получаем параметры видео
# #     width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# #     height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# #     fps = cap.get(cv2.CAP_PROP_FPS)
# #
# #     if fps == 0:
# #         fps = 30
# #
# #     # 3. Настраиваем запись
# #     fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# #     out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
# #
# #     print(f"Обработка видео: {width}x{height}, FPS: {fps}")
# #     print("Идет обработка...")
# #
# #     frame_count = 0
# #
# #     try:
# #         while True:
# #             ret, frame = cap.read()
# #             if not ret:
# #                 break
# #
# #             frame_count += 1
# #             if frame_count % 10 == 0:
# #                 print(f"Обработан кадр: {frame_count}")
# #
# #             # 4. Распознавание объектов
# #             results = model(frame, stream=True, verbose=False, conf=0.25)  # conf пониже, чтобы ловило больше
# #
# #             for r in results:
# #                 img = r.orig_img
# #
# #                 if r.masks is not None:
# #                     masks = r.masks.data.cpu().numpy()
# #                     boxes = r.boxes
# #                     names = r.names
# #
# #                     for i, mask in enumerate(masks):
# #                         class_id = int(boxes.cls[i])
# #                         class_name = names[class_id]
# #                         confidence = float(boxes.conf[i])
# #
# #                         # Рисуем контур
# #                         mask_uint8 = (mask * 255).astype(np.uint8)
# #                         contours, _ = cv2.findContours(mask_uint8, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# #                         cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
# #
# #                         # Пишем текст
# #                         if len(contours) > 0:
# #                             x, y, w, h = cv2.boundingRect(contours[0])
# #                             label = f"{class_name} {confidence:.2f}"
# #
# #                             text_size = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)[0]
# #                             cv2.rectangle(img, (x, y - 20), (x + text_size[0], y), (0, 255, 0), -1)
# #                             cv2.putText(img, label, (x, y - 5),
# #                                         cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
# #
# #                 out.write(img)
# #
# #     except KeyboardInterrupt:
# #         print("\nОстановлено пользователем.")
# #
# #     finally:
# #         cap.release()
# #         out.release()
# #         cv2.destroyAllWindows()
# #         print(f"Готово! Результат сохранен в: {output_path}")
# #
# #
# # if __name__ == "__main__":
# #     input_video = "test_video.mp4"
# #     output_video = "result.mp4"
# #
# #     # Создаем тестовое видео, если его нет
# #     if not os.path.exists(input_video):
# #         create_test_video(input_video)
# #
# #     # Обрабатываем видео
# #     process_video(input_video, output_video)
#
#
#
# #
# # import numpy as np
# # import matplotlib.pyplot as plt
# #
# # #  сигнала
# # duration = 0.009  # 9 миллисекунд
# # sample_rate = 5000
# # t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
# #
# # #  звук
# # signal = (
# #     0.65 * np.sin(2 * np.pi * 440 * t) +
# #     0.35 * np.sin(2 * np.pi * 880 * t)
# # )
# #
# # # амплитуда до диапазона
# # signal /= np.max(np.abs(signal))
# #
# # plt.figure(figsize=(8, 5))
# # plt.plot(t * 1000, signal, color="gray", linewidth=1)
# # plt.title("Сгенерированный аудиосигнал")
# # plt.xlabel("Время (миллисекунды)")
# # plt.ylabel("Амплитуда")
# # plt.xlim(0, 5)
# # plt.ylim(-1, 1.5)
# # plt.grid(True, alpha=0.3)
# # plt.tight_layout()
# # plt.show()
#
#
#
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.io.wavfile import write
# from scipy.signal import resample_poly
# import soundfile as sf
#
# input_file = "kitten.mp3"
# output_file = "generated_audio.wav"
#
# #аудиофайл
# signal, sampling_freq = sf.read(input_file)
#
#
# if signal.ndim == 2:
#     signal = signal.mean(axis=1)
#
# # WAV сохраняем в формате int16
# signal_normalized = signal / np.max(np.abs(signal))
# signal_scaled = (signal_normalized * np.iinfo(np.int16).max).astype(np.int16)
# write(output_file, sampling_freq, signal_scaled)
#
#
# signal_to_plot = signal[:200]
# time_axis = 1000 * np.arange(len(signal_to_plot)) / sampling_freq
#
# plt.plot(time_axis, signal_to_plot, color="black")
# plt.xlabel("Время (миллисекунды)")
# plt.ylabel("Амплитуда")
# plt.title("Аудиосигнал kitten.mp3")
# plt.grid(True, alpha=0.3)
# plt.show()
#
# import json
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.io import wavfile
# import librosa
#
#
# # Загрузка аудиофайла kitten.mp3
# def load_audio(filename):
#     # Загрузка аудио с помощью librosa
#     audio_data, sampling_freq = librosa.load(filename, sr=None)
#     return audio_data, sampling_freq
#
#
# # Визуализация аудиосигнала
# def visualize_audio(audio_data, sampling_freq, title="Audio Waveform"):
#     # Создание временной оси
#     time_axis = np.linspace(0, len(audio_data) / sampling_freq, len(audio_data))
#
#     # Создание графика
#     plt.figure(figsize=(12, 4))
#     plt.plot(time_axis, audio_data)
#     plt.xlabel('Time (seconds)')
#     plt.ylabel('Amplitude')
#     plt.title(title)
#     plt.grid(True)
#     plt.tight_layout()
#     plt.show()
#
#
# # Анализ частотного спектра
# def analyze_spectrum(audio_data, sampling_freq):
#     # Вычисление FFT
#     fft_data = np.fft.fft(audio_data)
#     frequencies = np.fft.fftfreq(len(fft_data), 1 / sampling_freq)
#
#     # Только положительные частоты
#     positive_freqs = frequencies[:len(frequencies) // 2]
#     magnitude = np.abs(fft_data[:len(fft_data) // 2])
#
#     # Визуализация спектра
#     plt.figure(figsize=(12, 4))
#     plt.plot(positive_freqs, magnitude)
#     plt.xlabel('Frequency (Hz)')
#     plt.ylabel('Magnitude')
#     plt.title('Frequency Spectrum')
#     plt.grid(True)
#     plt.tight_layout()
#     plt.show()
#
#
# # Основная функция
# def main():
#     # Загрузка аудиофайла
#     audio_file = "kitten.mp3"
#     audio_data, sampling_freq = load_audio(audio_file)
#
#     print(f"Загружен файл: {audio_file}")
#     print(f"Частота дискретизации: {sampling_freq} Hz")
#     print(f"Длительность: {len(audio_data) / sampling_freq:.2f} секунд")
#     print(f"Количество сэмплов: {len(audio_data)}")
#
#     # Визуализация waveform
#     visualize_audio(audio_data, sampling_freq, "Kitten Audio Waveform")
#
#     # Анализ спектра
#     analyze_spectrum(audio_data, sampling_freq)
#
#     # Сохранение информации о файле в JSON
#     audio_info = {
#         "filename": audio_file,
#         "sampling_frequency": sampling_freq,
#         "duration_seconds": len(audio_data) / sampling_freq,
#         "num_samples": len(audio_data),
#         "min_amplitude": float(np.min(audio_data)),
#         "max_amplitude": float(np.max(audio_data)),
#         "mean_amplitude": float(np.mean(audio_data))
#     }
#
#     with open("kitten_audio_info.json", "w", encoding="utf-8") as f:
#         json.dump(audio_info, f, indent=2, ensure_ascii=False)
#
#     print("\nИнформация об аудио сохранена в kitten_audio_info.json")
#
## # # Модуль numpy
# # import numpy as np
# #
# # # функция активации: f(x) = 1 / (1 + e^(-x))
# # def sigmoid(x):
# #     return 1 / (1 + np.exp(-x))
# #
# # # Создание класса "Нейрон"
# # class Neuron:
# #     def __init__(self, w):
# #         self.w = w
# #
# #     def y(self, x):
# #         s = np.dot(self.w, x)  # Сумматор
# #         return sigmoid(s)       # функция активации
# #
# # Xi = np.array([2, 2, 2, 2])
# # xi = np.array([1, 1, 1, 1]) # Задание значений входам
# # Wi = np.array([5, 4, 3, 1])    # Веса входных сенсоров
# #
# # n = Neuron(Wi)                 # Создание объекта из класса
# # print('Y= ', n.y(Xi+xi))          # Вывод результата
# # from turtledemo.sorting_animate import instructions1
#
# # #Листинг 4.3--------------------------104 стр.
# #
# # # Искусственный нейрон (персептрон)
# # def perceptron(Sensor):
# #     b = 7  # Порог функции активации
# #     s = 0  # Начальное значение суммы
# #     for i in range(15):  # цикл суммирования сигналов от сенсоров
# #         # Преобразуем сигнал ('0' или '1') в число и умножаем на вес связи
# #         s += int(Sensor[i]) * weights[i]
# #
# #     if s >= b:
# #         return True  # Сумма превысила порог
# #     else:
# #         return False  # Сумма меньше порога
# #
# #
# # # Проверка работы искусственного нейрона (персептрона)
# # num1 = list('001001001001001')
# # num2 = list('111001111100111')
# # weights = [1 for _ in range(15)]  # Присвоение значений всем связям w=1
# #
# # print(f"Сигналы: {num1}")
# # print(f"Ответ персептрона: {perceptron(num1)}")
# # print(f"Сигналы: {num2}")
# # print(f"Ответ персептрона: {perceptron(num2)}")
#
# # import cv2
# # import numpy as np
# #
# # img = cv2.imread('image/1234.jpg')
# #
# # img = cv2.resize(img,(img.shape[1] // 2,img.shape[0] // 2))
# # img = cv2.GaussianBlur(img,(9,9),0)
# # img = cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)
# #
# # img = cv2.Canny(img,100,100)
# #
# #
# # kernel = np.ones((5,5), np.uint8)
# # img = cv2.dilate(img, kernel, iterations=1)
# # img = cv2.erode(img, kernel, iterations=1)
# #
# # cv2.imshow('Result', img)
# #
# # cv2.waitKey(0)
# #
# #
# #
#
# #
# # import cv2
# # import numpy as np
# #
# #
# # photo = np.zeros((450,450,3) , dtype = 'uint8')
# #
# # # RGB -  стандарт
# # # BGR - формат в OpenCV
# #
# #
# # # photo[:] = 171,77,255
# # # photo[100:150,280:280] = 171,77,255
# #
# # # cv2.rectangle(photo, (0,0),(100, 100),(171,77,255),thickness=3)
# # cv2.rectangle(photo, (0,0),(100, 100),(171,77,255),thickness=cv2.FILLED)
# #
# # cv2.line(photo,(0,photo.shape[0]//2),(photo.shape[1], photo.shape[0]//2),(171,77,255),thickness=3)
# #
# #
# # # cv2.circle(photo,(photo.shape[1]//2, photo.shape[0]//2), photo.shape[0]//2),(171,77,255),thickness=3)
# #
# # cv2.putText (photo, 'itProgger',(100,150), cv2.FONT_HERSHEY_TRIPLEX,1,(255,0,0),3)
# #
# # cv2.imshow('Photo',photo)
# # cv2.waitKey(0)
# #
#
#
# # import cv2
# # import numpy as np
# #
# # cap = cv2.VideoCapture("vid/pzr.mp4")
# #
# # while True:
# #     success, img = cap.read()
# #     if not success:
# #         break
# #
# #     # img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
# #
# #     # 1. Размытие по Гауссу (убирает шум)
# #     img = cv2.GaussianBlur(img, (9, 9), 0)
# #
# #     # 2. Перевод в оттенки серого
# #     img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# #
# #     # 3. Выделение границ (контуров) методом Кэнни
# #     img = cv2.Canny(img, 30, 30)
# #
# #     # 4. Создание ядра для морфологических операций
# #     kernel = np.ones((5, 5), np.uint8)
# #
# #     # 5. Расширение (утолщение линий)
# #     img = cv2.dilate(img, kernel, iterations=1)
# #
# #     # 6. Сжатие (эрозия — утончение линий)
# #     img = cv2.erode(img, kernel, iterations=1)
# #
# #     cv2.imshow('Result', img)
# #
# #     # Ожидание нажатия клавиши (в оригинале урока строка ниже)
# #     if cv2.waitKey(1) & 0xFF == ord('q'):
# #         break
# #
# # cap.release()
# # cv2.destroyAllWindows()
#
# # img =cv2.imread("image/1234.jpg")
# #
# #
# # # img = cv2.flip(img, -1)
# # def rotate(img_param,angle):
# #     height,width = img.shape[:2]
# #     point =  (width//2,height//2)
# #
# #     mat = cv2.getRotationMatrix2D(point,angle,1)
# #     return  cv2.warpAffine(img_param,mat,(width,height))
# #
# # img = rotate(img,90)
# #
# # cv2.imshow("res",img)
# #
# # cv2.waitKey(0)
#
#
# #
# # import cv2                  # код не работает - (исправить по возможности!)
# # image_path = "image\s.jpg"
# # face_cascade = cv2.CascadeClassifier('# не рбаотает код')
# # image = cv2.imread(image_path)
# # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# # faces = face_cascade.detectMultiScale(
# #     gray,
# #     scaleFactor= 1.1,
# #     minNeighbors= 5,
# #     minSize=(10, 10)
# # )
# # faces_detected = "Лиц обнаружено: " + format(len(faces))
# # print(faces_detected)
# # # Рисуем квадраты вокруг лиц
# # for (x, y, w, h) in faces:
# #     cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 0), 2)
# # viewImage(image,faces_detected)
# #
# #
#
# # import cv2
# # from ultralytics import YOLO
# # import numpy as np
# # import os
# #
# #
# # def create_test_video(filename):
# #     """Создает простое тестовое видео программно"""
# #     print("Создание тестового видео...")
# #     width, height = 640, 480
# #     fps = 30
# #     duration_sec = 5  # длительность 5 секунд
# #
# #     fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# #     out = cv2.VideoWriter(filename, fourcc, fps, (width, height))
# #
# #     for i in range(duration_sec * fps):
# #         img = np.zeros((height, width, 3), dtype=np.uint8)
# #
# #         # Рисуем "человека" (просто прямоугольник, чтобы модель его увидела как объект,
# #         # но лучше использовать реальное фото. Для теста нарисуем похожие фигуры)
# #         # Центр экрана
# #         cx, cy = width // 2, height // 2
# #
# #         # Двигаем объект
# #         offset = int(100 * np.sin(i / 10))
# #
# #         # Рисуем зеленый прямоугольник (имитация человека)
# #         cv2.rectangle(img, (cx - 50 + offset, cy - 100), (cx + 50 + offset, cy + 100), (0, 255, 0), -1)
# #
# #         # Рисуем красный круг (имитация предмета)
# #         cv2.circle(img, (cx + 150, cy), 30, (0, 0, 255), -1)
# #
# #         out.write(img)
# #
# #     out.release()
# #     print(f"Тестовое видео создано: {filename}")
# #
# #
# # def process_video(input_path, output_path):
# #     # 1. Загружаем модель сегментации
# #     print("Загрузка модели YOLOv8...")
# #     model = YOLO('yolov8n-seg.pt')
# #
# #     # 2. Открываем видеофайл
# #     cap = cv2.VideoCapture(input_path)
# #
# #     if not cap.isOpened():
# #         print(f"Ошибка: Не удалось открыть файл {input_path}")
# #         return
# #
# #     # Получаем параметры видео
# #     width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# #     height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# #     fps = cap.get(cv2.CAP_PROP_FPS)
# #
# #     if fps == 0:
# #         fps = 30
# #
# #     # 3. Настраиваем запись
# #     fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# #     out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
# #
# #     print(f"Обработка видео: {width}x{height}, FPS: {fps}")
# #     print("Идет обработка...")
# #
# #     frame_count = 0
# #
# #     try:
# #         while True:
# #             ret, frame = cap.read()
# #             if not ret:
# #                 break
# #
# #             frame_count += 1
# #             if frame_count % 10 == 0:
# #                 print(f"Обработан кадр: {frame_count}")
# #
# #             # 4. Распознавание объектов
# #             results = model(frame, stream=True, verbose=False, conf=0.25)  # conf пониже, чтобы ловило больше
# #
# #             for r in results:
# #                 img = r.orig_img
# #
# #                 if r.masks is not None:
# #                     masks = r.masks.data.cpu().numpy()
# #                     boxes = r.boxes
# #                     names = r.names
# #
# #                     for i, mask in enumerate(masks):
# #                         class_id = int(boxes.cls[i])
# #                         class_name = names[class_id]
# #                         confidence = float(boxes.conf[i])
# #
# #                         # Рисуем контур
# #                         mask_uint8 = (mask * 255).astype(np.uint8)
# #                         contours, _ = cv2.findContours(mask_uint8, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# #                         cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
# #
# #                         # Пишем текст
# #                         if len(contours) > 0:
# #                             x, y, w, h = cv2.boundingRect(contours[0])
# #                             label = f"{class_name} {confidence:.2f}"
# #
# #                             text_size = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)[0]
# #                             cv2.rectangle(img, (x, y - 20), (x + text_size[0], y), (0, 255, 0), -1)
# #                             cv2.putText(img, label, (x, y - 5),
# #                                         cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
# #
# #                 out.write(img)
# #
# #     except KeyboardInterrupt:
# #         print("\nОстановлено пользователем.")
# #
# #     finally:
# #         cap.release()
# #         out.release()
# #         cv2.destroyAllWindows()
# #         print(f"Готово! Результат сохранен в: {output_path}")
# #
# #
# # if __name__ == "__main__":
# #     input_video = "test_video.mp4"
# #     output_video = "result.mp4"
# #
# #     # Создаем тестовое видео, если его нет
# #     if not os.path.exists(input_video):
# #         create_test_video(input_video)
# #
# #     # Обрабатываем видео
# #     process_video(input_video, output_video)
#
#
#
# #
# # import numpy as np
# # import matplotlib.pyplot as plt
# #
# # #  сигнала
# # duration = 0.009  # 9 миллисекунд
# # sample_rate = 5000
# # t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
# #
# # #  звук
# # signal = (
# #     0.65 * np.sin(2 * np.pi * 440 * t) +
# #     0.35 * np.sin(2 * np.pi * 880 * t)
# # )
# #
# # # амплитуда до диапазона
# # signal /= np.max(np.abs(signal))
# #
# # plt.figure(figsize=(8, 5))
# # plt.plot(t * 1000, signal, color="gray", linewidth=1)
# # plt.title("Сгенерированный аудиосигнал")
# # plt.xlabel("Время (миллисекунды)")
# # plt.ylabel("Амплитуда")
# # plt.xlim(0, 5)
# # plt.ylim(-1, 1.5)
# # plt.grid(True, alpha=0.3)
# # plt.tight_layout()
# # plt.show()
#
#
#
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.io.wavfile import write
# from scipy.signal import resample_poly
# import soundfile as sf
#
# input_file = "kitten.mp3"
# output_file = "generated_audio.wav"
#
# #аудиофайл
# signal, sampling_freq = sf.read(input_file)
#
#
# if signal.ndim == 2:
#     signal = signal.mean(axis=1)
#
# # WAV сохраняем в формате int16
# signal_normalized = signal / np.max(np.abs(signal))
# signal_scaled = (signal_normalized * np.iinfo(np.int16).max).astype(np.int16)
# write(output_file, sampling_freq, signal_scaled)
#
#
# signal_to_plot = signal[:200]
# time_axis = 1000 * np.arange(len(signal_to_plot)) / sampling_freq
#
# plt.plot(time_axis, signal_to_plot, color="black")
# plt.xlabel("Время (миллисекунды)")
# plt.ylabel("Амплитуда")
# plt.title("Аудиосигнал kitten.mp3")
# plt.grid(True, alpha=0.3)
# plt.show()
#
# import json
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.io import wavfile
# import librosa
#
#
# # Загрузка аудиофайла kitten.mp3
# def load_audio(filename):
#     # Загрузка аудио с помощью librosa
#     audio_data, sampling_freq = librosa.load(filename, sr=None)
#     return audio_data, sampling_freq
#
#
# # Визуализация аудиосигнала
# def visualize_audio(audio_data, sampling_freq, title="Audio Waveform"):
#     # Создание временной оси
#     time_axis = np.linspace(0, len(audio_data) / sampling_freq, len(audio_data))
#
#     # Создание графика
#     plt.figure(figsize=(12, 4))
#     plt.plot(time_axis, audio_data)
#     plt.xlabel('Time (seconds)')
#     plt.ylabel('Amplitude')
#     plt.title(title)
#     plt.grid(True)
#     plt.tight_layout()
#     plt.show()
#
#
# # Анализ частотного спектра
# def analyze_spectrum(audio_data, sampling_freq):
#     # Вычисление FFT
#     fft_data = np.fft.fft(audio_data)
#     frequencies = np.fft.fftfreq(len(fft_data), 1 / sampling_freq)
#
#     # Только положительные частоты
#     positive_freqs = frequencies[:len(frequencies) // 2]
#     magnitude = np.abs(fft_data[:len(fft_data) // 2])
#
#     # Визуализация спектра
#     plt.figure(figsize=(12, 4))
#     plt.plot(positive_freqs, magnitude)
#     plt.xlabel('Frequency (Hz)')
#     plt.ylabel('Magnitude')
#     plt.title('Frequency Spectrum')
#     plt.grid(True)
#     plt.tight_layout()
#     plt.show()
#
#
# # Основная функция
# def main():
#     # Загрузка аудиофайла
#     audio_file = "kitten.mp3"
#     audio_data, sampling_freq = load_audio(audio_file)
#
#     print(f"Загружен файл: {audio_file}")
#     print(f"Частота дискретизации: {sampling_freq} Hz")
#     print(f"Длительность: {len(audio_data) / sampling_freq:.2f} секунд")
#     print(f"Количество сэмплов: {len(audio_data)}")
#
#     # Визуализация waveform
#     visualize_audio(audio_data, sampling_freq, "Kitten Audio Waveform")
#
#     # Анализ спектра
#     analyze_spectrum(audio_data, sampling_freq)
#
#     # Сохранение информации о файле в JSON
#     audio_info = {
#         "filename": audio_file,
#         "sampling_frequency": sampling_freq,
#         "duration_seconds": len(audio_data) / sampling_freq,
#         "num_samples": len(audio_data),
#         "min_amplitude": float(np.min(audio_data)),
#         "max_amplitude": float(np.max(audio_data)),
#         "mean_amplitude": float(np.mean(audio_data))
#     }
#
#     with open("kitten_audio_info.json", "w", encoding="utf-8") as f:
#         json.dump(audio_info, f, indent=2, ensure_ascii=False)
#
#     print("\nИнформация об аудио сохранена в kitten_audio_info.json")
#
#
# if __name__ == "__main__":
#     main()


# if __name__ == "__main__":
#     main()


import os
import cv2
import numpy as np

IMAGE_DIR = "image"

#  каскады
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
plate_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_russian_plate_number.xml")

car_cascade_path = cv2.data.haarcascades + "haarcascade_car.xml"
car_cascade = cv2.CascadeClassifier(car_cascade_path) if os.path.exists(car_cascade_path) else None


def read_image(path):
    # чиает картинку
    if not os.path.exists(path):
        return None
    data = np.fromfile(path, dtype=np.uint8)
    return cv2.imdecode(data, cv2.IMREAD_COLOR)


def show_image(name, image):
    # показывает картинку в окне
    if image is None:
        return
    h, w = image.shape[:2]

    scale = min(1200 / w, 800 / h, 1.0)
    if scale < 1.0:
        image = cv2.resize(image, (int(w * scale), int(h * scale)))
    cv2.imshow(name, image)


def find_faces(image):
     # лица
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return face_cascade.detectMultiScale(gray, 1.1, 6, minSize=(40, 40))


def find_cars(image):
    # машина
    if car_cascade is None:
        return []
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    return car_cascade.detectMultiScale(gray, 1.1, 4, minSize=(60, 60))


def find_plates(image, box=None):
    # номера
    if box:
        x, y, w, h = box
        roi = image[y:y + h, x:x + w]
        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        plates = plate_cascade.detectMultiScale(gray, 1.1, 4, minSize=(20, 20))

        return [(x + px, y + py, pw, ph) for px, py, pw, ph in plates]
    else:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return plate_cascade.detectMultiScale(gray, 1.1, 4, minSize=(30, 30))


def draw_boxes(image, faces, cars, plates):

    result = image.copy()
    for x, y, w, h in faces:
        cv2.rectangle(result, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(result, "FACE", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    for x, y, w, h in cars:
        cv2.rectangle(result, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(result, "CAR", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
    for x, y, w, h in plates:
        cv2.rectangle(result, (x, y), (x + w, y + h), (0, 255, 255), 3)
        cv2.putText(result, "CAR2", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
    return result


# ===== ГЛАВНАЯ ЧАСТЬ =====

print("Запуск системы распознавания")

# Люди
people = read_image(os.path.join(IMAGE_DIR, "people.jpg"))
if people is not None:
    faces = find_faces(people)
    print(f"Люди: найдено лиц - {len(faces)}")
    show_image("PEOPLE", draw_boxes(people, faces, [], []))
else:
    print("Люди: файл не найден")

# Машины и номера
car = read_image(os.path.join(IMAGE_DIR, "car.jpg"))
if car is not None:
    cars = find_cars(car)
    print(f"Машины: найдено - {len(cars)}")

    plates = []
    if cars:
        for box in cars:
            plates.extend(find_plates(car, box))
        print(f"Номера: найдено - {len(plates)}")
    else:
        plates = find_plates(car)
        print(f"Номера: найдено - {len(plates)}")

    show_image("CAR", draw_boxes(car, [], cars, plates))
else:
    print("Машины: файл не найден")

print("Распознавание завершено")
cv2.waitKey(0)
cv2.destroyAllWindows()