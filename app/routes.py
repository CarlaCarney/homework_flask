from app import app
from flask import render_template, request, redirect, url_for
from app.forms import searchPokemon
from app.getPokemon import *

@app.route('/')
def homePage():
    return render_template('index.html')

@app.route('/search', methods=["GET","POST"])
def pokemon():
    form = searchPokemon()
    pokemon = {}
    error = ""
    try:
        if form.validate():
            pokemon = getPokemon(form.name.data)
            form.name.data = ""
    except Exception as e:
        error = str(e)
    finally:
        return render_template('search.html', title = 'Pokedex', form=form, pokemon=pokemon, error=error)