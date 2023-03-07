import argparse
import extractdata
import databaseop
import urllib.request


def fetchincidents(url):
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    data = urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read()
    return data

def main(args):

    url = args.incidents
    incident_data = fetchincidents(url)
    incidents = extractdata.extractincidents(incident_data)
    db = databaseop.createdb()
    databaseop.populatedb(db, incidents)
    databaseop.status(db)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--incidents",
                        type=str,
                        required=True,
                        help="Incident summary url")

    args = parser.parse_args()
    if args.incidents:
        main(args)
