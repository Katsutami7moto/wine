from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape

import datetime

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

now_year = datetime.datetime.now().year
est_year = 1920
age = now_year - est_year

age_last_number = int(str(age)[2:])
if age_last_number == 1:
    years = 'год'
elif age_last_number in (2, 3, 4):
    years = 'года'
else:
    years = 'лет'

rendered_page = template.render(
    winery_age=age,
    years_word_form=years,
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)


server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
