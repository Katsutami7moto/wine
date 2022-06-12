from collections import defaultdict
from datetime import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape
from pandas import read_excel

if __name__ == "__main__":
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    now_year = datetime.now().year
    est_year = 1920
    age = now_year - est_year

    age_last_number = int(str(age)[2:])
    if age_last_number == 1:
        years = 'год'
    elif age_last_number in (2, 3, 4):
        years = 'года'
    else:
        years = 'лет'

    wines_from_excel = read_excel(
        'wine.xlsx',
        sheet_name='Лист1',
        na_values=' ',
        keep_default_na=False
    ).to_dict(orient='records')
    wines_from_excel.sort(key=lambda w: (w['Категория'], w['Цена']))

    categorized_wines = defaultdict(list)
    for wine in wines_from_excel:
        categorized_wines[wine['Категория']].append(wine)
    processed_wines = dict(categorized_wines)

    rendered_page = template.render(
        winery_age=age,
        years_word_form=years,
        wines=processed_wines,
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()
