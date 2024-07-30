from typing import List, Tuple
import orjson
from collections import Counter
from memory_profiler import profile


def read_json_q3_memory(file_path: str):
    """
    Función que lee un archivo json y retorna los usuarios mencionados en los tweets.

    :param file_path: str con la ruta del archivo JSON.
    :return: Generador de strings con el content de los tweets.
    """
    # Se abre en binario para orjson
    with open(file_path, "rb") as f:
        for linea in f:
            try:
                mentioned_users = orjson.loads(linea).get("mentionedUsers")
                if mentioned_users:
                    yield [user.get("username") for user in mentioned_users]

            except Exception as e:
                print(f"Error al leer una línea JSON: {e}. Línea: {linea}")
                continue


@profile
def q3_memory(file_path: str) -> List[Tuple[str, int]]:

    """
    Función que retorna los 10 usuarios más mencionados en los tweets.

    :param file_path: str con la ruta del archivo JSON.
    :return top_10_users: Lista de tuplas con el usuario y la cantidad de veces que aparece.
    """

    # Se inicializa un contador de usuarios
    user_counter = Counter()

    # Se reciben los tuits del generador y se actualiza el contador
    for mentioned_users_list in read_json_q3_memory(file_path):
        user_counter.update(mentioned_users_list)

    # Se obtienen los 10 usuarios más mencionados
    return user_counter.most_common(10)


if __name__ == "__main__":

    # Solicitar el nombre del archivo, que debe estar dentro de data
    import os
    import sys

    # Revisar si el script recibió el argumento requerido
    if len(sys.argv) < 2:
        print("Usage: python q3_memory.py <file_name>")
        sys.exit(1)

    # Solicitar el nombre del archivo, que debe estar dentro de data
    ruta = sys.argv[1]
    file_path = os.path.join(os.path.dirname(__file__), "data", ruta)
    print(q3_memory(file_path))
