from random import sample

RELATIVES = {
    "caca": "father's brother",
    "caci(amma)": "father's brother's wife",
    "fupu": "father's sister",
    "fupa": "father's sister's husband",
    "mama": "mother's brother",
    "mami": "mother's brother's wife",
    "khala(amma)": "mother's sister",
    "khalu": "mother's sister's husband",
    # "bhagne": "sister's son",
    # "bhagni": "sister's daughter",
    # "shami": "husband",
    # "stri": "wife",
    # "bacca": "child"
}
num_res = 0
num_corr = 0
end_game = False

print("Let's see what you know 🤓. Type 'quit' to quit")
while not end_game:
    example = sample(sorted(RELATIVES), 1)
    response = ""
    answer = RELATIVES[example[0]]
    while response != answer:
        num_res += 1
        response = input(f"What is {example[0]}?\n")
        if response == "quit":
            print(f"Score: {num_corr}/{num_res - 1}")
            end_game = True
            break
    num_corr += 1
    print("khub bhalo!")
