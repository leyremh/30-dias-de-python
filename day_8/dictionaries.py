dog= {}

dog= {'name':'Drago', 'color':'blanco', 'breed':'chhiguagua', 'legs':'4', 'age':'3años'}
student={'name':'leyre','last_name': 'montero','gender':'femenino','age':'16','marital status':'con novio', 'skill':'bailar', 'country':'españa','city':'jerez'}
print(len(student))
print(type(student['skill']))
student['skill'].append("memorizar")
values = student.values()
item = list(student.items())
student.pop('age')
del student
