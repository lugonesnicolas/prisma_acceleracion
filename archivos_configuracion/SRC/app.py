import os
from dotenv import load_dotenv, find_dotenv
# from decouple import config

# print(config('POSTGRESQL_HOST'))
# print(config('POSTGRESQL_PORT'))
# print(config('POSTGRESQL_USER'))
# print(config('POSTGRESQL_PWD'))

# print('Host {HOST} - Puerto: {PORT}'.format(HOST=config('POSTGRESQL_HOST'), PORT=config('POSTGRESQL_PORT')))

load_dotenv(find_dotenv())
print(os.getenv('POSTGRESQL_HOST'))
print(os.getenv('POSTGRESQL_PORT'))
print(os.getenv('POSTGRESQL_USER'))
print(os.getenv('POSTGRESQL_PWD'))