from typing import List, Tuple
from datetime import datetime, date
from collections import defaultdict, Counter
import orjson

def read_json_q1_time(file_path: str):

    """
    Función que lee un archivo json y retorna los datos de las columnas especificadas.

    :param file_path: str con la ruta del archivo JSON.
    :return: Generador de listas con los datos de las columnas especificadas.
    """

    # Abrimos el archivo y leemos línea por línea
    with open(file_path, "r") as f:
        for line in f:
            try:
                # Cargar la línea como un diccionario
                tweet = orjson.loads(line)

                # El generador retorna el usuario y la fecha del tweet
                yield [tweet.get("user", {}).get("username"), tweet.get("date").split("T")[0]]

            except Exception as e:
                # En caso de que alguna fila no se pueda parsear, se imprime un mensaje de error
                print(f"Error while reading a JSON line: {e}. Line: {line}")
                continue

def q1_time(file_path: str) -> List[Tuple[date, str]]:

    """
    Función que retorna los 10 días con más tweets y el usuario que más tweets hizo en cada uno de esos días.

    :param file_path: str con la ruta del archivo JSON.
    :return top_users_per_date: Lista de tuplas con la fecha y el usuario con más tweets en esa fecha.
    """

    # Inicializar diccionario de contadores
    date_user_counter = defaultdict(Counter)

    # Leer el archivo JSON y contar los tweets por usuario y fecha
    for user, date_str in read_json_q1_time(file_path):
        date = datetime.fromisoformat(date_str).date()
        date_user_counter[date][user] += 1

    # Encontrar los 10 días con más tweets
    top_10_dates = sorted(date_user_counter.items(), key=lambda x: sum(x[1].values()), reverse=True)[:10]

    # Por cada uno de los 10 días, encontrar el usuario con más tweets
    top_users_per_date = [(date, user_counter.most_common(1)[0][0]) for date, user_counter in top_10_dates]

    return top_users_per_date


if __name__ == "__main__":
    print(q1_time(file_path="../data/farmers-protest-tweets-2021-2-4.json"))