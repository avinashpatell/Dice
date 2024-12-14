from die import Die
import pygal

#create a D6 die.
die=Die()

results=[]

#Make some rolls and store it in results list
for i in range (1000):
	result=die.Roll()
	results.append(result)

#Store the frequency of value from rolls
frequencies=[]

for value in range(1,die.faces+1):
	frequency=results.count(value)
	frequencies.append(frequency)

hist=pygal.Bar()

hist.title="Results of rolling D6 dice 1000 times."

hist.x_labels=['1','2','3','4','5','6']
hist.x_title="Result"
hist.y_title="Frequency of Result"

hist.add("D6",frequencies)

hist.render_to_file("die_visual.svg")
