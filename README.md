[![Actions Status](https://github.com/JoeCapHuang/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/JoeCapHuang/python-project-49/actions)
<a href="https://codeclimate.com/github/JoeCapHuang/python-project-49/maintainability"><img src="https://api.codeclimate.com/v1/badges/a0c6b2cb0ea0b5d1fecd/maintainability" /></a>

### Описание проекта

"Brain Games" - это набор увлекательных математических мини-игр, созданный для развития навыков в математике и логике. Проект разработан в рамках обучения на платформе Hexlet.

### Минимальные требования

- [Python 3.10](https://www.python.org/)
- [Prompt](https://pypi.org/project/prompt/)
- [flake8](https://flake8.pycqa.org/en/latest/)

### Установка Python

#### Ubuntu

1. Откройте терминал.

2. Установите Python 3.10 с помощью пакетного менеджера:

    ```bash
    sudo apt update
    sudo apt install python3.10
    ```

#### macOS

1. Откройте терминал.

2. Установите Homebrew, если у вас его еще нет. Последуйте инструкциям на [официальном сайте Homebrew](https://brew.sh/).

3. Установите Python 3.10 с помощью Homebrew:

    ```bash
    brew install python@3.10
    ```

4. Добавьте Python в ваш `PATH`:

    ```bash
    echo 'export PATH="/usr/local/opt/python@3.10/bin:$PATH"' >> ~/.zshrc
    source ~/.zshrc
    ```

#### Windows с использованием WSL

1. Установите WSL, следуя [официальной документации Microsoft](https://docs.microsoft.com/en-us/windows/wsl/install).

2. Запустите терминал WSL.

3. Установите Python 3.10 с помощью пакетного менеджера Ubuntu:

    ```bash
    sudo apt update
    sudo apt install python3.10
    ```

4. Добавьте Python в ваш `PATH`. Откройте ваш файл `~/.bashrc`:

    ```bash
    echo 'export PATH="/usr/bin/python3.10:$PATH"' >> ~/.bashrc
    source ~/.bashrc
    ```

### Установка зависимостей

    
    make install
    

### Клонирование репозитория:

    git clone https://github.com/JoeCapHuang/hexlet-code.git
    cd hexlet-code

### Запуск игр (до установки пакета)

Перед установкой пакета вы можете запустить игры напрямую из исходного кода. Используйте следующие команды для запуска каждой из игр:

1. "Проверка на чётность"

    ```bash
    make brain-even
    ```

2. "Калькулятор"

    ```bash
    make brain-calc
    ```

3. "Наибольший общий делитель (НОД)"

    ```bash
    make brain-gcd
    ```

4. "Арифметическая прогрессия"

    ```bash
    make brain-progression
    ```

5. "Простое ли число?"

    ```bash
    make brain-prime
    ```

### Запуск игр (после установки пакета)

- Установка пакета:

    ```bash
    make package-install
    ```

1. "Проверка на чётность"

    ```bash
    brain-even
    ```

2. "Калькулятор"

    ```bash
    brain-calc
    ```

3. "Наибольший общий делитель (НОД)"

    ```bash
    brain-gcd
    ```

4. "Арифметическая прогрессия"

    ```bash
    brain-progression
    ```

5. "Простое ли число?"

    ```bash
    brain-prime
    ```

## Дополнительные команды из Makefile:

- Сборка проекта:

    ```bash
    make build
    ```

- Публикация проекта (dry-run):

    ```bash
    make publish
    ```

- Переустановка пакета:

    ```bash
    make package-reinstall
    ```

- Проверка стиля кода:

    ```bash
    make lint
    ```

### Примеры работы игр:

[![asciicast](https://asciinema.org/a/3qi0RxCTbpsxR2TREET320IPl.svg)](https://asciinema.org/a/3qi0RxCTbpsxR2TREET320IPl)
[![asciicast](https://asciinema.org/a/h3HUj3Q1fthkD9p6YXW8wXSWn.svg)](https://asciinema.org/a/h3HUj3Q1fthkD9p6YXW8wXSWn)
[![asciicast](https://asciinema.org/a/3fJ5G6upBC8fFiVmUqMSXfrCu.svg)](https://asciinema.org/a/3fJ5G6upBC8fFiVmUqMSXfrCu)
[![asciicast](https://asciinema.org/a/45l15DR9ppkkusXVyAptkeCxy.svg)](https://asciinema.org/a/45l15DR9ppkkusXVyAptkeCxy)
[![asciicast](https://asciinema.org/a/QZ4iDMcuSOiF9LJTBYJp4FBa5.svg)](https://asciinema.org/a/QZ4iDMcuSOiF9LJTBYJp4FBa5)
