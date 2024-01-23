from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/main", response_class=HTMLResponse)
def main():
    # /board로 리다이렉션하는 링크가 있는 간단한 HTML 페이지
    return """
    <html>
        <head>
            <title>Main Page</title>
        </head>
        <body>
            <h1>Welcome to Main Page!!!!!!!</h1>
            <a href="/board">Go to Board</a>
        </body>
    </html>
    """
