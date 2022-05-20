import requests


def get_superhero_intelligence(name: str, token: str) -> int | None:
    url = f'https://superheroapi.com/api/{token}/search/{name}'
    try:
        response = requests.get(url)
        if response.ok:
            if response.json()['response'] == 'success':
                return int(response.json()['results'][0]['powerstats']['intelligence'])
            elif response.json()['response'] == 'error':
                raise Exception(response.json()['error'])
        else:
            raise Exception(response.status_code)
    except Exception as error:
        print(f'Error: {error}')


def find_most_intelligent_superhero(superheroes: dict) -> str:
    max_intelligence = 0
    most_intelligent_superhero = ''
    for superhero_name, superhero_intelligence in superheroes.items():
        if superhero_intelligence > max_intelligence:
            most_intelligent_superhero = superhero_name
    return most_intelligent_superhero


if __name__ == '__main__':
    my_token = '2619421814940190'
    superheroes = ['Hulk', 'Captain America', 'Thanos']
    superheroes_intelligence = {_: get_superhero_intelligence(_, my_token) for _ in superheroes}
    print(find_most_intelligent_superhero(superheroes_intelligence))

