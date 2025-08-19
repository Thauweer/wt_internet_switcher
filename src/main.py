import keyboard
import subprocess
import time
import configparser
import os
from functools import partial


CONFIG = None


def load_config():
    global CONFIG
    config_file = 'config.ini'

    if not os.path.exists(config_file):
        raise FileNotFoundError(f"Конфигурационный файл '{config_file}' не найден.")

    CONFIG = configparser.ConfigParser()
    CONFIG.read(config_file, encoding='utf-8')
    print(f"Конфигурация успешно загружена из {config_file}")


def block_internet_for_process(aces_path:str):
    """Блокирует исходящий интернет для процесса через Windows Firewall."""
    try:
        subprocess.run(
            'netsh advfirewall firewall add rule '
            'name="Block aces.exe OUT" '
            'dir=out '
            f'program="{aces_path}" '
            'action=block && '
            'netsh advfirewall firewall add rule '
            'name="Block aces.exe IN" '
            'dir=in '
            f'program="{aces_path}" '
            'action=block',
            shell=True,
            check=True  # Проверяем успешность выполнения
        )
        print(f"🔴 Интернет для {aces_path} заблокирован!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Ошибка блокировки: {e}")


def unblock_internet_for_process(aces_path:str):
    """Разблокирует интернет для процесса, удаляя правило."""
    try:
        subprocess.run(
            'netsh advfirewall firewall delete rule '
            'name="Block aces.exe OUT" && '
            'netsh advfirewall firewall delete rule '
            'name="Block aces.exe IN"',
            shell=True,
            check=True
        )
        print(f"🟢 Интернет для {aces_path} разблокирован!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Ошибка разблокировки: {e}")


def main():
    global CONFIG

    # Проверяем, загружен ли конфиг, если нет — загружаем
    if CONFIG is None:
        try:
            load_config()
        except Exception as e:
            print(f"Не удалось загрузить конфиг: {e}")
            return
    
    # Парсим значение game_path
    try:
        if 'Paths' in CONFIG and 'game_path' in CONFIG['Paths']:
            game_path = CONFIG['Paths']['game_path']
            print(f"Путь к игре: {game_path}")

            # Проверка существования пути
            if os.path.exists(game_path):
                print("✅ Путь к игре существует.")
            else:
                print("⚠️  Путь к игре не существует на диске.")
        else:
            print("❌ В конфиге отсутствует секция 'Paths' или параметр 'game_path'.")
    except Exception as e:
        print(f"Ошибка при чтении конфига: {e}")
    
    
    aces_path = f"{game_path}\\win64\\aces.exe"
    if os.path.exists(aces_path):
        print("✅ Путь к aces.exe существует.")
    else:
        return print("⚠️  Путь к aces.exe не существует на диске.")
    
    
    print("🔥 Скрипт управления интернетом для aces.exe")
    print("🔹 F10 — заблокировать интернет")
    print("🔹 F11 — разблокировать интернет")
    print("🔹 Ctrl+C — выход")

    keyboard.add_hotkey("F10", partial(block_internet_for_process, aces_path))
    keyboard.add_hotkey("F11", partial(unblock_internet_for_process, aces_path))

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nСкрипт остановлен.")


if __name__ == "__main__":
    main()
