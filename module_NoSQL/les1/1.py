import redis

client = redis.Redis()

mike = client.pubsub()
mike.subscribe('rock_music')

alice = redis.Redis()
alice.publish('rock_music', 'Alice music')

mike.get_message()

new_music = mike.get_message()['data']
print(new_music)


