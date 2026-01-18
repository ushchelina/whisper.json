# Преобразование mp3-файлов в текст через Whisper

## Настройка под Windows.

Предварительно установить следующие программы.

- GNU [Unix Utils](http://unxutils.sourceforge.net/) для операций через makefile
- [Git for Windows](https://git-scm.com/download/win) для доступа к репозитарию исходных кодов.
- [Python3.10](https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe)

## Установка

```bash
git clone https://github.com/ushchelina/whisper.json.git
cd whisper.json
make setup PYTHON_BIN=/path/to/python3.10
make tests
```

## Использование

Положить в каталог `build` mp3-файл для транскрибирования под именем `xxx.mp3`. Затем:

```bash
make json
```

После завершения процесса транскрибирования в каталоге `build` будет создан файл `xxx.json` с транскрибированным из аудио-файла текстом.

## Ссылки

- [Проект faster-whisper](https://github.com/SYSTRAN/faster-whisper)
- [Адаптация языковой модели vosk](https://habr.com/ru/articles/735480/)
- [Сравнение Vosk и Whisper](https://habr.com/ru/articles/814057/)
