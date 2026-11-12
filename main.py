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

import cv2
import os
import numpy as np

# Директория с изображениями
IMAGE_DIR = 'image'
# Максимальный размер окна для отображения изображений
MAX_WINDOW_SIZE = (1200, 800)

# Загрузка каскада Хаара для детекции лиц
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

# Загрузка каскада Хаара для детекции автомобилей (используем его для поиска рамки машины)
# Убедитесь, что файл 'haarcascade_car.xml' находится в правильной директории или укажите полный путь
# Если у вас нет этого файла, его можно скачать или использовать другой метод детекции объектов.
# Для примера, я предполагаю, что у вас есть такой файл.
# Если нет, эту часть можно будет заменить или удалить.
car_cascade_path = cv2.data.haarcascades + 'haarcascade_car.xml'
if os.path.exists(car_cascade_path):
    car_cascade = cv2.CascadeClassifier(car_cascade_path)
else:
    print(f"Предупреждение: Файл {car_cascade_path} не найден. Детекция автомобилей будет пропущена.")
    car_cascade = None


def safe_read_image(path):
    """
    Безопасно читает изображение из файла.
    Возвращает None, если файл не существует или не может быть прочитан.
    """
    if not os.path.exists(path):
        print(f"Ошибка: Файл не найден по пути: {path}")
        return None

    img = cv2.imread(path)

    if img is None:
        print(f"Предупреждение: Не удалось прочитать изображение стандартным способом: {path}. Попытка через imdecode.")
        try:
            with open(path, 'rb') as f:
                file_bytes = np.frombuffer(f.read(), np.uint8)
                img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        except Exception as e:
            print(f"Ошибка при чтении файла {path} через imdecode: {e}")
            return None
    return img


def resize_to_fit(img, max_size=MAX_WINDOW_SIZE):
    """
    Изменяет размер изображения, чтобы оно соответствовало максимальным размерам,
    сохраняя при этом соотношение сторон.
    """
    h, w = img.shape[:2]
    max_w, max_h = max_size

    if w <= max_w and h <= max_h:
        return img

    scale = min(max_w / w, max_h / h)
    new_w = int(w * scale)
    new_h = int(h * scale)

    return cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_AREA)


def detect_faces(img):
    """
    Обнаруживает лица на изображении.
    """
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=7, minSize=(50, 50)
    )
    faces = [f for f in faces if f[2] > 40 and f[3] > 40]
    return faces


def detect_cars_in_roi(img, roi):
    """
    Обнаруживает автомобили внутри указанной области (ROI).
    Использует каскад Хаара для автомобилей.
    """
    if car_cascade is None:
        return []

    x, y, w, h = roi
    # Извлекаем область интереса
    car_roi_img = img[y:y+h, x:x+w]
    gray_roi = cv2.cvtColor(car_roi_img, cv2.COLOR_BGR2GRAY)

    # Детектируем автомобили внутри этой области
    cars = car_cascade.detectMultiScale(
        gray_roi,
        scaleFactor=1.05, # Может потребоваться подстройка
        minNeighbors=5,
        minSize=(30, 30) # Минимальный размер автомобиля
    )

    # Корректируем координаты обнаруженных автомобилей, чтобы они соответствовали оригинальному изображению
    adjusted_cars = []
    for (cx, cy, cw, ch) in cars:
        # Убедимся, что автомобиль не слишком маленький и не выходит за пределы ROI
        if cw > 50 and ch > 50: # Дополнительная фильтрация
            adjusted_cars.append((x + cx, y + cy, cw, ch))
    return adjusted_cars


