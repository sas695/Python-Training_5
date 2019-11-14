import json

from basicdb import *

def state_of(zipcode):
    load_db('geo.json')
    State_ID = select(where(db_from('geozipcodes'),'Zip Code',zipcode),'State_ID')
    return State_ID 



def zipcodes_in_city(city_name):
    load_db('geo.json')
    c = count(where(db_from('geozipcodes'),'City', city_name))
    return c



def northernmost(state): 
    load_db('geo.json')
    l = orderby(where(db_from('geozipcodes'),'State_ID', state),'Longitude')
    max = l[0]['Longitude']
    return max



def states_by_size():
    load_db('geo.json')
    create_table('stateZipCount', 'St' 'ZipCount')
    st_names =[]
    States = distinct(select(db_from('geozipcodes'),'State'))
    for state in States:
        c = count(where(db_from('geozipcodes'),'State',state))
        insert('stateZipCount', {'St': state , 'ZipCount':c})
    ordered_list = orderby(db_from('stateZipCount'), 'ZipCount')
    for l in ordered_list:
        st_names.append(l['St'])
    return st_names
