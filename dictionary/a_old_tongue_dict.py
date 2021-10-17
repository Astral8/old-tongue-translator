from word import Word

a_dictionary = {}

a = Word("a", "o", "adjective")
a_dictionary[a.__str__()] = a
able = Word("able", "folyt", "adjective")
a_dictionary[able.__str__()] = able

about = Word("about", "tiel", "adverb")
about.add_second_type("preposition")
a_dictionary[about.__str__()] = about

account = Word("account", "norvenne", "noun")
a_dictionary[account.__str__()] = account
acid = Word("acid", "ghar", "noun")
a_dictionary[acid.__str__()] = acid
across = Word("across", "gaen", "preposition")
a_dictionary[across.__str__()] = across
act = Word("act", "bunok", "verb")
a_dictionary[act.__str__()] = act
addition = Word("addition", "einto", "noun")
a_dictionary[addition.__str__()] = addition
adjustment = Word("adjustment", "faerstin", "noun")
a_dictionary[adjustment.__str__()] = adjustment

after = Word("after", "widon", "adjective")
after.add_second_type("preposition")
after.add_third_type("conjunctive")
a_dictionary[after.__str__()] = after

again = Word("again", "nye", "adverb")
a_dictionary[again.__str__()] = again
against = Word("against", "bat", "preposition")
a_dictionary[against.__str__()] = against
agony = Word("agony", "dha", "noun")
a_dictionary[agony.__str__()] = agony
agreement = Word("agreement", "o'vin", "noun")
a_dictionary[agreement.__str__()] = agreement
air = Word("air", "raia", "noun")
a_dictionary[air.__str__()] = air

all_word = Word("all", "aes", "noun")
a_dictionary[all_word.__str__()] = all_word
# Uses all_word to represent all

all_powerful = Word("all-powerful", "ghraem", "noun")
a_dictionary[all_powerful.__str__()] = all_powerful
# Need to look at Phrase implementation for The All Powerful

almost = Word("almost", "sast", "adverb")
a_dictionary[almost.__str__()] = almost
always = Word("always", "hei", "adverb")
a_dictionary[always.__str__()] = always
am = Word("am", "misain", "verb", "insistent;emphatic")
a_dictionary[am.__str__()] = am

am_not = Word("am not", "isainde", "verb", "insistent;emphatic")
# Note not sure for this word, and is verb negative. Might be a phrase
# NOT IN DICTIONARY

among = Word("among", "tom", "preposition")
a_dictionary[among.__str__()] = among
amount = Word("amount", "abakran", "noun")
a_dictionary[amount.__str__()] = amount
amusement = Word("amusement", "seel", "noun")
a_dictionary[amusement.__str__()] = amusement

and_word = Word("and", "e", "conjunction")
a_dictionary[and_word.__str__()] = and_word
# For and

angle = Word("angle", "lato", "noun")
a_dictionary[angle.__str__()] = angle
angry = Word("angry", "cavastu", "adjective")
a_dictionary[angry.__str__()] = angry
anguish = Word("anguish", "dha", "noun")
a_dictionary[anguish.__str__()] = anguish
animal = Word("animal", "ubunto", "noun")
a_dictionary[animal.__str__()] = animal
annihilation = Word("annihilation", "bhan", "noun")
a_dictionary[annihilation.__str__()] = annihilation

anniversary = Word("anniversary", "shanna'har", "noun", "Saldean word for Marriage/Celebration/Anniversary")
a_dictionary[anniversary.__str__()] = anniversary
# Need to add words for Marriage and Celebration and then initializae them as Synonyms later


another = Word("another", "sovya", "adjective")
a_dictionary[another.__str__()] = another
answer = Word("answer", "conagh", "noun")
a_dictionary[answer.__str__()] = answer
ant = Word("ant", "pizar", "noun")
a_dictionary[ant.__str__()] = ant
anxiety = Word("anxiety", "cuande", "noun", "stress-induced condition; can be experienced as chest pains")
a_dictionary[anxiety.__str__()] = anxiety

any_word = Word("any", "shak", "pronoun")
any_word.add_second_type("adjective")
any_word.add_third_type("adverb")
a_dictionary[any_word.__str__()] = any_word
# Uses any_word for any

any_other = Word("any other", "sovya", "adjective")
# Might need to be a phrase
# NOT IN DICTIONARY

apparatus = Word("apparatus", "jobei", "noun")
a_dictionary[apparatus.__str__()] = apparatus
apple = Word("apple", "melimo", "noun")
a_dictionary[apple.__str__()] = apple
approval = Word("approval", "modan", "noun")
a_dictionary[approval.__str__()] = approval
arch = Word("arch", "onadh", "noun")
a_dictionary[arch.__str__()] = arch
argument = Word("argument", "zheshi", "noun")
a_dictionary[argument.__str__()] = argument
arm = Word("arm", "bazam", "noun")
a_dictionary[arm.__str__()] = arm
army = Word("army", "dumki", "noun")
a_dictionary[army.__str__()] = army
arrow = Word("arrow", "vasen", "noun")
a_dictionary[arrow.__str__()] = arrow

# PHRASE: arrow of time (n.) – vasen’cierto

art = Word("art", "beatha", "noun")
a_dictionary[art.__str__()] = art

as_word = Word("as", "sene", "adverb")
a_dictionary[as_word.__str__()] = as_word
# For as

ask = Word("ask", "devor", "verb")
a_dictionary[ask.__str__()] = ask
asked = Word("asked", "devoriska", "relative pronoun")
a_dictionary[asked.__str__()] = asked
# asked, what was (rel. pron.) – devoriska

at = Word("at", "thaz", "preposition")
a_dictionary[at.__str__()] = at
attack = Word("attack", "baijan", "noun")
a_dictionary[attack.__str__()] = attack

attempt = Word("attempt", "gomaen", "noun")
attempt.add_second_type("verb")
a_dictionary[attempt.__str__()] = attempt

attention = Word("attention", "sahlan", "noun")
a_dictionary[attention.__str__()] = attention
attraction = Word("attraction", "amotath", "noun")
a_dictionary[attraction.__str__()] = attraction
aunt = Word("aunt", "shaendi", "noun")
a_dictionary[aunt.__str__()] = aunt
authority = Word("authority", "rahtsi", "noun")
a_dictionary[authority.__str__()] = authority
automatic = Word("automatic", "n'baid", "adjective")
a_dictionary[automatic.__str__()] = automatic
awake = Word("awake", "aagret", "adjective")
a_dictionary[awake.__str__()] = awake


def check_a_dict(word):
    if word in a_dictionary:
        a_word = a_dictionary.get(word)
        return a_word.ot_word
    else:
        for words in a_dictionary:
            if word == words + "s":
                a_word = a_dictionary.get(words)
                return a_word.ot_word
