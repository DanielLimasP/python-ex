# Python the hard way: excercise 48
# Advanced user input. Basically create a parser

lexicon = {
    "north": "direction",
    "south": "direction",
    "east": "direction",
    "west": "direction",
    "up": "direction",
    "down": "direction",
    "left": "direction",
    "right": "direction",
    "go": "verb",
    "kill": "verb",
    "eat": "verb",
    "stop": "verb",
    "princess": "noun",
    "bear": "noun",
    "door": "noun",
    "cabinet": "noun",
    "the": "stop",
    "in": "stop",
    "of": "stop"
}


def scan_lexicon(raw_sentence: str):
    words = raw_sentence.split(" ")
    new_sentence = []
    for word in words:
        if word in lexicon:
            word_sentence = (lexicon[word], word)
        elif word.isnumeric():
            word_sentence = ("number", word)
        else:
            word_sentence = ("error", word)
        new_sentence.append(word_sentence)
    return new_sentence


if __name__ == "__main__":
    loop_control = True
    print(scan_lexicon("go north"))
    while(loop_control):
        user_input = input("> ")
        if user_input == "exit":
            loop_control = False
            break
        print(scan_lexicon(user_input))
