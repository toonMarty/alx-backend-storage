# 0. Writing strings to Redis
A python script that creates a class Cache that writes strings to Redis

# 1. Reading from Redis and recovering original type
creating a get method that takes a key string argument and an optional Callable argument named fn. This callable is used to convert the data back to the desired format.
The method also conserves the original Redis.get behavior if the key does not exist.
Also, there is the implementation of  2 new methods: get_str and get_int that automatically parametrize Cache.get with the correct conversion function.
