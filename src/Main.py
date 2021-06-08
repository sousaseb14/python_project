import sys
import json
print(sys.executable)
print(sys.version)

with open('/Users/seb/Desktop/python_project/src/iphone_sensors.json',) as f:
    idata = json.load(f)


people_string = '''
{
    "employee": [
    {
        "name":       "Dude1",
        "salary":      56000,
        "married":    true
    },
    {
        "name":       "Dude2",
        "salary":      43000,
        "married":    false
    }
    ]
}
'''

data = json.loads(people_string)
print(type(idata))
print(type(idata['Accelerometer']))
print(type(idata['Gyroscope']))
print(type(idata['GPS']))
print(type(idata['Magnetic Field']))
print(type(idata['Pressure']))

for time in idata['Magnetic Field']:
    print(time['Time (s)'],time['Absolute field (µT)'])
