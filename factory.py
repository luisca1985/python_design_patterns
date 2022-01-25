"""
Python Code for factory method
it comes under the creational
Design Pattern
"""


class FrenchLocalizer:
    """ it simply returns the french version"""

    def __init__(self):
        self.translations = {
            "car": "voiture",
            "bike": "bicyclette",
            "cycle": "cyclette"
        }

    def localize(self, msg):
        """change the message using translations"""
        return self.translations.get(msg, msg)


class SpanishLocalizer:
    """ it simply returns the spanish version """

    def __init__(self):
        self.translations = {
            "car": "coche",
            "bike": "bicileta",
            "cycle": "cicla"
        }

    def localize(self, msg):
        return self.translations.get(msg, msg)


class EnglishLocalizer:
    def localize(self, msg):
        return msg

def Factory(language="English"):
    """Factory Method"""
    localizers = {
        "French": FrenchLocalizer,
        "English": EnglishLocalizer,
        "Spanish": SpanishLocalizer
    }

    return localizers[language]()

if __name__ == "__main__":
    f = Factory("French")
    e = Factory("English")
    s = Factory("Spanish")

    messages = ["car", "bike", "cycle"]

    for msg1 in messages:
        print(f.localize(msg1))
        print(e.localize(msg1))
        print(s.localize(msg1))
