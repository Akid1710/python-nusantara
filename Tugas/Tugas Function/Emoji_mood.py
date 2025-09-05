def convert_mood(mood_list):
    mood_dict ={
        "senang":"😀",
        "biasa": "😐",
        "sedih": "😢",
        "semangat": "💪,"
    }


    return list(map(lambda mood: mood_dict.get(mood.lower(), "❓"), mood_list))
