import httpx
import redis


def cache_wrapper(func_to_cache):
    client = redis.Redis()

    def inner(*args):
        if not client.get(*args):
            client.set(*args, func_to_cache(*args))
            print('web')
            return func_to_cache(name)
        print('redis')
        return client.get(name).decode()
    return inner


@cache_wrapper
def get_info_from_API(name):
    with httpx.Client() as web_client:
        base_url = 'https://api.nationalize.io?name'
        url = f'{base_url}={name}'

        response = web_client.get(url)
        return response.json()['country'][0]['country_id']


if __name__ == '__main__':
    # EXAMPLE
    names = ['rost', 'petr', 'jack', 'jackob', 'bohdan', 'roman']
    for name in names:
        print(get_info_from_API(name))
