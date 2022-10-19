from app import app
from flask import render_template

@app.route('/')
def homePage():
    category = [{'category': 'BRAZILIAN FOODS', 'picture': 'https://www.meusdicionarios.com.br/wp-content/uploads/2016/04/sh_bandeira-do-brasil_1056515003.jpg'}]
    return render_template('index.html', category=category)

@app.route('/foods')
def favoriteFoods():
    
    foods = [{'name': 'Churrasco', 'picture': 'https://cptstatic.s3.amazonaws.com/imagens/enviadas/materias/materia28136/churrasco-e-acompanhamentos-afe.jpg'},
    {'name': 'Brigadeiro', 'picture': 'https://1.bp.blogspot.com/-2rVkjI7DrJE/XjojdxXydZI/AAAAAAAAYuc/fdBYccRFVugWVdorEy9wj3zkVb-hGCDkwCNcBGAsYHQ/s1600/BRIGADEIRO-RECEITA.jpg'},
    {'name': 'Coxinha','picture': 'https://img.cybercook.com.br/receitas/610/coxinha-3-840x480.jpeg?q=75'},
    {'name': 'Pastel', 'picture': 'https://guiadopastel.com.br/wp-content/uploads/2020/04/4-receitas-de-massa-de-pastel-dourado-1200x900.jpg'},
    {'name': 'Pão de Queijo', 'picture': 'https://amopaocaseiro.com.br/wp-content/uploads/2022/08/yt-069_pao-de-queijo_receita-840x560.jpg'}]
    
    return render_template('foods.html', foods=foods)