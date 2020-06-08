
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
