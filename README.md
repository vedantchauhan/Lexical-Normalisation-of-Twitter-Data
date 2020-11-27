# Lexical-Normalisation-of-Twitter-Data

- Author     : Vedant Chauhan<br>
This file, which describes problem context, program implementation details, procedure to execute program, files used in program, 
output details and references and required material.

- Program context: Lexical normalisation of twitter data. <br>
Twitter messages contain elisions, misspellings, grammatical errors, poses a challenge. In order to make sense of Twitter messages we need to 
convert them into a canonical form, consistent with the dictionary. This is called lexical normalisation of individual tokens. 

- Implementation details and Execution of program:<br>
The program is implemented in python. The program uses edit distance and n-gram to classify tokens. Inorder for this program to work python 
package of edit distance, and n-gram is needed in the system. The path /LexicalNorm/ has Proj1.py file. Run this program in terminal by 
executing the following command:
python Proj1.py

- Files used and Output details:<br>
The files dict.txt (dictionary file), tweets.txt (input tweets file), tokenResults.txt (output tokens with best match) should be in 
the the directory /LexicalNorm/.<br>
The format of these files are:<br>
1. tweets.txt<br>
A list of tweets, one per line. Each tweet is comprised of a space-delimited list of tokens. The tweets have been case-folded, where any 
upper-case (English) characters have been converted to their lower-case equivalent.<br>
2. tokenResults.txt<br>
Token TAB Code TAB Canonical_Form<br>
where <br>
Token: is drawn from the tweet text, <br>
Canonical_Form: is the normalised version of the token,<br>
Code: can take one of three values: <br>
a. IV  - "in vocabulary", such that the form from the tweet was found in the dictionary, and is consequently not a candidate for normalisation.<br>
b. OOV - "out of vocabulary", such that the form of the token from the tweet was not found in the dictionary, and thus the token was a 
candidate for normalisation.<br>
c. NO  - "not a normalisation candidate", such that the token was not considered in the normalisation process.
The program takes roughly 8 to 9 mins to execute.<br>

- References and required material:<br>
1. edit distance python package<br>
https://pypi.python.org/pypi/editdistance<br>
2. ngram python package<br>
https://pypi.python.org/pypi/ngram<br>
3. Ahmed Bilal, (28-30 July 2015), Lexical Normalization of Twitter Data, Published in:  Science and Information Conference, 2015. Available at: 
https://arxiv.org/abs/1409.4614v<br>
4. Bo Han and Timothy Baldwin (2011) Lexical normalisation of short text messages: Makn sens a #twitter. In Proceedings of the 49th Annual Meeting of 
the Association for Computational Linguistics, Portland, USA. pp. 368–378.
