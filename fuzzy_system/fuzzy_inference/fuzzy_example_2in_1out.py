from fuzzy_system.fuzzy_variable_output import FuzzyOutputVariable
from fuzzy_system.fuzzy_variable_input import FuzzyInputVariable
#from fuzzy_system.fuzzy_variable import FuzzyVariable
from fuzzy_system.fuzzy_system import FuzzySystem

colour = FuzzyInputVariable('Colour', 0,1,13)
colour.add_triangular('Excellent', 0, 0.15, 0.25)
colour.add_trapezoidal('Average', 0.15, 0.25, 0.5,0.65)
colour.add_trapezoidal('Bad', 0.5, 0.65, 0.75,0.9)
colour.add_triangular('ExtraBad', 0.75,0.9,1)

tree = FuzzyInputVariable('Tree', 0,1,13)
tree.add_triangular('Excellent', 0, 0.15, 0.25)
tree.add_trapezoidal('Average', 0.15, 0.25, 0.5,0.65)
tree.add_trapezoidal('Bad', 0.5, 0.65, 0.75,0.9)
tree.add_triangular('ExtraBad', 0.75,0.9,1)  


gini = FuzzyInputVariable('Gini', 0, 1,13)
gini.add_triangular('LBad', 0, 0.3, 0.42)
gini.add_trapezoidal('Good',0.3,0.42,0.55,0.75)
gini.add_triangular('RBad', 0.55,0.75,1)


inter = FuzzyOutputVariable('Interpretability', 0,1,13)
inter.add_triangular('Excellent', 0.8,0.9,1)
inter.add_trapezoidal('Average', 0.6, 0.7, 0.8, 0.9)
inter.add_trapezoidal('Bad', 0.3, 0.5,0.6,0.7)
inter.add_triangular('ExtraBad', 0, 0.3, 0.5)

system = FuzzySystem()
system.add_input_variable(colour)
system.add_input_variable(tree)
system.add_input_variable(gini)
system.add_output_variable(inter)

system.add_rule(
		{ 'Colour':'Excellent',
			'Tree':'Excellent','Gini':'Good'},
		{ 'Interpretability':'Excellent'})

system.add_rule(
		{ 'Colour':'Average',
			'Tree':'Excellent','Gini':'Good'},
		{ 'Interpretability':'Excellent'})

system.add_rule(
		{ 'Colour':'Bad',
			'Tree':'Excellent','Gini':'Good'},
		{ 'Interpretability':'Average'})

system.add_rule(
		{ 'Colour':'ExtraBad',
			'Tree':'Excellent','Gini':'Good'},
		{ 'Interpretability':'Bad'})

system.add_rule(
		{ 'Colour':'Excellent',
			'Tree':'Average','Gini':'Good'},
		{ 'Interpretability':'Average'})

system.add_rule(
		{ 'Colour':'Excellent',
			'Tree':'Bad','Gini':'Good'},
		{ 'Interpretability':'Bad'})

system.add_rule(
		{ 'Colour':'Excellent',
			'Tree':'ExtraBad','Gini':'Good'},
		{ 'Interpretability':'ExtraBad'})

system.add_rule(
		{ 'Colour':'Excellent',
			'Tree':'Excellent','Gini':'Good'},
		{ 'Interpretability':'Excellent'})

system.add_rule(
		{ 'Colour':'Excellent',
			'Tree':'Excellent','Gini':'LBad'},
		{ 'Interpretability':'Excellent'})

system.add_rule(
		{ 'Colour':'Excellent',
			'Tree':'Excellent','Gini':'RBad'},
		{ 'Interpretability':'Average'})

system.add_rule(
		{ 'Colour':'ExtraBad',
			'Tree':'ExtraBad','Gini':'RBad'},
		{ 'Interpretability':'ExtraBad'})

system.add_rule(
		{ 'Colour':'ExtraBad',
			'Tree':'ExtraBad','Gini':'RBad'},
		{ 'Interpretability':'ExtraBad'})

system.add_rule(
		{ 'Colour':'Average',
			'Tree':'Average','Gini':'Good'},
		{ 'Interpretability':'Average'})

system.add_rule(
		{ 'Colour':'Bad',
			'Tree':'Bad','Gini':'LBad'},
		{ 'Interpretability':'Bad'})
system.add_rule(
		{ 'Colour':'Bad',
			'Tree':'Bad','Gini':'Good'},
		{ 'Interpretability':'Bad'})
system.add_rule(
		{ 'Colour':'Average',
			'Tree':'Bad','Gini':'Good'},
		{ 'Interpretability':'Average'})
system.add_rule(
		{ 'Colour':'Bad',
			'Tree':'Average','Gini':'LBad'},
		{ 'Interpretability':'Bad'})

system.add_rule(
		{ 'Colour':'Average',
			'Tree':'Bad','Gini':'LBad'},
		{ 'Interpretability':'Bad'})

system.add_rule(
		{ 'Colour':'Average',
			'Tree':'ExtraBad','Gini':'LBad'},
		{ 'Interpretability':'Bad'})

system.add_rule(
		{ 'Colour':'Average',
			'Tree':'ExtraBad','Gini':'RBad'},
		{ 'Interpretability':'ExtraBad'})
system.add_rule(
		{ 'Colour':'Excellent',
			'Tree':'Excellent','Gini':'LBad'},
		{ 'Interpretability':'Excellent'})


output = system.evaluate_output({
				'Colour':0.1,
				'Gini':0.89,
				'Tree':0.12
		})

print(output)
# print('fuzzification\n-------------\n', info['fuzzification'])
# print('rules\n-----\n', info['rules'])

system.plot_system()
