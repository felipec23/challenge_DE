from src.q2_memory import get_emojis_from_tweet as get_emojis_from_tweet_memory
from src.q2_time import get_emojis_from_tweet as get_emojis_from_tweet_time


def test_get_emojis_from_tweet_memory():

    tweets = [
        "The world progresses while the Indian police and Govt are still trying to take India back to the horrific past through its tyranny. \n\n@narendramodi @DelhiPolice Shame on you. \n\n#ModiDontSellFarmers \n#FarmersProtest \n#FreeNodeepKaur https://t.co/es3kn0IQAF",
        "#FarmersProtest \n#ModiIgnoringFarmersDeaths \n#ModiDontSellFarmers \n@Kisanektamorcha \nFarmers constantly distroying crops throughout India. \nReally, it's hearts breaking...we care about our crops like our children. And govt. agriculture minister is laughing on us🚜🌾WE WILL WIN💪 https://t.co/kLspngG9xE",
        "ਪੈਟਰੋਲ ਦੀਆਂ ਕੀਮਤਾਂ ਨੂੰ ਮੱਦੇਨਜ਼ਰ ਰੱਖਦੇ ਹੋਏ \nਮੇਰੇ ਹਿਸਾਬ ਨਾਲ ਬਾਹਰ(ਪ੍ਰਦੇਸ਼) ਜਾਣ ਨਾਲੋਂ ਬਿਹਤਰ ਆ ਭਾਰਤ 'ਚ ਪੈਟਰੋਲ ਪੰਪ ਪਾ ਲਈਏ। 🤫🤫🤔🤔\n#FarmersProtest",
        "@ReallySwara @rohini_sgh watch full video here https://t.co/wBPNdJdB0n\n#farmersprotest #NoFarmersNoFood https://t.co/fUsTOKOcXK",
        "#KisanEktaMorcha #FarmersProtest #NoFarmersNoFood https://t.co/g9TYYBHQRH",
    ]

    emojis = [get_emojis_from_tweet_memory(tweet) for tweet in tweets]
    truth = [[], ["🚜", "🌾", "💪"], ["🤫", "🤫", "🤔", "🤔"], [], []]
    assert emojis == truth


def test_get_emojis_from_tweet_time():

    tweets = [
        "The world progresses while the Indian police and Govt are still trying to take India back to the horrific past through its tyranny. \n\n@narendramodi @DelhiPolice Shame on you. \n\n#ModiDontSellFarmers \n#FarmersProtest \n#FreeNodeepKaur https://t.co/es3kn0IQAF",
        "#FarmersProtest \n#ModiIgnoringFarmersDeaths \n#ModiDontSellFarmers \n@Kisanektamorcha \nFarmers constantly distroying crops throughout India. \nReally, it's hearts breaking...we care about our crops like our children. And govt. agriculture minister is laughing on us🚜🌾WE WILL WIN💪 https://t.co/kLspngG9xE",
        "ਪੈਟਰੋਲ ਦੀਆਂ ਕੀਮਤਾਂ ਨੂੰ ਮੱਦੇਨਜ਼ਰ ਰੱਖਦੇ ਹੋਏ \nਮੇਰੇ ਹਿਸਾਬ ਨਾਲ ਬਾਹਰ(ਪ੍ਰਦੇਸ਼) ਜਾਣ ਨਾਲੋਂ ਬਿਹਤਰ ਆ ਭਾਰਤ 'ਚ ਪੈਟਰੋਲ ਪੰਪ ਪਾ ਲਈਏ। 🤫🤫🤔🤔\n#FarmersProtest",
        "@ReallySwara @rohini_sgh watch full video here https://t.co/wBPNdJdB0n\n#farmersprotest #NoFarmersNoFood https://t.co/fUsTOKOcXK",
        "#KisanEktaMorcha #FarmersProtest #NoFarmersNoFood https://t.co/g9TYYBHQRH",
    ]

    emojis = [get_emojis_from_tweet_time(tweet) for tweet in tweets]
    truth = [[], ["🚜", "🌾", "💪"], ["🤫", "🤫", "🤔", "🤔"], [], []]
    assert emojis == truth
