import re
from flask import Blueprint, render_template, request, redirect, url_for
from .models import *
from . import db

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return redirect(url_for('views.outfits'))


@views.route('/outfits')
def outfits():
    outfits = Outfit.query.all()
    return render_template('outfits.html', outfits=outfits)


@views.route('/clothes')
def clothes():
    clothes = Cloth.query.all()
    return render_template('clothes.html', clothes=clothes)


@views.route('/add-outfits', methods=['GET', 'POST'])
def add_outfits():
    if request.method == 'POST':
        name = request.form.get('name')
        descr = request.form.get('descr')
        rating = request.form.get('rating')

        new_outfit = Outfit(name=name, descr=descr, rating=rating)
        db.session.add(new_outfit)
        db.session.commit()
        return redirect(url_for('views.home'))

    return render_template('add-outfits.html')


@views.route('/add-clothes', methods=['GET', 'POST'])
def add_clothes():
    if request.method == 'POST':
        name = request.form.get('item-name')
        size = request.form.get('item-size')
        color = request.form.get('item-color')

        new_cloth = Cloth(item=name, size=size, color=color)
        db.session.add(new_cloth)
        db.session.commit()
        return redirect(url_for('views.home'))

    return render_template('add-clothes.html')


@views.route('/delete-outfit/<id>')
def delete_outfit(id):
    outfit = Outfit.query.filter_by(id=id).first()
    db.session.delete(outfit)
    db.session.commit()
    return redirect(url_for('views.outfits'))


@views.route('/delete-cloth/<id>')
def delete_cloth(id):
    outfit = Cloth.query.filter_by(id=id).first()
    db.session.delete(outfit)
    db.session.commit()
    return redirect(url_for('views.clothes'))


@views.route('/update-cloth/<id>', methods=['GET', 'POST'])
def update_cloth(id):
    if request.method == 'POST':

        new = {
            "item": request.form.get('item'),
            "size": request.form.get('size'),
            "color": request.form.get('color')
        }

        Cloth.query.filter_by(id=id).update(new)
        db.session.commit()

        return redirect(url_for('views.home'))

    outfit = Cloth.query.filter_by(id=id).first()
    return render_template('update-cloth.html', outfit=outfit)


@views.route('/update-outfit/<id>', methods=['GET', 'POST'])
def update_outfit(id):
    if request.method == 'POST':

        new = {
            "name": request.form.get('name'),
            "descr": request.form.get('descr'),
            "rating": request.form.get('rating')
        }

        Outfit.query.filter_by(id=id).update(new)
        db.session.commit()

        return redirect(url_for('views.home'))

    outfit = Outfit.query.filter_by(id=id).first()

    clothlinks = list(Outfit_Cloth.query.filter_by(outfitId=id).all())

    return render_template('update-outfit.html', outfit=outfit, clothlinks=clothlinks)

@views.route('/cloth-outfit-link/<id>', methods=['GET','POST'])
def link(id):
    if request.method == 'POST':

        new = Outfit_Cloth(outfitId=id, clothId= request.form.get('clothid'))
        db.session.add(new)
        db.session.commit()

        return redirect(url_for('views.home'))
    return render_template('link.html')

@views.route('/remove/<oid>/<cid>')
def remove(oid, cid):
    link = Outfit_Cloth.query.filter_by(outfitId=oid, clothId=cid).first()
    db.session.delete(link)
    db.session.commit()
    return redirect(url_for('views.home'))