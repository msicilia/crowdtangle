

import json
import crowdtangle as ct

def main():
    with open("sample_keys.json", "r") as file:
        creds = json.load(file)
    print(creds['CROWDTANGLE_DASHBOARD_KEY'])
    client = ct.Client(creds['CROWDTANGLE_DASHBOARD_KEY'])
    print(list(client.lists(types=['LIST'])))


if __name__ == "__main__":
    main()