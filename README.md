# War Thunder Internet Switcher

Простой помощник для блокировки интернета в War Thunder.

## 📥 Установка

### Вариант 1: Готовый executable (рекомендуется)

1. Перейди в [Releases](https://github.com/your-username/wt_internet_switcher/releases).
2. Скачай последний `wt_internet_switcher.exe`.
3. Запусти **`wt_internet_switcher.exe` от имени администратора**.
4. При первом запуске автоматически создастся `config.ini` — отредактируй его, указав путь к игре.

### Вариант 2: Запуск из исходного кода

1. Запусти **`setup.cmd`** — создаст виртуальное окружение и установит зависимости (необходим Python с path - https://www.python.org/getit/windows/ 3.11+).
2. Отредактируй **`config.ini`**:
   - Укажи путь к папке с игрой War Thunder.
   - Пример:
     ```ini
     [Paths]
     game_path = C:\Program Files (x86)\War Thunder
     ```

3. Запусти **`run.cmd` от имени администратора**.

## ⌨️ Управление

- **F10** — заблокировать интернет для War Thunder  
- **F11** — разблокировать интернет  
- **Ctrl + C** — выход из программы

## ⚠️ Важно

- Для фаерволла windows требуется **запуск от имени администратора**.
- Если ошибка — проверь путь в `config.ini`.