def detect_license_plate(img, car_roi):
    """
    Находит номерной знак внутри заданной области (ROI автомобиля).
    """
    x, y, w, h = car_roi
    # Извлекаем область автомобиля
    car_img_part = img[y:y+h, x:x+w]

    gray = cv2.cvtColor(car_img_part, cv2.COLOR_BGR2GRAY)
    h_roi, w_roi = gray.shape

    # Шаг 1: Поиск белых областей
    _, white_mask = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

    # Шаг 2: Морфологические операции
    kernel = np.ones((5, 5), np.uint8)
    white_mask = cv2.morphologyEx(white_mask, cv2.MORPH_OPEN, kernel, iterations=2)
    white_mask = cv2.morphologyEx(white_mask, cv2.MORPH_CLOSE, kernel, iterations=2)

    # Шаг 3: Поиск контуров
    contours, _ = cv2.findContours(white_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    best_plate = None
    best_score = 0

    for cnt in contours:
        x_cnt, y_cnt, w_cnt, h_cnt = cv2.boundingRect(cnt)

        if w_cnt < 60 or h_cnt < 20: # Уменьшил минимальный размер для поиска внутри ROI
            continue

        ratio = w_cnt / h_cnt
        if ratio < 3.0 or ratio > 6.0:
            continue

        area = w_cnt * h_cnt
        if area < 1500 or area > 15000: # Уменьшил диапазон площади
            continue

        roi_plate = gray[y_cnt:y_cnt + h_cnt, x_cnt:x_cnt + w_cnt]
        dark_pixels = np.sum(roi_plate < 100)
        total_pixels = roi_plate.size
        dark_ratio = dark_pixels / total_pixels

        if 0.10 <= dark_ratio <= 0.40:
            score = area * dark_ratio
            if 4.0 <= ratio <= 5.0:
                score *= 1.5

            if score > best_score:
                best_score = score
                # Сохраняем координаты относительно ROI автомобиля
                best_plate = (x_cnt, y_cnt, w_cnt, h_cnt)

    if best_plate:
        # Возвращаем координаты относительно оригинального изображения
        plate_x, plate_y, plate_w, plate_h = best_plate
        return [(x + plate_x, y + plate_y, plate_w, plate_h)]
    return []


def draw_detections(img, faces, cars, plates):
    """
    Рисует прямоугольники вокруг обнаруженных объектов.
    """
    result = img.copy()

    # Рисуем лица
    for (x, y, w, h) in faces:
        cv2.rectangle(result, (x, y), (x + w, y + h), (0, 255, 0), 3)
        cv2.putText(result, 'FACE', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    # Рисуем рамки автомобилей
    for (x, y, w, h) in cars:
        cv2.rectangle(result, (x, y), (x + w, y + h), (255, 0, 0), 3)
        cv2.putText(result, 'CAR', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

    # Рисуем номерные знаки
    for (x, y, w, h) in plates:
        cv2.rectangle(result, (x, y), (x + w, y + h), (0, 255, 255), 4)
        cv2.putText(result, f'PLATE', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

    return result


def show_image(window_name, img):
    """
    Отображает изображение в окне, масштабируя его при необходимости.
    """
    img_resized = resize_to_fit(img)
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    h, w = img_resized.shape[:2]
    cv2.resizeWindow(window_name, w, h)
    cv2.imshow(window_name, img_resized)


# ===== ОБРАБОТКА =====
print("Начинаю обработку...\n")

# Обработка изображения с людьми (для демонстрации детекции лиц)
people_path = os.path.join(IMAGE_DIR, 'people.jpg')
people_img = safe_read_image(people_path)

if people_img is not None:
    faces = detect_faces(people_img)
    # Для людей не ищем машины и номера, только лица
    result_people = draw_detections(people_img, faces, [], [])
    show_image('PEOPLE', result_people)
    print(f"Найдено лиц: {len(faces)}")

# Обработка изображения с автомобилем
car_path = os.path.join(IMAGE_DIR, 'car.jpg')
car_img = safe_read_image(car_path)

if car_img is not None:
    # Сначала детектируем автомобили на всем изображении
    cars = []
    if car_cascade is not None:
        cars = car_cascade.detectMultiScale(
            cv2.cvtColor(car_img, cv2.COLOR_BGR2GRAY),
            scaleFactor=1.05,
            minNeighbors=5,
            minSize=(50, 50) # Увеличен минимальный размер для общей детекции
        )
        cars = [(x, y, w, h) for (x, y, w, h) in cars if w > 100 and h > 100] # Фильтруем слишком мелкие обнаружения

    all_plates = []
    # Для каждого найденного автомобиля ищем номерной знак внутри его рамки
    for car_roi in cars:
        plates = detect_license_plate(car_img, car_roi)
        all_plates.extend(plates)

    print(f"Найдено автомобилей (для поиска номеров): {len(cars)}")
    print(f"Найдено номерных знаков: {len(all_plates)}")

    # Рисуем обнаружения: лица (если были), автомобили и номерные знаки
    # Для изображения с машиной, лица не ищем, поэтому передаем пустой список
    result_car = draw_detections(car_img, [], cars, all_plates)
    show_image('CAR', result_car)

print("\nОбработка завершена. Закройте окна для выхода.")
cv2.waitKey(0)
cv2.destroyAllWindows()
