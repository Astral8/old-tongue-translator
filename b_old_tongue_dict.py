from word import Word

b_dictionary = {}

baby = Word("baby", "bopo", "noun")
b_dictionary[baby.__str__()] = baby

back = Word("back", "rakh", "noun")
back.add_second_type("adjective")
back.add_third_type("adverb")
b_dictionary[back.__str__()] = back

bad = Word("bad", "begoud", "adjective")
b_dictionary[bad.__str__()] = bad

bag = Word("bag", "sich", "noun")
b_dictionary[bag.__str__()] = bag

balance = Word("balance", "rieht", "noun")
b_dictionary[balance.__str__()] = balance

ball = Word("ball", "dhub", "noun")
b_dictionary[ball.__str__()] = ball

band = Word("band", "samid", "verb")
band.alt_ot_word("shen", "noun")
b_dictionary[band.__str__()] = band

brotherhood = Word("brotherhood", "shen", "noun")
b_dictionary[brotherhood.__str__()] = brotherhood
# band/brotherhood/group (n.) – shen


# Band of the Red Hand (n.) – Shen an Calhar

banner = Word("banner", "con", "noun")
b_dictionary[banner.__str__()] = banner
# banner, small (n.) – con

bar = Word("bar", "vadin", "noun")
b_dictionary[bar.__str__()] = bar
barrier = Word("barrier", "vadin", "noun")
b_dictionary[barrier.__str__()] = barrier
# bar/barrier (n.) — vadin

base = Word("base", "nupar", "noun", "as in bottom or supprt")
b_dictionary[base.__str__()] = base

basin = Word("basin", "dal", "noun")
b_dictionary[basin.__str__()] = basin

basket = Word("basket", "vhool", "noun")
b_dictionary[basket.__str__()] = basket

bath = Word("bath", "badan", "noun")
b_dictionary[bath.__str__()] = bath

battle = Word("battle", "gai", "noun")
battle.add_second_type("verb")
battle.add_alt_ot_word("dai", "adjective")
b_dictionary[battle.__str__()] = battle
# battle (n., v. & adj.) – dai; gai (n.)


# battle, key (n.) – gai’don (one that will decide the war)

# battle blood (n.) – daishar (meaning, glory)

# battle, brother to/of (n.) – gaidin (Aes Sedai word for Warders)

# Battle Lord (n.) – Dai Shan (title for Lan)

# battle person (n.) – algai

# battle-related (adj.) – dhai

# battle, those sworn to peace in (n.) – gai’shain (Aiel term)

beautiful = Word("beautiful", "n'am", "adjective")
b_dictionary[beautiful.__str__()] = beautiful


# beauty, female ideal of (n.) – boan

# beauty, male ideal of (n.) – botay

because = Word("because", "po", "conjunction")
b_dictionary[because.__str__()] = because

bed = Word("bed", "desu", "noun")
b_dictionary[bed.__str__()] = bed

bee = Word("bee", "souk", "noun")
b_dictionary[bee.__str__()] = bee

beet = Word("beet", "birok", "noun")
b_dictionary[beet.__str__()] = beet

before = Word("before", "ailen", "conjunction")
before.add_second_type("preposition")
before.add_third_type("adjective")
b_dictionary[before.__str__()] = before

# behavior (n.) — soovri NOTE CAN BE SPELLED AS BEHAVIOUR

beldam = Word("beldam", "drova", "noun")
beldam.add_alt_ot_word("drovja", "possessive")
b_dictionary[beldam.__str__()] = beldam

belief = Word("belief", "astai", "noun")
b_dictionary[belief.__str__()] = belief

bell = Word("bell", "kloye", "noun")
b_dictionary[bell.__str__()] = bell

# belonging to (prep.) — d (implied ownership or inferior position)

beloved = Word("beloved", "lan", "adjective")
b_dictionary[beloved.__str__()] = beloved

bent = Word("bent", "slagh", "adjective")
b_dictionary[bent.__str__()] = bent

berry = Word("berry", "rimbai", "noun")
b_dictionary[berry.__str__()] = berry

betray = Word("betray", "ishar", "verb")
b_dictionary[betray.__str__()] = betray

betrayal = Word("betrayal", "ishavid", "noun")
b_dictionary[betrayal.__str__()] = betrayal

betrayer = Word("betrayer", "isham", "noun")
b_dictionary[betrayer.__str__()] = betrayer

# betrayer of hope (n.) – ishamael (name of a Forsaken)

between = Word("between", "scrup", "adverb")
between.add_second_type("preposition")
b_dictionary[between.__str__()] = between

bird = Word("bird", "kriko", "noun")
b_dictionary[bird.__str__()] = bird

birth = Word("birth", "syndon", "noun")
b_dictionary[birth.__str__()] = birth

bit = Word("bit", "roedane", "verb")
b_dictionary[bit.__str__()] = bit

bite = Word("bite", "roedna", "verb")
b_dictionary[bite.__str__()] = bite

bitter = Word("bitter", "chaki", "adjective")
b_dictionary[bitter.__str__()] = bitter

black = Word("black", "doon", "noun")
black.add_second_type("adjective")
b_dictionary[black.__str__()] = black

