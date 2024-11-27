import redis

redis_client = redis.Redis(host='localhost', port=6379, db=0)
# host - The hostname of the Redis instance to connect to. Default is localhost.
# port - The port number to connect to. Default is 6379.
# db - The database number to connect to. Default is 0.

try:
    response = redis_client.ping()
    print(f"Conection to Redis: {response}")
except Exception as e:
    print(f"Error: {e}")


# setting and getting a string
redis_client.set('price', 1_000)
price = redis_client.get('price')
print(price.decode())

# incrementing a value
redis_client.set('visits', 1)
redis_client.incr('visits')


# hashes
# hashes are maps between string fields and string values
redis_client.hset('user:1000', mapping={'name': 'Sasson Shaulov', 'king_level': 100})
name = redis_client.hget('user:1000', 'name')
king_level = redis_client.hget('user:1000', 'king_level')
print(f'the name is {name.decode()} and the king level is {king_level.decode()}')

user = redis_client.hgetall('user:1000')
user = {key.decode(): value.decode() for key, value in user.items()}
print(user)


# lists
# insert
redis_client.lpush('Tfilos', 'Shachris', 'Mincha', 'Maariv')

# pop
next_tfila = redis_client.rpop('Tfilos')
print(next_tfila.decode())

# getting elements
tfilos1 = redis_client.lrange('Tfilos', 0, -1) # bring all the list
print(f'Tfilos: {[t.decode() for t in tfilos1]}')
tfilos2 = redis_client.lrange('Tfilos', 0, 2) # bring first 3
print(f'Tfilos: {tfilos2}')



# sets
redis_client.sadd('Mitsvos', 'Tefilin', 'Mezuzah', 'Shabbos')
redis_client.sadd('Mitsvos', 'Shiluas Ha Ken', 'Simuach Kala', 'Shabbos')

# get all from set
mitsvos = redis_client.smembers('Mitsvos')


# sorted sets
# sorted sets are similar to regular sets, but now every member is associated with a score
redis_client.zadd('Aveiros', {'Eating Pork': 100, 'Stealing': 150, 'Lashon Hara': 200})
aveiros = redis_client.zrange('Aveiros', 0, -1, withscores=True)



# pipeline
# דומה לטרנזקציה

# pipe = redis_client.pipeline()
# pipe.set('best_book', 'Tora')
# pipe.get('best_book')
# results = pipe.execute()
# print(results)
# how can we create an error so the execute will not work?
# pipe = redis_client.pipeline()
# pipe.set('best_book', 'Tora')
# pipe.get('best_book')
# pipe.incr('best_book')
# results = pipe.execute()
# print(results)



# save with TTL
redis_client.setex('best_movie', 60, 'The Matrix')






