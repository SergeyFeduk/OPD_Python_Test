"""Import solver and flask"""
from flask import render_template, request
from quadratic_solver import solve_quadratic


class QuadraticServerExecutor:
    """Class that handles requests from client"""


    def handle_index(self):
        """Function that returns templated index"""
        return render_template("index.html")


    def handle_form(self):
        """Function that solves equation and returns template with resulst"""
        if request.method == 'POST':
            var_a_s = request.form.get('var_a')
            var_b_s = request.form.get('var_b')
            var_c_s = request.form.get('var_c')
            if not var_a_s.isnumeric() or not var_b_s.isnumeric() or not var_c_s.isnumeric():
                return render_template('index.html', result="All inputs must be numbers")
            solution = solve_quadratic(int(var_a_s), int(var_b_s), int(var_c_s))
            if len(solution) == 0:
                return render_template('index.html', result="No solutions")
            if len(solution) == 1:
                res = "One root found: X = " + str(solution[0])
                return render_template('index.html', result=res)
            res = "Two roots found: X1 = " + str(solution[0]) + ", X2 = " + str(solution[1])
            return render_template('index.html', result=res)
