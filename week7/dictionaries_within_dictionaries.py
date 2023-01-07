# variable with a dictionary inside another dictionary
employee_data = {
    'name': 'Cody Developer',
    'employee_number': 123456,
    'location': {
        'city': 'Minneapolis',
        'office': 'M.123',
        'telephone': '612-123-4567'
    },
    'roles': ['python developer', 'system administrator']
}
# calls on the variable - locates the key - locates another key in the dictionary - modifies the value
employee_data['location']['office'] = 'M.400'
print(employee_data['location']['office'])
# same process when calling for another value inside a dictionary
print(employee_data['location']['telephone'])
# adding new value to key -- variable[key].add[value]
employee_data['roles'].append('web developer')
print(employee_data)
