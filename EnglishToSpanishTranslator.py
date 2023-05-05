import sys
import nltk
from nltk import word_tokenize
from nltk.parse.generate import generate

my_grammar="""
S -> NP VP 
NP -> Det N | Pronoun | N V | V | V Pronoun | Det Nominal | PP |N V VP | N | Pronoun Det N | N NP 
Pronoun -> Det N
Nominal -> N | Adjective Nominal | Nominal PP | Adverb VP | N PP | V NP | N VP | N NP 
PP -> P NP
VP -> V NP | V Adjective | Adverb | V | V VP | Adverb VP | Adjective | V Adverb | V PP | V Adverb PP  
Det -> 'the' | 'a' | 'an' | 'my' | 'your' | 'his' | 'her' | 'its' | 'our' | 'their'
P ->| 'afore' | 'about' | 'above' | 'absent' | 'across' | 'after' | 'against' | 'along' | 'alongside' | 'amid' | 'amidst' | 'among' | 'amongst' | 'an' | 'anent' | 'apropos' | 'apud' | 'around' | 'as' | 'aside' | 'astride' | 'at' | 'athwart' | 'atop' | 'barring' | 'before' | 'behind' | 'below' | 'beneath' | 'beside' | 'besides' | 'between' | 'beyond' | 'but' | 'by' | 'circa' | 'come' | 'despite' | 'down' | 'during' | 'except' | 'for' | 'from' | 'given' | 'in' | 'including' | 'inside' | 'into' | 'lest' | 'like' | 'mid' | 'midst' | 'minus' | 'modulo' | 'near' | 'next' | 'notwithstanding' | 'of' | 'off' | 'on' | 'onto' | 'opposite' | 'out' | 'outen' | 'outside' | 'over' | 'pace' | 'past' | 'per' | 'plus' | 'pro' | 'qua' | 'regarding' | 'round' | 'sans' | 'save' | 'since' | 'than' | 'through' | 'throughout' | 'thru' | 'thruout' | 'till' | 'times' | 'to' | 'toward' | 'towards' | 'under' | 'underneath' | 'unlike' | 'until' | 'unto' | 'up' | 'upon' | 'versus' | 'via' | 'vice' | 'with' | 'within' | 'without' | 'worth' |
Pronoun -> 'i' | 'you' | 'he' | 'she' | 'it' | 'book' | 'we' | 'they' | 'me' | 'you' | 'him' | 'her' | 'it' | 'us' | 'them' |  'mine' | 'yours' | 'his' | 'hers' | 'its' | 'ours' | 'theirs' | 'myself' | 'yourself' | 'himself' | 'herself' | 'itself' | 'ourselves' | 'themselves' | 'this' | 'that' | 'these' | 'those' | 'anything' | 'someone' | 'something' | 'nobody' | 'nothing' | 'each' | 'every' | 'either' | 'neither' | 'one' | 'another' | 'all' | 'some' | 'any' | 'none' | 'few' | 'many' | 'several' | 'both' | 'others' | 'several' | 'few' | 'many' | 'most' | 'several'
N -> 'park' | 'wall' | 'room' | 'assignment' | 'homework' | 'street' | 'trees' | 'dog' | 'cat' | 'beauty' |'bird' | 'apple' |'friends' | 'table' |'fish' | 'horse' | 'cow' | 'pig' | 'chicken' | 'duck' | 'goose' | 'sheep' | 'rabbit' | 'fox' | 'bear' | 'lion' | 'tiger' | 'elephant' | 'monkey' | 'snake' | 'lizard' | 'frog' | 'bug' | 'butterfly' | 'flower' | 'tree' | 'grass' | 'rock' | 'water' | 'fire' | 'earth' | 'sky' | 'sun' | 'moon' | 'star' | 'cloud' | 'wind' | 'rain' | 'snow' | 'ice' | 'basketball' | 'American' | 'Indian' | 'football' | 'teacher' | 'professor' | 'racer' | 'billiken' | 'actor' | 'student' | 'breakfast' | 'lunch' | 'dinner' | 'party' | 'food' | 'movie' | 'cinema' | 'country'
V -> 'gave' |'walked' |'watching' | 'blows' | 'barks' | 'running' | 'is' | 'are' | 'was' | 'were' | 'eats' |'in' | 'on' | 'at' | 'to' | 'from' | 'with' | 'by' | 'for' | 'of' | 'that' | 'this' | 'these' | 'those' | 'have' | 'has' | 'had' | 'do' | 'does' | 'did' | 'will' | 'would' | 'should' | 'can' | 'could' | 'may' | 'might' | 'must' | 'need' | 'want' | 'like' | 'love' | 'hate' | 'eat' | 'drink' | 'play' | 'plays'| 'run' | 'walk' | 'fly' | 'swim' | 'crawl' | 'jump' | 'sleep' | 'wake' | 'see' | 'hear' | 'smell' | 'taste' | 'touch' | 'feel' | 'play' | 'know' | 'who' | 'take' | 'takes' | 'likes' | 'dance' | 'dancing' | 'like' | 'love' | 'hate' | 'have' | 'need' | 'want' | 'eat' | 'drink' | 'cook' | 'read' | 'write' | 'talk' | 'listen' | 'tastes' | 'touch' | 'feel' | 'sleep' | 'wake' | 'dream' | 'think' | 'remember' | 'forget' | 'understand' | 'believe' | 'watch' | 'play' | 'work' | 'study' | 'learn' | 'teach' | 'travel' | 'meet' | 'see' | 'hear' | 'smell' | 'taste' | 'know' | 'hope' | 'wish' | 'pray' | 'cry' | 'laugh' | 'smile' | 'sing' | 'dance' | 'fly' | 'swim' | 'run' | 'walk' | 'climb' | 'jump' | 'skip' | 'play' | 'win' | 'lose' | 'try' | 'start' | 'stop' | 'continue' | 'finish' | 'begin' | 'end' | 'improve' | 'grow' | 'change' | 'develop' | 'create' | 'make' | 'build' | 'design' | 'draw' | 'paint' | 'take' | 'give' | 'send' | 'receive' | 'buy' | 'sell' | 'pay' | 'cost' | 'own' | 'use' | 'wear' | 'clean' | 'fix' | 'repair' | 'throw' | 'catch' | 'keep' | 'save' | 'lose' | 'find' | 'search' | 'look' | 'see' | 'show' | 'tell' | 'ask' | 'answer' | 'explain' | 'describe' | 'imagine' | 'think' | 'belong' | 'include' | 'believe' | 'consist' | 'depend' | 'matter' | 'seem' | 'sound' | 'occur' | 'happen' | 'live' | 'die' | 'kill' | 'survive' | 'help' | 'support' | 'care' | 'protect' | 'save' | 'serve' | 'follow' | 'lead' | 'direct' | 'guide' | 'manage' | 'organize' | 'plan' | 'decide' | 'vote' | 'agree' | 'disagree' | 'argue' | 'discuss' | 'negotiate' | 'compromise' | 'win' | 'lose' | 'succeed' | 'fail' | 'celebrate' | 'enjoy' | 'relax' | 'rest' | 'meditate' | 'pray' | 'think' | 'worry' | 'stress' | 'fear' | 'hope' | 'believe' | 'doubt' | 'accept' | 'reject' | 'forgive' | 'blame' | 'apologize' | 'thank' | 'welcome' | 'greet' | 'introduce' | 'visit' | 'host' | 'attend' | 'invite' | 'offer' | 'promise' | 'swear' | 'threaten' | 'insult' | 'compliment' | 'flirt' | 'date' | 'go'
Adjective -> 'quiet' | 'hot' | 'cold' | 'natural' | 'big' | 'small' | 'good' | 'bad' | 'happy' | 'sad' | 'angry' | 'afraid' | 'tired' | 'hungry' | 'thirsty' | 'beautiful' | 'ugly' | 'old' | 'young' | 'delicious' | 'new' | 'tall' | 'slow' | 'fast' | 'easy' | 'difficult' | 'expensive' | 'cheap' | 'hard' | 'soft' | 'long' | 'intelligent'
Adverb -> 'and' | 'too' | 'enough' | 'such' | 'lot' |'very' | 'quite' | 'also' | 'only' | 'just' | 'even' | 'still' | 'yet' | 'already' | 'never' | 'sometimes' | 'always' | 'usually' | 'often' | 'rarely' | 'hardly' | 'almost' | 'nearly' | 'finally' | 'actually' | 'simply' | 'totally' | 'completely' | 'mostly' | 'obviously' | 'clearly' | 'apparently' | 'likely' | 'perhaps' | 'possibly' | 'certainly' | 'definitely' | 'probably' | 'after'
"""

