import csv
import redis

def csv_to_redis(csv_filename, redis_key, redis_port=6379, redis_db=0):
    redis_client = redis.StrictRedis(host='localhost', port=redis_port, db=redis_db, decode_responses=True)

    redis_client.flushdb()


    with open(csv_filename, 'r') as csv_file:

        csv_reader = csv.DictReader(csv_file)
        h = csv_reader.fieldnames[0]
        for row in csv_reader:
            redis_client.hset("Key "+str(row[h]), mapping=row)


if __name__ == "__main__":

    csv_filename = "./przyklad.csv"
    redis_key = "moja_baza_redis"

    csv_to_redis(csv_filename, redis_key)

    print(f"Nowa baza danych Redis została utworzona i dane z pliku CSV zostały zapisane")

