from die import Die
import pygal

#create a D6 die.
die_1=Die()
die_2=Die()

results=[]

#Make some rolls and store it in results list
for i in range (1000):
	result=die_1.Roll()+die_2.Roll()
	results.append(result)

#Store the frequency of value from rolls
frequencies=[]
max_result=die_1.faces+die_2.faces

for value in range(1,max_result+1):
	frequency=results.count(value)
	frequencies.append(frequency)

hist=pygal.Bar()

hist.title="Results of rolling two D6 dice 1000 times."

hist.x_labels=['1','2','3','4','5','6','7','8','9','10','11','12']
hist.x_title="Result"
hist.y_title="Frequency of Result"

hist.add("D6+D6",frequencies)

hist.render_to_file("die_visual2.svg")
