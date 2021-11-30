import httpx
import redis


def get_info_from_API(name):
    with httpx.Client() as web_client:
        base_url = 'https://api.nationalize.io?name'
        url = f'{base_url}={name}'

        response = web_client.get(url)
        return response.json()['country'][0]['country_id']


def get_info_from_cache(name, client):
    val = client.get(name)
    return val


def set_info_from_cache(name, val, client):
    data = client.set(name, val)
    return data


def cache_analyzer(name, client):

    data = get_info_from_cache(name, client)
    if data:
        print(f'{data.decode("utf-8")} and its country from cache')
    else:
        data = get_info_from_API(name)
        print(f'{data} and this country from WEB')
        if data:
            load_state = set_info_from_cache(name=name, val=data, client=client)
            return load_state


if __name__ == '__main__':
    redis_client = redis.Redis()

    cache_analyzer('boris', redis_client)
    cache_analyzer('petr', redis_client)
    cache_analyzer('boris', redis_client)
    cache_analyzer('john', redis_client)
    cache_analyzer('jhon', redis_client)
    cache_analyzer('ivan', redis_client)
