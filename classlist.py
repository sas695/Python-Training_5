import sys
import json
import csv
from basicdb import *

load_db('registrar.json')

n = sys.argv[1]


T_1 = join(db_from('rooms'), db_from('courses'), 'roomid')
r = where(T_1,'courseid', n)
r = r[0]
capacity = int(r['capacity'])
print(r['coursename']+ ' meets ' + r['times'] + ' in ' + r['roomname'])


T_2 = join(db_from('enrollments'), db_from('students'), 'studentid')
r1 = where(T_2,'courseid', n)
for l in r1:
    print(l['firstname'] +' '+ l['lastname'])


enroll = count(r1)
print('Current enrollment: ' + str(enroll))
remain = capacity - enroll
print('Remaining capacity: ' + str(remain))

        

    