from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import requests
import random
import sqlalchemy
from datetime import datetime

def cria_db():
    conn = conexao()
    sql_log = """CREATE TABLE IF NOT EXISTS logs (
        data_hora TEXT,
        pagina TEXT
    );"""
    conn.execute(sql_log)

def conexao():
    cnx = sqlalchemy.create_engine(f'sqlite:///db.db')
    return cnx

def insert_db(pagina):
    conn = conexao()
    sql = f"insert into logs (data_hora, pagina) values('{datetime.now()}', '{pagina}')"
    conn.execute(sql)

def select_db():
    conn = conexao()
    sql = f"select * from logs"
    cursor = conn.execute(sql)
    return cursor
    
    

def home(request):
    insert_db('home')
    return Response('Desafio Web 1.0')

def quotes(request):

    html = "<ul>"

    req = requests.get("https://1c22eh3aj8.execute-api.us-east-1.amazonaws.com/challenge/quotes")
    items = req.json()
    for row in items["quotes"]:
        html += f"<li>{row}</li>"

    html += "</ul>"
    insert_db('/quotes')
    return Response(html)

def quote(request):
    quote_number = int(request.matchdict['quote_number'])

    req = requests.get("https://1c22eh3aj8.execute-api.us-east-1.amazonaws.com/challenge/quotes")
    items = req.json()
    html = items["quotes"][quote_number - 1]

    insert_db('/quotes/random')
    return Response(html)

def quotes_random(request):

    req = requests.get("https://1c22eh3aj8.execute-api.us-east-1.amazonaws.com/challenge/quotes")
    items = req.json()

    quote_number = random.randint(0,len(items["quotes"]) - 1)

    html = f"quote_number: {quote_number}<br>"
    html += items["quotes"][quote_number]

    insert_db(f'/quote/{quote_number}')
    return Response(html)



def logs(request):
    cursor = select_db()
    json = { "rows": []}
    for row in cursor:
        json["rows"].append({
            "data_hora": row[0],
            "pagina": row[1]
        })
    return json

cria_db()

#if __name__ == '__main__':
with Configurator() as config:
    config.add_route('home', '/')
    config.add_route('quotes', '/quotes')
    config.add_route('quote', '/quote/{quote_number}')
    config.add_route('random', '/quotes/random')
    config.add_route('logs', '/api/logs')
    config.add_view(home, route_name='home')
    config.add_view(quotes, route_name='quotes')
    config.add_view(quote, route_name='quote')
    config.add_view(quotes_random, route_name='random')
    config.add_view(logs, route_name='logs', renderer="json")
    app = config.make_wsgi_app()
server = make_server('0.0.0.0', 6543, app)
server.serve_forever()