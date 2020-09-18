from application import app

if __name__ == "__main__":
    app.jinja_env.cache = {}
    app.run()
