from typing import List, Tuple
import orjson
from collections import Counter


def read_json_q3_time(file_path: str):
    """
    Función que lee un archivo json y retorna los usuarios mencionados en los tweets.

    :param file_path: str con la ruta del archivo JSON.
    :return: Generador de strings con el content de los tweets.
    """
    # Se abre en binario para orjson
    with open(file_path, "rb") as f:
        for linea in f:
            try:
                tweet = orjson.loads(linea)
                mentioned_users = tweet.get("mentionedUsers")
                if mentioned_users:
                    mentioned_users_list = [
                        user.get("username") for user in mentioned_users
                    ]
                    yield mentioned_users_list

            except Exception as e:
                print(f"Error al leer una línea JSON: {e}. Línea: {linea}")
                continue


def q3_time(file_path: str) -> List[Tuple[str, int]]:

    """
    Función que retorna los 10 usuarios más mencionados en los tweets.

    :param file_path: str con la ruta del archivo JSON.
    :return top_10_users: Lista de tuplas con el usuario y la cantidad de veces que aparece.
    """

    # Se inicializa un contador de usuarios
    user_counter = Counter()

    # Se reciben los tuits del generador y se actualiza el contador
    for mentioned_users_list in read_json_q3_time(file_path):
        user_counter.update(mentioned_users_list)

    # Se obtienen los 10 usuarios más mencionados
    top_10_users = user_counter.most_common(10)

    return top_10_users


if __name__ == "__main__":

    import os
    import sys

    # Check if the script received the required argument
    if len(sys.argv) < 2:
        print("Usage: python q3_time.py <file_name>")
        sys.exit(1)

    # Solicitar el nombre del archivo, que debe estar dentro de data
    ruta = sys.argv[1]
    file_path = os.path.join(os.path.dirname(__file__), "data", ruta)
    print(q3_time(file_path))
