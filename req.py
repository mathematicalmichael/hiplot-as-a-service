import csv
import io
import json
import requests


def post_data(data, url="http://192.168.0.125:1234/h", sorted=False, strip=False) -> str:
    """
    Creates CSV file in memory and posts it to `url` as multipart/form-data.
    """
    if sorted:
        keys = sorted(data.keys())
    else:
        keys = list(data.keys())

    inmem = io.StringIO()
    csv_writer = csv.writer(inmem)
    csv_writer.writerow(keys)
    csv_writer.writerows(zip(*[data[k] for k in keys]))
    r = requests.post(url, files={'data': inmem.getvalue()})
    if strip:
        return r.content.decode('utf-8').replace('<!DOCTYPE html>\n\n<html>', '').replace('</html>','')
    return r.content.decode('utf-8')


if __name__ == "__main__":

    data = {
        'total': [1, 3, 5],
        'a': [0, 1, 2],
        'b': [1, 2, 3]
    }

    print(post_data(data)[:100])

