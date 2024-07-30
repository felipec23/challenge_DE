from typing import List, Tuple

import json
import regex as re
from collections import Counter
from memory_profiler import profile

# Compile emoji pattern once
emoji_pattern = emoji_pattern = re.compile(
    r"[\p{Emoji_Presentation}\p{Extended_Pictographic}]"
)


def read_json_q2_memory(file_path: str):
    """
    Función que lee un archivo json y retorna el content de los tweets.

    :param file_path: str con la ruta del archivo JSON.
    :return: Generador de strings con el content de los tweets.
    """
    # Se abre en binario para orjson
    with open(file_path, "rb") as f:
        for linea in f:
            try:
                # Se devuelve el contenido a través de un generador
                yield json.loads(linea).get("content")

            except Exception as e:
                print(f"Error al leer una línea JSON: {e}. Línea: {linea}")
                continue


def get_emojis_from_tweet(tweet: str) -> List[str]:

    """
    Función que extrae los emojis de un tweet.

    :param tweet: str con el contenido del tweet.
    :return: Lista de emojis en el tweet.
    """
    return emoji_pattern.findall(tweet)


@profile
def q2_memory(file_path: str) -> List[Tuple[str, int]]:

    """
    Función que retorna los 10 emojis más usados en los tweets.

    :param file_path: str con la ruta del archivo JSON.
    :return top_10_emojis: Lista de tuplas con el emoji y la cantidad de veces que aparece.
    """

    # Se inicializa un contador de emojis
    emoji_counter = Counter()

    # Se reciben los tuits del generador y se actualiza el contador
    for content in read_json_q2_memory(file_path):
        emoji_counter.update(get_emojis_from_tweet(content))

    # Se obtienen los 10 emojis más usados
    return emoji_counter.most_common(10)


if __name__ == "__main__":

    # Solicitar el nombre del archivo, que debe estar dentro de data
    import os
    import sys

    # Revisar si el script recibió el argumento requerido
    if len(sys.argv) < 2:
        print("Usage: python q2_memory.py <file_name>")
        sys.exit(1)

    # Solicitar el nombre del archivo, que debe estar dentro de data
    ruta = sys.argv[1]
    file_path = os.path.join(os.path.dirname(__file__), "data", ruta)
    print(q2_memory(file_path))
