from project import create_app
from project.config import Production


app = create_app(config=Production)

if __name__ == '__main__':
    app.run(debug=True)
