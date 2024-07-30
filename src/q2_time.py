from typing import List, Tuple

import orjson  # Faster and more memory-efficient JSON parser
import regex as re
from collections import Counter

# Compile emoji pattern once
emoji_pattern = emoji_pattern = re.compile(
    r'[\p{Emoji_Presentation}\p{Extended_Pictographic}]'
)

def read_json_q2_time(file_path: str):
    """
    Función que lee un archivo json y retorna el content de los tweets.

    :param file_path: str con la ruta del archivo JSON.
    :return: Generador de strings con el content de los tweets.
    """
    # Se abre en binario para orjson
    with open(file_path, "rb") as f:  
        for linea in f:
            try:
                tweet = orjson.loads(linea)
                yield tweet.get("content")

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

def q2_time(file_path: str) -> List[Tuple[str, int]]:

    """
    Función que retorna los 10 emojis más usados en los tweets.

    :param file_path: str con la ruta del archivo JSON.
    :return top_10_emojis: Lista de tuplas con el emoji y la cantidad de veces que aparece.
    """

    # Se inicializa un contador de emojis
    emoji_counter = Counter()

    # Se reciben los tuits del generador y se actualiza el contador
    for content in read_json_q2_time(file_path):
        emojis = get_emojis_from_tweet(content)
        emoji_counter.update(emojis)

    # Se obtienen los 10 emojis más usados
    top_10_emojis = emoji_counter.most_common(10)

    return top_10_emojis

if __name__ == "__main__":
    print(q2_time(file_path="../data/farmers-protest-tweets-2021-2-4.json"))