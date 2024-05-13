"""Import flask and server executor"""
from flask import Flask
from quadratic_server import QuadraticServerExecutor

if __name__ == "__main__":
    app = Flask(__name__)
    executor = QuadraticServerExecutor()

    @app.route('/')
    def index():
        """Handle index route"""
        return executor.handle_index()

    @app.route('/', methods=['post', 'get'])
    def form():
        """Handle posts and gets from index route"""
        return executor.handle_form()

    app.run()
