"""Import unit test module, solver and server"""
import unittest
import requests
import bs4
from quadratic_solver import solve_quadratic


class TestQuadraticSolver(unittest.TestCase):
    """Class that tests solver and flask server"""


    def test_solver(self):
        """Unit test for solver"""
        self.assertEqual(solve_quadratic(4, 4, 1), [-.5])
        self.assertEqual(solve_quadratic(2, 3, 1), [-0.5, -1])
        self.assertEqual(solve_quadratic(8, 6, 1), [-.25, -.5])


    def test_server_availability(self):
        """Unit test to find if server is available or not"""
        response = requests.get('http://127.0.0.1:5000/', timeout = 10)
        self.assertEqual(response.status_code, 200)


    def request_solution(self,a,b,c):
        """Request solution for a,b,c and return resulting string"""
        request_session = requests.Session()
        headers = {'User-Agent': 'Mozilla/5.0'}
        data = {'var_a': a, 'var_b': b, 'var_c' : c}
        result = request_session.post('http://127.0.0.1:5000/', headers = headers, data = data)
        #Parse result
        soup = bs4.BeautifulSoup(result.text, "html.parser")
        return soup.find('h1').text

    def test_server_submission(self):
        """Unit test to find if server solves equations correctly"""
        self.assertEqual(self.request_solution(0,0,0),"No solutions")
        self.assertEqual(self.request_solution(4,4,2),"No solutions")
        self.assertEqual(self.request_solution(1,12,36),"One root found: X = -6.0")
        self.assertEqual(self.request_solution("4",4,"2"),"No solutions")
        self.assertEqual(self.request_solution("1",12,"36"),"One root found: X = -6.0")
        self.assertEqual(self.request_solution("Banana", "Pineapple", "Fork"),"All inputs must be numbers")



if __name__ == "__main__":
    unittest.main()