# Black Eyes (n.) – Seia Doon (Aiel warrior society)

# Black Wind (n.) – Machin Shin (literally, ‘journey of destruction’)

# blade (n.) – mandarb (name of Lan’s stallion); manshima

# blade, related to (adj.) – man

# blade, small (n.) – nai (knife-like)

blinder = Word("blinder", "samma", "noun")
b_dictionary[blinder.__str__()] = blinder

# blood/bloodline (meaning descent or heritage) (n.) – shar (pl. is shari)

# blood of battles (n.) – daishar (meaning, glory)

blow = Word("blow", "khoop", "verb")
b_dictionary[blow.__str__()] = blow

# blue (n. & adj.) – ascar; –era (suffix)

# blue-eye (n.) – seiera (a flower in Baerlon; name of Min’s mare)

# boar-horse (n.) – s’redit (used by Seanchan)

# boar-like animal (n.) – capar (from Aiel Waste)

board = Word("board", "kontar", "noun")
b_dictionary[board.__str__()] = board

boat = Word("boat", "nausig", "noun")
b_dictionary[boat.__str__()] = boat

body = Word("body", "chinnar", "noun")
b_dictionary[body.__str__()] = body

boiling = Word("boiling", "merwon", "adjective")
b_dictionary[boiling.__str__()] = boiling


# bollocks (interjection) – tsag (obsenity uttered by Sammael)

bone = Word("bone", "khadi", "noun")
b_dictionary[bone.__str__()] = bone

book = Word("book", "blagh", "noun")
b_dictionary[book.__str__()] = book

# boot(s) (n.) – poulam

bottle = Word("bottle", "tsatsi", "noun")
b_dictionary[bottle.__str__()] = bottle

bowl = Word("bowl", "dal", "noun")
b_dictionary[bowl.__str__()] = bowl

box = Word("box", "bah", "noun")
b_dictionary[box.__str__()] = box

boxes = Word("boxes", "baha", "noun")
b_dictionary[boxes.__str__()] = boxes

boy = Word("boy", "yuntar", "noun")
b_dictionary[boy.__str__()] = boy

brain = Word("brain", "sysyn", "noun")
b_dictionary[brain.__str__()] = brain

brake = Word("brake", "tsinas", "noun")
brake.add_second_type("verb")
b_dictionary[brake.__str__()] = brake

branch = Word("branch", "warat", "noun")
b_dictionary[branch.__str__()] = branch

brass = Word("brass", "farhota", "noun")
b_dictionary[brass.__str__()] = brass

bread = Word("bread", "bachri", "noun")
b_dictionary[bread.__str__()] = bread

breath = Word("breath", "chati", "noun")
b_dictionary[breath.__str__()] = breath

brick = Word("brick", "yedcost", "noun")
b_dictionary[brick.__str__()] = brick

bridge = Word("bridge", "spotsu", "noun")
b_dictionary[bridge.__str__()] = bridge

bright = Word("bright", "sheikar", "adjective")
b_dictionary[bright.__str__()] = bright

# bringers of (n.) — sheen

# Bringers of Annihilation (n.) – Bhan’sheen (a Trolloc band)

broken = Word("broken", "yugol", "adjective")

# brother (n.) – alantin; din (singular and plural)

# Brothers of the Eagle (n.) – Far Aldazar Din (an Aiel warrior society)

# brother to/of battle (n.) – gaidin (Aes Sedai word for Warders)

# Brotherhood (n.) – Ko’bal (a Trolloc band; literally, circle of one)

# brotherhood/band/group (n.) — shen

# Brotherless, the (n.) – Mera’din (used by Aiel)

brown = Word("brown", "deebo", "noun")
brown.add_second_type("adjective")
b_dictionary[brown.__str__()] = brown

brush = Word("brush", "jhabal", "noun")
b_dictionary[brush.__str__()] = brush

# Brutes of Venom (n.) – Ghar’ghael (a Trolloc band)

bucket = Word("bucket", "hutsah", "noun")
b_dictionary[bucket.__str__()] = bucket

# builders (n.) – wansho (Shienaran term for the Ogier)

building = Word("building", "bhardo", "noun")
b_dictionary[building.__str__()] = building

# building material (n.) – cueran (from Age of Legends)

bulb = Word("bulb", "tumerest", "noun")
b_dictionary[bulb.__str__()] = bulb

burn = Word("burn", "jalat", "noun")
burn.add_second_type("verb")
b_dictionary[burn.__str__()] = burn

burst = Word("burst", "doozhi", "verb")
b_dictionary[burst.__str__()] = burst

business = Word("business", "pantae", "noun")
b_dictionary[business.__str__()] = business

but = Word("but", "no","conjunction")
b_dictionary[but.__str__()] = but

butter = Word("butter", "maspil", "noun")
b_dictionary[butter.__str__()] = butter

button = Word("button", "sobel", "noun")
b_dictionary[button.__str__()] = button

by = Word("by", "dyu", "adverb")
by.add_second_type("preposition")
b_dictionary[by.__str__()] = by


def check_b_dict(word):
    if word in b_dictionary:
        return b_dictionary.get(word)
