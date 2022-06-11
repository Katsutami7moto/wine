from collections import defaultdict
from datetime import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape
from pandas import read_excel

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

wines_excel = read_excel('wine.xlsx', sheet_name='Лист1', na_values=' ', keep_default_na=False)
wines_dict = wines_excel.to_dict(orient='records')
for wine in wines_dict:
    wine['Цена'] = int(wine['Цена'])

dd_wines = defaultdict(list)
for wine in wines_dict:
    dd_wines[wine['Категория']].append(dict(sorted(wine.items())))
wines = dict(sorted(dict(dd_wines).items()))

rendered_page = template.render(
    winery_age=age,
    years_word_form=years,
    wines=wines,
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
