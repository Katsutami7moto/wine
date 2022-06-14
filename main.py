from collections import defaultdict
from datetime import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler

from configargparse import ArgParser
from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader, select_autoescape
from pandas import read_excel


def count_age(est_year: int) -> tuple:
    now_year = datetime.now().year
    age = now_year - est_year
    age_last_number = int(str(age)[2:])
    if age_last_number == 1:
        years = 'год'
    elif age_last_number in (2, 3, 4):
        years = 'года'
    else:
        years = 'лет'
    return age, years


def process_wines_excel(excel_file: str, excel_sheet: str) -> dict:
    wines_from_excel = read_excel(
        excel_file,
        sheet_name=excel_sheet,
        na_values=' ',
        keep_default_na=False
    ).to_dict(orient='records')
    wines_from_excel.sort(key=lambda w: (w['Категория'], w['Цена']))

    categorized_wines = defaultdict(list)
    for wine in wines_from_excel:
        categorized_wines[wine['Категория']].append(wine)
    return dict(categorized_wines)


def main():
    load_dotenv()
    parser = ArgParser()
    parser.add_argument(
        '-f', '--file',
        help='Path to Excel file with your data',
        env_var='FILE_NAME', default='wine.xlsx'
    )
    parser.add_argument(
        '-s', '--sheet',
        help='Name of Excel sheet to use in chosen file',
        env_var='SHEET_NAME', default='Лист1'
    )
    options = parser.parse_args()

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')

    age, years = count_age(est_year=1920)
    processed_wines = process_wines_excel(options.file, options.sheet)
    rendered_page = template.render(
        winery_age=age,
        years_word_form=years,
        wines=processed_wines,
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
