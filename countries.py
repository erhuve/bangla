from random import sample

NATIONALITY = "Nationality"
LANGUAGE = "Language(s)"
ENGLISH = "English Name"

COUNTRIES = {
    "bangladesh": {
        NATIONALITY: "bangladeshi",
        LANGUAGE: "bangla",
        ENGLISH: "Bangladesh"
    },
    "bharot": {
        NATIONALITY: "bharotio",
        LANGUAGE: "hindi",
        ENGLISH: "India"
    },
    "barma": {
        NATIONALITY: "bormi",
        LANGUAGE: "bormi",
        ENGLISH: "Myanmar (Burma)"
    },
    "pakistan": {
        NATIONALITY: "pakistani",
        LANGUAGE: "urdu",
        ENGLISH: "Pakistan"
    },
    "parOssho": {
        NATIONALITY: "parshi",
        LANGUAGE: "farshi",
        ENGLISH: "Iran"
    },
    "mishOr": {
        NATIONALITY: "mishorio",
        LANGUAGE: "arbi",
        ENGLISH: "Egypt"
    },
    "cin": {
        NATIONALITY: "cina",
        LANGUAGE: "cina",
        ENGLISH: "China"
    },
    "bilat": {
        NATIONALITY: "ingrej",
        LANGUAGE: "ingreji",
        ENGLISH: "English"
    },
    "jukto-rajjo": {
        NATIONALITY: "briTish",
        LANGUAGE: "ingreji",
        ENGLISH: "UK"
    },
    "frans": {
        NATIONALITY: "fOrashi",
        LANGUAGE: "fOrashi",
        ENGLISH: "France"
    },
    "jukto-rastro": {
        NATIONALITY: "markin",
        LANGUAGE: "ingreji",
        ENGLISH: "US"
    },
}

while True:
    first, second = sample(sorted(COUNTRIES), 2)
    dialogue = ""
    answer = f"adab. aekTa prosno korte pari? ami {COUNTRIES[first][NATIONALITY]}. ami Olpo ekTu {COUNTRIES[second][LANGUAGE]} bhasha jani. apni ki {COUNTRIES[second][NATIONALITY]}?"
    while dialogue != answer:
        dialogue = input(
            f"Pretend you are from {first} ({COUNTRIES[first][ENGLISH]}) and ask if someone is from {second} ({COUNTRIES[second][ENGLISH]})\n")
    print("khub bhalo!")
