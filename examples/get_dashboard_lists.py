

import json
import crowdtangle as ct

def main():
    with open("sample_keys.json", "r") as file:
        creds = json.load(file)
    client = ct.Client(creds['CROWDTANGLE_DASHBOARD_KEY'])
    lsts = client.lists(types=['LIST'])
    for lst in lsts:
        for a in client.accounts(lst):
            print(a.name)

    for p in client.posts():
        print(p.id)
        if hasattr(p, 'description'):
            print(p.description)


if __name__ == "__main__":
    main()