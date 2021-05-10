import json

def write_order_to_json(data):
    with open('orders.json','r') as f:
        obj = json.load(f)
    obj['orders'].append(data)

    with open('orders1.json','w') as f:
        json.dump(obj, f, indent=4, ensure_ascii=False)




order = {
    'item':'phone',
    'quantity':2,
    'price':10000,
    'buyer':'id_buyer',
    'date': '22.01.2020'
         }

write_order_to_json(order)