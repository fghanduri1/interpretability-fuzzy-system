from fuzzy_system.fuzzy_variable_output import FuzzyOutputVariable
from fuzzy_system.fuzzy_variable_input import FuzzyInputVariable
from fuzzy_system.fuzzy_system import FuzzySystem

colour = FuzzyInputVariable('Colour', 1, 100)
colour.add_triangular('Excellent', 1, 2)
colour.add_triangular('Average', 3, 5)
colour.add_triangular('Bad', 25, 40)
colour.add_triangular('ExtraBad', 25, 100)

tree = FuzzyInputVariable('Tree', 1, 500,3000)
tree.add_triangular('Excellent', 1, 14)
tree.add_trapezoidal('Average', 15, 20)
tree.add_triangular('Bad', 21, 30)
tree.add_triangular('ExtraBad', 31, 500,3000)

gini = FuzzyInputVariable('Gini', 0, 1, 1)
gini.add_triangular('Excellent', 0.45, 0.55)
gini.add_triangular('Average', 0.35, 0.44, 0.56,0.75)
gini.add_triangular('Bad', 0.25, 0.34, 0.76,0.85)
gini.add_triangular('ExtraBad', 0,0.24, 0.86, 1)

inter = FuzzyOutputVariable('Interpretability', 0,10)
inter.add_triangular('Excellent', 8, 10)
inter.add_triangular('Average', 6, 7)
inter.add_triangular('Bad', 3, 5)
inter.add_triangular('ExtraBad', 0, 2)

system = FuzzySystem()
system.add_input_variable(colour)
system.add_input_variable(tree)
system.add_input_variable(gini)
system.add_output_variable(inter)

system.add_rule(
		{ 'Colour':'Excellent',
			'Tree':'Excellent','Gini':'Excellent'},
		{ 'Interpretability':'Excellent'})

system.add_rule(
		{ 'Colour':'Average',
			'Tree':'Excellent','Gini':'Excellent'},
		{ 'Interpretability':'Excellent'})

system.add_rule(
		{ 'Colour':'Bad',
			'Tree':'Excellent','Gini':'Excellent'},
		{ 'Interpretability':'Average'})

system.add_rule(
		{ 'Colour':'ExtraBad',
			'Tree':'Excellent','Gini':'Excellent'},
		{ 'Interpretability':'Bad'})

system.add_rule(
		{ 'Colour':'Excellent',
			'Tree':'Average','Gini':'Excellent'},
		{ 'Interpretability':'Average'})

system.add_rule(
		{ 'Colour':'Excellent',
			'Tree':'Bad','Gini':'Excellent'},
		{ 'Interpretability':'Bad'})

system.add_rule(
		{ 'Colour':'Excellent',
			'Tree':'ExtraBad','Gini':'Excellent'},
		{ 'Interpretability':'ExtraBad'})

system.add_rule(
		{ 'Colour':'Excellent',
			'Tree':'Excellent','Gini':'Average'},
		{ 'Interpretability':'Excellent'})

system.add_rule(
		{ 'Colour':'Excellent',
			'Tree':'Excellent','Gini':'Bad'},
		{ 'Interpretability':'Excellent'})

system.add_rule(
		{ 'Colour':'Excellent',
			'Tree':'Excellent','Gini':'ExtraBad'},
		{ 'Interpretability':'Average'})

system.add_rule(
		{ 'Colour':'ExtraBad',
			'Tree':'ExtraBad','Gini':'ExtraBad'},
		{ 'Interpretability':'ExtraBad'})

system.add_rule(
		{ 'Colour':'ExtraBad',
			'Tree':'ExtraBad','Gini':'ExtraBad'},
		{ 'Interpretability':'ExtraBad'})

system.add_rule(
		{ 'Colour':'Average',
			'Tree':'Average','Gini':'Average'},
		{ 'Interpretability':'Average'})

system.add_rule(
		{ 'Colour':'Bad',
			'Tree':'Bad','Gini':'Bad'},
		{ 'Interpretability':'Bad'})

output = system.evaluate_output({
				'Colour':5,
				'Interpretability':7
		})

print(output)
# print('fuzzification\n-------------\n', info['fuzzification'])
# print('rules\n-----\n', info['rules'])

system.plot_system()