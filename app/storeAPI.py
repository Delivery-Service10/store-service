from flask import Blueprint, request, jsonify
from models import db, Store
import uuid
import bcrypt

store_api = Blueprint('store_api', __name__)


@store_api.route("/store", methods=['POST'])
@store_api.route("/store/", methods=['POST'])
def create_store():

    data = request.get_json()
    store_username = Store.query.filter_by(username=data['username']).first()
    store_name = Store.query.filter_by(name=data['name']).first()
    if store_username is not None:
        return jsonify({'message': 'Store username already exists'})
    elif store_name is not None:
        return jsonify({'message': 'Store name already exists'})

    hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
    new_store = Store(public_id=str(uuid.uuid4()),
                      name=data['name'],
                      chain_id=data['chain-id'],
                      username=data['username'],
                      password=hashed_password,
                      addressLine1=data['addressLine1'],
                      addressLine2=data['addressLine2'],
                      city=data['city'],
                      district=data['district'],
                      country=data['country']
                      )
    db.session.add(new_store)
    db.session.commit()
    return jsonify({'message': 'New  Store created'})


@store_api.route('/store/id/<public_id>', methods=['GET'])
@store_api.route('/store/id/<public_id>/', methods=['GET'])
def get_one_store(public_id):
    store = Store.query.filter_by(public_id=public_id).first()
    if not store:
        return jsonify({'message': 'No store found'})
    else:
        store_data = allocate_data(store)
        return jsonify({'store': store_data})


@store_api.route('/store', methods=['GET'])
@store_api.route('/store/', methods=['GET'])
def get_all_stores():

    stores = Store.query.all()
    return combine_results(stores)


@store_api.route('/store/keyword/<keyword>', methods=['GET'])
@store_api.route('/store/keyword/<keyword>/', methods=['GET'])
def get_specified_stores(keyword):

    stores = Store.query.filter(Store.name.like("%" + keyword + "%"))
    return combine_results(stores)


@store_api.route('/store/<public_id>', methods=['DELETE'])
@store_api.route('/store/<public_id>/', methods=['DELETE'])
def delete_store(public_id):
    store = Store.query.filter_by(public_id=public_id).first()
    if not store:
        return jsonify({'message': 'Store not found'})
    else:
        db.session.delete(store)
        db.session.commit()
        return jsonify({'message': 'store deleted'})


def combine_results(stores):
    output = []
    for store in stores:
        store_data = allocate_data(store)
        output.append(store_data)

    return jsonify({'stores': output})


def allocate_data(store):
    store_data = {'public_id': store.public_id,
                  'username': store.username,
                  'name': store.name,
                  'addressLine1': store.addressLine1,
                  'addressLine2': store.addressLine2,
                  'city': store.city,
                  'district': store.district,
                  'country': store.country
                  }
    return store_data
