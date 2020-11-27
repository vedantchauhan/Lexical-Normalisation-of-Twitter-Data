# Lexical-Normalisation-of-Twitter-Data

- Author     : Vedant Chauhan
This file, which describes problem context, program implementation details, procedure to execute program, files used in program, 
output details and references and required material.

- Program context: Lexical normalisation of twitter data. 
Twitter messages contain elisions, misspellings, grammatical errors, poses a challenge. In order to make sense of Twitter messages we need to 
convert them into a canonical form, consistent with the dictionary. This is called lexical normalisation of individual tokens. 

- Implementation details and Execution of program:
The program is implemented in python. The program uses edit distance and n-gram to classify tokens. Inorder for this program to work python 
package of edit distance, and n-gram is needed in the system. The path /LexicalNorm/ has Proj1.py file. Run this program in terminal by 
executing the following command:
python Proj1.py

- Files used and Output details:
The files dict.txt (dictionary file), tweets.txt (input tweets file), tokenResults.txt (output tokens with best match) should be in 
the the directory /LexicalNorm/.
The format of these files are:
1. tweets.txt
A list of tweets, one per line. Each tweet is comprised of a space-delimited list of tokens. The tweets have been case-folded, where any 
upper-case (English) characters have been converted to their lower-case equivalent.
2. tokenResults.txt
Token TAB Code TAB Canonical_Form
where 
Token: is drawn from the tweet text, 
Canonical_Form: is the normalised version of the token,
Code: can take one of three values: 
a. IV  - "in vocabulary", such that the form from the tweet was found in the dictionary, and is consequently not a candidate for normalisation.
b. OOV - "out of vocabulary", such that the form of the token from the tweet was not found in the dictionary, and thus the token was a 
candidate for normalisation.
c. NO  - "not a normalisation candidate", such that the token was not considered in the normalisation process.
The program takes roughly 8 to 9 mins to execute.

- References and required material:
1. edit distance python package
https://pypi.python.org/pypi/editdistance
2. ngram python package
https://pypi.python.org/pypi/ngram
3. Ahmed Bilal, (28-30 July 2015), Lexical Normalization of Twitter Data, Published in:  Science and Information Conference, 2015. Available at: 
https://arxiv.org/abs/1409.4614v
4. Bo Han and Timothy Baldwin (2011) Lexical normalisation of short text messages: Makn sens a #twitter. In Proceedings of the 49th Annual Meeting of 
the Association for Computational Linguistics, Portland, USA. pp. 368–378.
