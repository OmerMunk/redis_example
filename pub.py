import redis
import json

redis_client = redis.Redis(host='localhost', port=6379, db=0)

transaction = {
    'sender': 'Ahmad',
    'receiver': 'Shuku',
    'amount': 1_000
}

redis_client.publish(
    'transaction-channel',
    json.dumps(transaction)
)