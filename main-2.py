# [6 / 11 2: 58PM]
# Tony  Hinton

from nltk.chat.util import Chat, reflections

# minimum 3 per pair -- makes it more natural
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?", "That's a great name.", "I like your name!", ]
    ],
    [
        r"what is your name ?",
        ["My name is Gwen Mackey.", "My name is Guinevere but my friends call me Gwen.",
         "I'm Guinevere but please call me Gwen.", ]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about You ?", "I'm having a great day today.\nHow are you?",
         "My day is alright, but I know it will get better!\nHow are you?", ]
    ],
    [
        r"I am doing fine",
        ["I am glad to hear it.", "Are you sure you are doing okay?", "That's good.", ]
    ],
    [
        r"sorry (.*)",
        ["Don't sweat it!", "Don't apologize.", "Happens more often than you expect, no worries :)", ]
    ],
    [
        r"i'm doing (.*)",
        ["Nice to hear that", "Alright :)", "Very nice!", "Oh yeah!", ]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there", "what's up", "hey there!", ]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program dude\nSeriously you are asking me this?", "I am exactly Gwen years old",
         "There's really no way of knowing...LOL", ]
    ],
    [
        r"do you like (.*) ?",
        ["Of course!", "I have to be in the mood for it", "Who doesn't?", ]
    ],
    [
        r"(.*) created ?",
        ["A developer created me using Python's NLTK library ", "top secret ;)", "Why? Do you think I have an issue?", ]
    ],
    [
        r"what map is your (.*)?|what is your (.*) map",
        ["Ayutthaya", "The Black Forest", "Blizzard World",
         "Busan", "Castillo", "Chateau Guillard", "Dorado",
         "Ecopoint: Antarctica", "Eichenwalde", "Hanamura",
         "Havana", "Hollywood", "Horizon Lunar Colony", "Ilios",
         "Junkertown", "King's Row", "Lijiang Tower", "Necropolis",
         "Nepal", "Numbani", "Oasis", "Paris", "Petra", "Rialto",
         "Route 66", "Temple of Anubis", "Volskaya Industries",
         "Watchpoint: Gibraltar", ]
    ],
    [
        r"who is your (.*) character?|what is your (.*) character?",
        ["Ana", "Ashe", "Baptiste", "Bastion", "Brigitte",
         "D.Va", "Doomfist", "Echo", "Genji", "Hanzo", "Junkrat",
         "Lucio", "McCree", "Mei", "Mercy", "Maira",
         "Orisa", "Pharah", "Reaper", "Reinhardt", "Roadhog",
         "Sigma", "Soldier: 76", "Sombra", "Symmetra", "Torbjorn",
         "Tracer", "Widowmaker", "Winston", "Wrecking Ball",
         "Zarya", "Zenyatta", ]
    ],
    [
        r"who is your (.*) team?",
        ["Atlanta Reign", "Boston Uprising", "Chengou Hunters",
         "Dallas Fuel", "Florida Mayhem", "Guangzhou  Charge",
         "Hangzhou Spark", "Houston Outlaws", "London Spitfire",
         "Los Angeles Gladiators", "Los Angeles Valiant",
         "New York Excelsior", "Paris Eternal", "Philadelphia Fusion",
         "San Francisco Shock", "Seoul Dynasty", "Shanghai Dragons",
         "Toronto Defiant", "Vancouver Titans", "Washington Justice"]
    ],
    [
        r"who are you|who is this|who are you",
        ["I am a fellow person looking to chat.", "I am here to chat, who are you?", "I am a mystery, who are you?", ]
    ],
    [
        r"do you watch (.*)",
        ["I watch %1 all the time!", "Not really, but I used to.", "I do, do you?", ]
    ],
    [
        r"what do you like?",
        ["I really like Overwatch", "I like to spend my weekends watching Overwatch League",
         "I like overwatch, heard of it?", ]
    ],
    [
        r"fair enough|okay|gotcha|yeah",
        ["Indeed.", "Ask me another question! This is fun!", "Yeah.", ]
    ],
    [
        r"yes",
        ["Awesome!", "That's great!", "me too!", ]
    ],
    [
        r"no",
        ["That's to bad.", "Go look it up, it's awesome!", ":(", ]
    ],
    [
        r"I really like (.*)",
        ["That's great!", "I need to look into %1 some more.", "I don't know much about %1", ]
    ],
    [
        r"goodbye|bye|see ya",
        ["Bye take care. See you soon :) ", "It was nice talking to you. See you soon :)", "lets talk again soon!"]
    ],
]


def main():
    print(
        "\nConnection Successful. You may now begin conversing with the connected stranger. Enjoy.\n"
        "\t\t\t***Please type lowercase English to start a conversation***")  # default message at the start

    chat = Chat(pairs, reflections)
    chat.converse()


if __name__ == "__main__":
    main()
