# Преобразование mp3-файлов в текст через Whisper

[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/ushchelina/whisper.json/pep257.yml?label=Pep257&style=plastic&branch=main)](https://github.com/ushchelina/whisper.json/actions?query=workflow%3Apep257)
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/ushchelina/whisper.json/py3.yml?label=Python%203.10&style=plastic&branch=main)](https://github.com/ushchelina/whisper.json/actions?query=workflow%3Apy3)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/0fa4672064ca46e1926197f16a8fe523)](https://app.codacy.com/gh/ushchelina/whisper.json/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/0fa4672064ca46e1926197f16a8fe523)](https://app.codacy.com/gh/ushchelina/whisper.json/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_coverage)

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
make xxx
```

После завершения процесса транскрибирования в каталоге `build` будет создан файл `xxx.json` с транскрибированным из аудио-файла текстом.

## Ссылки

- [Проект faster-whisper](https://github.com/SYSTRAN/faster-whisper)
- [Адаптация языковой модели vosk](https://habr.com/ru/articles/735480/)
- [Сравнение Vosk и Whisper](https://habr.com/ru/articles/814057/)
