from models import Store
import uuid


def combine_results(stores):
    output = []
    for store in stores:
        store_data = allocate_data(store)
        output.append(store_data)

    return output


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


def populate_store(data, hashed_password):
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
    return new_store
