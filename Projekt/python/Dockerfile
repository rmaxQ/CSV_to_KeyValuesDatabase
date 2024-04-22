# Ustaw obraz bazowy z Pythonem
FROM python:3.10

# Ustaw katalog roboczy w kontenerze
WORKDIR /python

# Skopiuj pliki aplikacji do kontenera
COPY . /python/

# Zainstaluj zależności
RUN pip install redis

# Ustaw zmienne środowiskowe
ENV REDIS_HOST=redis
ENV REDIS_PORT=6379

# Uruchom aplikację
CMD ["python", "Konwerter.py"]