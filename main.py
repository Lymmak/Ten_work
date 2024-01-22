import threading
import time


def Command(x, event_for_set):
    for i in range(10):
        print(f"Командир обнаружил цель и дает команду уничтожить квадрат {i}")
        print("Команда дана")
        time.sleep(0.1)



def Gun(x, event_for_wait, event_for_set):
    for i in range(10):
        event_for_wait.wait()  # блокирует выполнение до тех пор, пока внутренний флаг не станет истинным True.
        event_for_wait.clear()  # сбрасывает внутренний флаг на значение False.
        time.sleep(0.0301)
        print(f"Пушка №{x} нанесла удар по квадрату: {i}")
        event_for_set.set()  # устанавливает для внутреннего флага значение True


# Инициализируем ивенты
e1 = threading.Event()
e2 = threading.Event()
e3 = threading.Event()
e4 = threading.Event()
# Инициализируем потоки
Com = threading.Thread(target=Command, args=(0, e2))
Gun1 = threading.Thread(target=Gun, args=(0, e1, e2))
Gun2 = threading.Thread(target=Gun, args=(1, e2, e3))
Gun3 = threading.Thread(target=Gun, args=(2, e3, e1))

# Запуск
Com.start()
Gun1.start()
Gun2.start()
Gun3.start()


# устанавливает для внутреннего флага значение True. Пробуждаются все потоки, ожидающие его выполнения. Потоки,
# которые вызывают метод Event.wait() после установки флага, не будут блокироваться вообще.
e1.set()  # Активируем первый ивент

# Ожидание, когда все пушки и командир закончат работу
Com.join()
Gun1.join()
Gun2.join()
Gun3.join()

print("Квадрат успешно отработан")
