from random import choice



def num_translate_adv(letter):
    numbers_dict = {
        'one' : 'один',
        'two' : 'два',
        'three' : 'три',
        'four' : 'четыре',
        'five' : 'пять',
        'six' : 'шесть',
        'seven' : 'семь',
        'eight' : 'восемь',
        'nine' : 'девять',
        'ten' : 'десять',
        'One': 'Один',
        'Two': 'Два',
        'Three': 'Три',
        'Four': 'Четыре',
        'Five': 'Пять',
        'Six': 'Шесть',
        'Seven': 'Семь',
        'Eight': 'Восемь',
        'Nine': 'Девять',
        'Ten': 'Десять'}
    print(numbers_dict.get(letter))


def thesaurus(*names_list):
    first_letters_dict = dict()
    for name in names_list:
        first_letter = name[0].capitalize()
        if first_letter not in first_letters_dict:
            first_letters_dict[first_letter] = []
            first_letters_dict[first_letter].append(name)


    return first_letters_dict


def get_jokes(times, flag = False):
    """
    returns randomly generated jokes

    arguments:
    times -- amount of randomly generated jokes
    flag -- flag in charge of repeating words in jokes (default - False)
    """
    temp_noun_index = 0
    temp_adverbs_index = 0
    temp_adjectives_index = 0
    i = 0
    joke = []
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    while i < times:
        temp_joke = ''
        if flag == False:
            temp_joke += choice(nouns)
            temp_joke += ' ' + choice(adverbs)
            temp_joke += ' ' + choice(adjectives)



        if flag == True:
            if times >= 5:
                return 'Error: unable to make more than 5 jokes with flag turned on.'
            else:
                temp_noun_index = nouns.index(choice(nouns))
                temp_adverbs_index = adverbs.index(choice(adverbs))
                temp_adjectives_index = adjectives.index(choice(adjectives))
                temp_joke += nouns[temp_noun_index]
                temp_joke += ' ' + adverbs[temp_adverbs_index]
                temp_joke += ' ' + adjectives[temp_adjectives_index]

                adverbs.remove(adverbs[temp_adverbs_index])
                nouns.remove(nouns[temp_noun_index])
                adjectives.remove(adjectives[temp_adjectives_index])


        joke.append(temp_joke)



        i += 1

    return joke







num_translate_adv('One')
num_translate_adv('three')
num_translate_adv('f')


dict_names = thesaurus('Антон', 'Урмек', 'Неред')
print(dict_names)


print(get_jokes(2))
print(get_jokes(3, flag=True))
