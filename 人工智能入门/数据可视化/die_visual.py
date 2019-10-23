from 数据可视化.die import Die
import pygal

die = Die()

result = []
frequenices = []
for i in range(100):
    re = die.roll()
    result.append(re)

for value in range(1,die.num_size+1):
    frequency = result.count(value)
    frequenices.append(frequency)

print(frequenices)
#对结果进行可视化
hist = pygal.Bar()

hist.title='97'
hist.x_labels = [1, 2, 3, 4, 5, 6]
hist.x_title = "result"
hist.y_title = "frequency"

hist.add('D6', frequenices)
hist.render_to_file('die_visual.svg')