# Define the translation rules for English to Spanish
translation_rules = {
    'watching': 'viendo',
    'student': 'alumna',
    'actor':'actriz',
    'park':'parque',
    'trees': 'árboles',
    'blows':'golpes',
    'a': 'un',
    'book':'libro',
    'an': 'un',
    'the': 'el',
    'and': 'y',
    'is': 'es',
    'are': 'son',
    'was': 'fue',
    'were': 'eran',
    'in': 'en',
    'on': 'en',
    'at': 'a',
    'to': 'a',
    'from': 'de',
    'with': 'con',
    'by': 'por',
    'for': 'para',
    'of': 'de',
    'that': 'ese',
    'this': 'este',
    'these': 'estos',
    'those': 'aquellos',
    'my': 'mi',
    'your': 'tu',
    'his': 'su',
    'gave':'dar',
    'homework':'tarea',
    'assignment':'signación',
    'her': 'su',
    'its': 'su',
    'our': 'nuestro',
    'their': 'su',
    'I': 'yo',
    'you': 'tu',
    'he': 'el',
    'she': 'ella',
    'it': 'eso',
    'we': 'nosotros',
    'they': 'ellos',
    'dog': 'perro',
    'cat': 'gato',
    'bird': 'ave',
    'fish': 'pez',
    'horse': 'caballo',
    'cow': 'vaca',
    'pig': 'cerdo',
    'chicken': 'pollo',
    'duck': 'pato',
    'goose': 'ganso',
    'sheep': 'oveja',
    'rabbit': 'conejo',
    'fox': 'zorro',
    'bear': 'oso',
    'lion': 'leon',
    'tiger': 'tigre',
    'elephant': 'elefante',
    'monkey': 'mono',
    'snake': 'serpiente',
    'lizard': 'lagarto',
    'frog': 'rana',
    'bug': 'bicho',
    'butterfly': 'mariposa',
    'flower': 'flor',
    'tree': 'arbol',
    'grass': 'hierba',
    'rock': 'piedra',
    'water': 'agua',
    'fire': 'fuego',
    'earth': 'tierra',
    'sky': 'cielo',
    'sun': 'sol',
    'moon': 'luna',
    'star': 'estrella',
    'cloud': 'nube',
    'wind': 'viento',
    'rain': 'lluvia',
    'snow': 'nieve',
    'ice': 'hielo',
    'hot': 'caliente',
    'cold': 'frio',
    'big': 'grande',
    'small': 'pequeno',
    'good': 'bueno',
    'bad': 'malo',
    'happy': 'feliz',
    'sad': 'triste',
    'angry': 'enojado',
    'afraid': 'asustado',
    'tired': 'cansado',
    'hungry': 'hambriento',
    'thirsty': 'sediento',
    'beautiful': 'hermoso',
    'ugly': 'feo',
    'old': 'viejo',
    'young': 'joven',
    'new': 'nuevo',
    'some': 'algunos',
    'any': 'cualquier',
    'all': 'todos',
    'none': 'ninguno',
    'every': 'cada',
    'each': 'cada uno',
    'most': 'la mayoria de',
    'few': 'pocos',
    'several': 'varios',
    'many': 'muchos',
    'much': 'mucho',
    'more': 'mas',
    'less': 'menos',
    'too': 'demasiado',
    'enough': 'suficiente',
    'such': 'tal',
    'very': 'muy',
    'quite': 'bastante',
    'also': 'tambien',
    'only': 'solo',
    'just': 'justo',
    'even': 'incluso',
    'still': 'todavia',
    'yet': 'todavia',
    'already': 'ya',
    'never': 'nunca',
    'sometimes': 'a veces',
    'always': 'siempre',
    'usually': 'generalmente',
    'often': 'a menudo',
    'rarely': 'rara vez',
    'hardly': 'apenas',
    'almost': 'casi',
    'nearly': 'casi',
    'finally': 'finalmente',
    'actually': 'realmente',
    'simply': 'simplemente',
    'totally': 'totalmente',
    'completely': 'completamente',
    'mostly': 'en su mayoria',
    'obviously': 'obviamente',
    'clearly': 'claramente',
    'apparently': 'aparentemente',
    'likely': 'probablemente',
    'perhaps': 'quizas',
    'possibly': 'posiblemente',
    'certainly': 'ciertamente',
    'definitely': 'definitivamente',
    'probably': 'probablemente',
    'must': 'debe',
    'should': 'deberia',
    'could': 'podria',
    'would': 'seria',
    'might': 'podria',
    'can': 'puede',
    'will': 'va a',
    'shall': 'debera',
    'may': 'puede',
    'must': 'debe',
    'should': 'deberia',
    'cannot': 'puede',
    'will': 'va a',
    'do': 'hacer',
    'make': 'hacer',
    'give': 'dar',
    'walked':'caminó',
    'street':'calle',
    'quiet':'tranquilo',
    'take': 'tomar',
    'find': 'encontrar',
    'see': 'ver',
    'look': 'mirar',
    'watch': 'ver',
    'hear': 'oir',
    'listen': 'escuchar',
    'smell': 'oler',
    'taste': 'gustar',
    'feel': 'sentir',
    'touch': 'tocar',
    'play': 'jugar',
    'work': 'trabajar',
    'study': 'estudiar',
    'learn': 'aprender',
    'teach': 'ensenar',
    'read': 'leer',
    'write': 'escribir',
    'speak': 'hablar',
    'say': 'decir',
    'tell': 'contar',
    'ask': 'preguntar',
    'hello': 'hola',
    'not': 'no',
    'yes':'si',
    'here':'aqui',
    'i':'me',
    'like':'como',
    'tall':'alto',
    'slow':'lento',
    'fast':'rapido',
    'easy':'fácil',
    'difficult':'difícil',
    'expensive':'caro/a',
    'cheap':'barato/a',
    'hard':'duro/a',
    'soft':'suave',
    'long':'largo/a',
    'short':'corto/a',
    'play':'jugar',
    'know':'saber',
    'who':'oms',
    'after':'después',
    'takes':'acepta',
    'likes':'gustos',
    'dance':'baile',
    'dancing':'bailando',
    'party':'fiesta',
    'intelligent':'inteligente',
    'me':'yo',
    'you':'tú',
    'him':'él',
    'her':'ella',
    'it':'ello',
    'us':'nosotros/nosotras',
    'them':'ellos/ellas',
    'mine':'mío/mía',
    'yours':'tuyo/tuya',
    'his':'suyo (de él)',
    'hers':'suyo (de ella)',
    'its':'suyo (de ello)',
    'ours':'nuestro/nuestra',
    'theirs':'suyo (de ellos/ellas)',
    'myself':'yo mismo/a',
    'yourself':'tú mismo/a',
    'himself':'él mismo',
    'herself':'ella misma',
    'itself':'sí mismo',
    'ourselves':'nosotros/as mismos/as',
    'themselves':'ellos/as mismos/as',
    'this':'este/esta/esto',
    'that':'ese/esa/eso',
    'these':'estos/estas',
    'those':'esos/esas',
    'anything':'cualquier cosa',
    'someone':'alguien',
    'something':'algo',
    'nobody':'nadie',
    'nothing':'nada',
    'each':'cada uno/a',
    'every':'cada',
    'either':'cualquiera',
    'neither':'ninguno/a',
    'one':'uno/a',
    'another':'otro/a',
    'all':'todos/as',
    'some':'algunos/as',
    'any':'cualquier',
    'none':'ningún/ninguna',
    'few':'pocos/as',
    'many':'muchos/as',
    'several':'varios/as',
    'both':'ambos/as',
    'others':'otros/as',
    'most':'la mayoría',
    'several':'varios/as',
    'few':'pocos/as',
    'many':'muchos/as',
    'most':'la mayoría',
    'flirt':'coquetear',
    'date':'tener una cita',   
    'invite':'invitar',
    'offer':'ofrecer',
    'like':'gustar',
    'love':'amar',
    'hate':'odiar',
    'have':'tener',
    'need':'necesitar',
    'want':'querer',
    'eat':'comer',
    'drink':'beber',
    'cook':'cocinar',
    'read':'leer',
    'write':'escribir',
    'talk':'hablar',
    'listen':'escuchar',
    'watch':'ver',
    'play':'jugar',
    'work':'trabajar',
    'study':'estudiar',
    'learn':'aprender',
    'teach':'enseñar',
    'travel':'viajar',
    'meet':'conocer',
    'see':'ver',
    'hear':'oir',
    'smell':'oler',
    'taste':'gustar',
    'touch':'tocar',
    'feel':'sentir',
    'sleep':'dormir',
    'wake':'despertar',
    'eats':'come',
    'dream':'soñar',
    'think':'pensar',
    'remember':'recordar',
    'forget':'olvidar',
    'understand':'entender',
    'believe':'creer',
    'know':'saber',
    'hope':'esperar',
    'wish':'desear',
    'pray':'rezar',
    'cry':'llorar',
    'laugh':'reír',
    'smile':'sonreír',
    'sing':'cantar',
    'dance':'bailar',
    'fly':'volar',
    'swim':'nadar',
    'run':'correr',
    'walk':'caminar',
    'climb':'trepar',
    'jump':'saltar',
    'skip':'saltar a la cuerda',
    'win':'ganar',
    'lose':'perder',
    'try':'intentar',
    'start':'empezar',
    'stop':'parar',
    'room':'habitacion',
    'continue':'continuar',
    'finish':'terminar',
    'begin':'comenzar',
    'end':'finalizar',
    'improve':'mejorar',
    'grow':'crecer',
    'change':'cambiar',
    'develop':'desarrollar',
    'create':'crear',
    'wall':'muro',
    'make':'hacer',
    'build':'construir',
    'design':'diseñar',
    'draw':'dibujar',
    'paint':'pintar',
    'take':'tomar',
    'give':'dar',
    'send':'enviar',
    'receive':'recibir',
    'buy':'comprar',
    'sell':'vender',
    'pay':'pagar',
    'cost':'costar',
    'own':'poseer',
    'use':'usar',
    'wear':'usar (ropa)',
    'clean':'limpiar',
    'fix':'arreglar',
    'repair':'reparar',
    'throw':'lanzar',
    'catch':'atrapar',
    'keep':'mantener',
    'save':'guardar',
    'find':'encontrar',
    'search':'buscar',
    'look':'mirar',
    'see':'ver',
    'show':'mostrar',
    'tell':'decir',
    'ask':'preguntar',
    'answer':'responder',
    'explain':'explicar',
    'describe':'describir',
    'imagine':'imaginar',
    'belong':'pertenecer',
    'include':'incluir',
    'consist':'consistir',
    'depend':'depender',
    'matter':'importar',
    'seem':'parecer',
    'sound':'sonar',
    'occur':'ocurrir',
    'happen':'suceder',
    'live':'vivir',
    'die':'morir',
    'kill':'matar',
    'survive':'sobrevivir',
    'help':'ayudar',
    'support':'apoyar',
    'care':'preocuparse',
    'after': 'después de',
    'against': 'contra',
    'along': 'a lo largo de',
    'amid': 'en medio de',
    'amidst': 'en medio de',
    'among': 'entre',
    'around': 'alrededor de',
    'as': 'como',
    'at': 'en',
    'before': 'antes de',
    'behind': 'detrás de',
    'below': 'debajo de',
    'beneath': 'debajo de',
    'beside': 'junto a',
    'between': 'entre',
    'beyond': 'más allá de',
    'but': 'pero',
    'by': 'por',
    'despite': 'a pesar de',
    'down': 'abajo',
    'during': 'durante',
    'except': 'excepto',
    'for': 'para',
    'from': 'de',
    'in': 'en',
    'into': 'en',
    'like': 'como',
    'of': 'de',
    'off': 'desde',
    'on': 'en',
    'onto': 'sobre',
    'out': 'fuera',
    'over': 'sobre',
    'past': 'pasado',
    'since': 'desde',
    'than': 'que',
    'through': 'a través de',
    'to': 'a',
    'toward': 'hacia',
    'under': 'debajo de',
    'until': 'hasta',
    'up': 'arriba',
    'upon': 'sobre',
    'with': 'con',
    'within': 'dentro de',
    'without': 'sin',
    'go':'ir',
    'food':'comida',
    'tastes':'sabores',
    'delicious':'delicioso',
    'movie':'película',
    'cinema':'cine',
    'country':'país',
    'lot':'lote',
    'beauty':'belleza',
    'friends':'amigos',
    'plays':'obras',
    'table': 'mesa',
    'apple': 'manzana',
    'running': 'correr'
}

def translate_sentence(sentence):
    # Load the grammar and create a parser
    grammar = nltk.CFG.fromstring(my_grammar)
    parser = nltk.ChartParser(grammar)

    # Tokenize the input sentence
    tokens = nltk.word_tokenize(sentence)
    print(tokens)
    # Parse the sentence using the grammar
    trees = parser.parse(tokens)
    print(trees)
    # Get the first parse tree
    tree = next(trees)
    print(tree)
    # Traverse the parse tree and replace English words with Spanish words
    def traverse(node):
        if isinstance(node, str):
            if node in translation_rules:
                return translation_rules[node]
            return node
        else:
            parts = [traverse(child) for child in node]
            return ' '.join(parts)

    # Translate the sentence and return the result
    spanish_sentence = ''.join(traverse(tree))
    return spanish_sentence.capitalize() + '.'

# Test the function
if len(sys.argv) != 2:
    print("Please provide an english sentence enclosed in double quotes as command line argument for translation")
    sys.exit(1)
sentence = sys.argv[1]
print("English to Spanish Translator")
print("Original Sentence: ")
print(sentence)
translation = translate_sentence(sentence.lower())
print("Translated Sentence: ")
print(translation)