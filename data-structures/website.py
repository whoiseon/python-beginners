from requests import get

websites = (
    'https://google.com',
    'facebook.com',
    'https://airbnb.com',
    'twitter.com',
)

for website in websites:
    if not website.startswith('https://'):
        website = f'https://{website}'
    response = get(website)
    if 200 == response.status_code:
        print(f'{website} is OK!')