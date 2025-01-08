user_preferences = {
    "timezone": "GMT",
    "language": "English",
    "notifications": None,
    "currency": "USD",
    "theme": None
}


def update_preferences(user_pref):
    # update_preferences = {}
    # for key, value in user_pref.items():
    #     if value is not None:
    #         update_preferences[key] = value
    # return update_preferences
    return {key:value for key, value in user_pref.items() if value is not None}


print(update_preferences(user_preferences))
