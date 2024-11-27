import redis

redis_client = redis.Redis(host='localhost', port=6379, db=0)


def message_handler(message):
    print(f'Received: {message["data"].decode()}')


pubsub = redis_client.pubsub()
pubsub.subscribe(**{'transaction-channel': message_handler})
thread = pubsub.run_in_thread(sleep_time=0.001)