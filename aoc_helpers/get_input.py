import os
import requests as requests

session = None
if os.path.exists('session.txt'):
    with open('session.txt', 'r') as f:
        session = f.read().replace('\n', '')
if not session:
    session = input("Please paste your session cookie (you can get this from your browser's dev tools):\n")
    with open('session.txt', 'w') as f:
        f.write(session)

base_url = 'https://adventofcode.com'


def get_url(day: str):
    return f'{base_url}/2021/day/{day}/input'


def get_input(day: int, home_dir: str = os.getenv('HOME')):
    current_day_input = os.path.join(home_dir, f'aoc_input/input-{day}.txt')
    if not os.path.exists(current_day_input):
        os.makedirs(os.path.join(f'{home_dir}', 'aoc_input'), exist_ok=True)
        url = get_url(str(day))
        req = requests.get(url, cookies={'session': session})
        if req.status_code == 200:
            with open(current_day_input, 'w') as f:
                f.write(req.text)
            return req.text
        else:
            print(req.status_code, url)
    else:
        with open(current_day_input, 'r') as f:
            return f.read()


if __name__ == '__main__':
    get_input(int(input('day: ')))
