import cgi
import experiment as hip
import io

def app(environ, start_response):
  # Route to requested handler.
  if environ["PATH_INFO"] == "/h":
    return main(environ, start_response)
  start_response("404 Not Found", [])
  return [b"Page not found."]

def main(environ, start_response):
  form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)
  data = io.BytesIO(form["data"].value)
  data = io.TextIOWrapper(data, encoding='utf-8').read()
  data = io.StringIO(data)
  out = hip.Experiment.from_csv(data).to_html()

  headers = [
    ("Content-Type", "text/html")
  ]
  start_response("200 OK", headers)
  return [out.encode("utf-8")]

