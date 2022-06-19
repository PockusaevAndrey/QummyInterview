from server import serve
from server.QummyApplication import Application

if __name__ == "__main__":
    serve(Application(), 8000)
