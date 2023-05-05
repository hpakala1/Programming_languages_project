<h2>Brief Detail of the Project Created</h2>

Using the Python **NLTK** module, this code creates a context-free grammar for natural language processing. The grammar is written in Backus-Naur form, where terminals are placed in quotes and nonterminals are represented by uppercase letters.

The parts of speech, a few prepositions, and certain pronouns are all defined in the grammar, along with the rules for constructing sentences, phrases, and words. A noun phrase and a verb phrase, for instance, can be combined to make a sentence according to the rule "S -> NP VP". A determiner is followed by a noun, a pronoun, or a few other possible words to make up the noun phrase. The verb phrase may also include a noun phrase, an adjective, an adverb, or a prepositional phrase after the verb.

A list of nouns, verbs, and other speech components are also provided in the grammar, and these may be used to create sentences that follow the grammar's rules. As an illustration, the noun "dog" may be used to create noun phrases such as "the dog" or "my dog" and the verb "walked" can be used to create verb phrases such as "walked the dog" or "is walking."

Once the given sentence conforms to the program's grammar, the program begins translating the sentence's English words into Spanish. If the particular word is found in the Python dictionary "translation_rules," it is translated into Spanish and replaces the respective word in the sentence; otherwise, it simply ignores the word and keeps it the same. 

**NOTE:** If the input sentence either doesn't satisfy the program's grammar or the words in it doesn't match with any words in the grammar it gives out an error and crashes the program.

<h2>Interesting Things From The Code</h2>

A context-free grammar (CFG) is used by the **translate_sentence** method in my project code to analyze an English sentence and swap out English terms for their Spanish counterparts. The function constructs a parser using the nltk.ChartParser class after first loading a CFG from a textual representation (my_grammar).

The input sentence is then tokenized using **nltk.word_tokenize** into individual words. The function then parses the sentence in accordance with the CFG using the parser. The outcome is a collection of parse trees that depict each and every method the input text could be parsed in accordance with the CFG.

The function then outputs the translated Spanish text with a period ('.') at the end and the first letter capitalized.

These below are a few intriguing aspects of **translate_sentence** method:

1. It parses the input text using a CFG, which enables a more flexible and reliable method of language translation than using straightforward pattern matching or regular expressions.

2. The translation process may be easily customized and altered since the translation rules are defined as a dictionary.

3. By changing the translation rules and CFG, it would be simple to change the function's assumption that the input sentence is in English and that Spanish is the desired output language.

<h2>Steps To Run Program</h2>

1. Open a terminal in your pc. (**Note:** Windows users use **gitbash** for better accessibilty.)

2. Clone the project in your local.

    ```
    git clone https://github.com/hpakala1/Programming_languages_project.git
    ```

3. Navigate to the directory where the cloned repository resides.

    ```
    cd <Path in your local to the repository>
    ```

4. Navigate inside the cloned repository.

    ```
    cd Programming_languages_project
    ```

5. Create a python virtual environment in this repository.

    ```
    python3 -m venv venv
    ```

6. Activate the python virtual environment.

    ```
    source venv/bin/activate
    ```

7. Install **nltk** library.

    ```
    pip install nltk
    ```

8. Run the python file by providing the desired english sentence as command line argument.

    ```
    python EnglishToSpanishTranslator.py "The food tastes delicious"
    ```

    **Note:**Don't use period at the end of the input sentence as the given grammar does not identify characters other than english alphabets.

9. After completion of running the program. Deactivate the virtual environment.

    ```
    deactivate
    ```

<h2>Example Sentences That Satisfy The Grammar</h2>

1. The country has a lot of natural beauty.

2. The food tastes delicious.

3. They watch a movie at the cinema.

4. The dog barks at the cat.

5. She is a beauty with friends.

6. They were running towards the water.

7. The wind blows through the trees.

8. We are watching a movie in the cinema.

9.He walked along the quiet street.

10.The teacher gave us homework.

11. He is dancing in the room.

12. Cat can climb the wall.

13. Dog walked in the park.

14. Apple trees are on the street.

15. She likes the smell of a flower.

16. Student takes food to lunch.

17. The actor likes dancing.

<h2>Important Note On Possible Errors</h2>

1. If the given sentence does not satisfy the given grammar the below error will be provided in the terminal and the program crashes.

![Unidentified grammar error](./Yaw_Axis_Corrected.svg.png)

2. If the given sentence contains a word/phrase that is not present in the given grammar the below error will be provided in the terminal and the program crashes.

![Word not found error](./Yaw_Axis_Corrected.svg.png)

