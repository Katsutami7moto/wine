# New Russian wine

Website of the original wine store "New Russian wine".

### How to install

Python3 should be already installed.
Download the [ZIP archive](https://github.com/Katsutami7moto/wine/archive/refs/heads/master.zip) of the script and unzip it.
Then open terminal form unzipped directory and use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```commandline
pip install -r requirements.txt
```
Before you run the website, you may need to configure environmental variables:

1. Go to the directory where `main.py` file is and create a file with the name `.env` (yes, it has only the extension).
It is the file to contain environmental variables that usually store data unique to each user, thus you will need to create your own.
2. Copy and paste this to `.env` file:
```dotenv
FILE_NAME='{file_name}'
SHEET_NAME='{sheet_name}'
```
3. Replace `{file_name}` with path to your Excel file where wines data is stored. If it's in the same category as `main.py` file, replace with just its name.
4. Replace `{sheet_name}` with the name of the sheet in chosen Excel file that you want to use. It can be written in any language.

### How to use

Excel file and sheet names specified in `.env` file may be replaced if you run `main.py` script with command line arguments.
Arguments are `-f filename.xlsx` for name of Excel file and `-s SheetName` for name of its sheet. Both arguments are optional.

Change only the file:
```commandline
python3 main.py -f filename.xlsx
```

Change only the sheet:
```commandline
python3 main.py -s SheetName
```

Change both:
```commandline
python3 main.py -f filename.xlsx -s SheetName
```

Change nothing:
```commandline
python3 main.py
```

If you don't have `.env` file and run the script without arguments, there still are default values for both variables inside the script:

```dotenv
FILE_NAME='wine.xlsx'
SHEET_NAME='Лист1'
```

### Input data example

Script uses an Excel `*.xlsx` file to store data which is used to form website's index page from template.
This repository has `wine.xlsx` file as an example. You may copy it and fill it with your data.
Or, if that file was lost, use this table as an example to create your Excel file (some cells in `Сорт` and `Цена` columns may be empty):

| Категория    | Имя           | Сорт            | Цена | Картинка          | Акция                |
|--------------|---------------|-----------------|------|-------------------|----------------------|
| Белые вина   | Белая леди    | Дамский пальчик | 399  | belaya_ledi.png   |                      |
| Красные вина | Чёрный лекарь |                 | 350  | chernyi_lekar.png | Выгодное предложение |

### Project Goals

The code is written for educational purposes on the online-course for web-developers, [dvmn.org](https://dvmn.org/).
