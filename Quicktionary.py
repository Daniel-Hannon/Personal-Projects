import random
import PySimpleGUI as sg
sg.theme("LightGray1")

blue_card_rules = ["A girl’s name",
"A boy’s name",
"Cities",
"Countries",
"Animals",
"Plants",
"Cartoon Characters",
"Brands",
"Related to the beach",
"Related to cars",
"Things that are sticky",
"Related to Ice cream",
"Related to water",
"Halloween costumes",
"Places to go on a date",
"Nicknames",
"Job titles",
"College majors",
"Historical figures",
"Celebrities",
"Good gifts",
"Things on a map",
"Things in an office",
"Things people are afraid of",
"Apps",
"Movie titles",
"Book titles",
"Related to Music",
"Song title",
"Drinks",
"Hobbies",
"Related to space",
"Sweet things",
"Ways to get from here to there",
"Things around the house",
"Sports teams",
"Related to sports",
"Colors",
"Item within eyesight",
"Things that can be blue",
"Related to the body",
"Items you would find at Walmart",
"Foods",
"Having to do with cooking",
"Something people can do on a weekend",
"TV show title",
"Things related to the Holidays",
"Related to Games",
"Fictional Heroes or Villains",
"Related to Fairytales/Myths",
"Related to Nature",
"Related to airports",
"Related to Clothing",
"Related to art",
"Related to Weather",
"Related to Spring",
"Related to Summer",
"Related to Fall",
"Related to Winter"]

blue_card_len = len(blue_card_rules)

red_card_rules = ["2 words",
"1 word",
"1 syllable",
"2 syllables",
"3 syllables",
"4 or more syllables",
"2 words (2 syllables each)",
"3 or 4 letters",
"5 letters",
"6 letters",
"7 letters",
"8 or 9 letters",
"10+ letters",
"Even letters",
"Odd letters",
"2 words (same number of letters)",
"Even vowels",
"Odd vowels",
"Even consonants",
"Odd consonants",
"Same number of vowels & consonants",
"Double consonant",
"Double vowel",
"Repeats a consonant and a vowel",
"Less than 4 consonants",
"One vowel"]
red_card_len = len(red_card_rules)

yellow_card_rules = ["Ends with S",
"Ends with R",
"Ends with E",
"Ends with D",
"Ends with N",
"Doesn’t include A",
"Doesn’t include E",
"Doesn’t include I",
"Doesn’t include O",
"Doesn’t include U",
"Doesn’t include P",
"Doesn’t include R",
"Doesn’t include S",
"Doesn’t include T",
"Doesn’t include L",
"Doesn’t include N",
"Doesn’t include H",
"Starts with S",
"Starts with T",
"Starts with A",
"Starts with C",
"Starts with H",
"Starts with W",
"Includes 'PH'",
"Includes 'CH'",
"Includes 'TH'",
"Includes 'SH'",
"Includes 'OU'",
"Includes 'QU'",
"Has a K",
"Has an L",
"Has a J",
"Has a V",
"Has an F",
"Has an I"]
yellow_card_len = len(yellow_card_rules)

used_blue = {}
used_red = {}
used_yellow = {}

def draw_cards(used_blue, used_red, used_yellow):
    if len(used_blue.keys()) == blue_card_len:
        used_blue.clear()

    blue_card = random.randint(0, blue_card_len - 1)
    while blue_card in used_blue:
        blue_card = random.randint(0, blue_card_len - 1)

    if len(used_red.keys()) == red_card_len:
        used_red.clear()

    red_card = random.randint(0, red_card_len - 1)
    while red_card in used_red:
        red_card = random.randint(0, red_card_len - 1)

    if len(used_yellow.keys()) == yellow_card_len:
        used_yellow.clear()

    yellow_card = random.randint(0, yellow_card_len - 1)
    while yellow_card in used_yellow:
        yellow_card = random.randint(0, yellow_card_len - 1) 

    used_blue[blue_card] = 1
    used_red[red_card] = 1
    used_yellow[yellow_card] = 1

    return blue_card, red_card, yellow_card

if __name__ == '__main__':
    blue_card_column = [
        sg.Column([
            [sg.Text("Category Rule", font= ("Georgia",24))], 
            [sg.Text(text= '', size = (9,5), key= "-BLUE-", justification='center', background_color = 'cyan', font= ("Georgia", 54))]
        ])
    ]
    red_card_column = [
        sg.Column([
            [sg.Text("Syntax Rule" , font= ("Georgia",24))],
            [sg.Text(text= '', size = (9,5), key= "-RED-", justification='center', background_color = 'pink', font= ("Georgia", 54))]
        ])
    ]
    yellow_card_column = [
        sg.Column([
            [sg.Text("Letter Rule", font= ("Georgia",24))],
            [sg.Text(text= '', size = (9,5), key= "-YELLOW-", justification='center', background_color = 'yellow', font= ("Georgia", 54))]
            ])
    ]
    layout = [
        [
        sg.Pane(blue_card_column, background_color = 'cyan'),
        sg.VSeperator(),
        sg.Pane(red_card_column, background_color = 'red'),
        sg.VSeperator(),
        sg.Pane(yellow_card_column, background_color = 'yellow')
        ],
        [sg.Button("Draw"), sg.Button("Quit")]
    ]
    window = sg.Window("Quicktionary", layout)

    while True:
        event, values = window.read()
        if event == sg. WIN_CLOSED or event == "Quit":
            break
        elif event == "Draw":
            blue_card, red_card, yellow_card = draw_cards(used_blue, used_red, used_yellow)
            window["-BLUE-"].update(blue_card_rules[blue_card])
            window["-RED-"].update(red_card_rules[red_card])
            window["-YELLOW-"].update(yellow_card_rules[yellow_card])
    window.close()