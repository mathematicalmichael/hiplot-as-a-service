from wsgiref.simple_server import make_server
import io
import urllib.parse
import experiment as hip

def app(environ, start_response):
    # Route to requested handler.
    if environ["PATH_INFO"] == "/h":
        return main(environ, start_response)
    
    start_response("404 Not Found", [])
    return [b"Page not found."]

def main(environ, start_response):
    # Read the request body
    content_length = int(environ.get("CONTENT_LENGTH", 0))
    request_body = environ['wsgi.input'].read(content_length).decode('utf-8')
    
    # Parse the form data
    params = urllib.parse.parse_qs(request_body)
    data = params.get("data", [None])[0]
    
    if data is None:
        start_response("400 Bad Request", [("Content-Type", "text/html")])
        return [b"Missing 'data' parameter."]

    # Process the data
    data_io = io.StringIO(data)
    out = hip.Experiment.from_csv(data_io).to_html()

    headers = [("Content-Type", "text/html")]
    start_response("200 OK", headers)
    return [out.encode("utf-8")]

if __name__ == "__main__":
    httpd = make_server('', 8081, app)
    print("Serving on port 8081...")
    httpd.serve_forever()
