from io import StringIO
import webview
from server import app

if __name__ == '__main__':
    window = webview.create_window('Pyweb', app)
    webview.start(debug=True)