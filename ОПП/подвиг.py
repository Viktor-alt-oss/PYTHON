class Figure:
    type_fig = 'ellipse'
    color = 'red'

dict_fig1 = {'start_pt': [10, 5],
             'end_pt': [100, 20],
             'color': 'blue'}

fig1 = Figure()
for keys, value in dict_fig1.items():
    setattr(fig1, keys, value)

delattr(fig1, 'color')

print(*fig1.__dict__.keys())