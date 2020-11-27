# Author     : Vedant Chauhan
# Student id : 892758
import editdistance
import ngram

tweetList = []
tempTokens = []
writer = []

# Read tweets file and store in a list
with open("tweets.txt",'r') as tweetFile:
    tweetList = [line.strip() for line in tweetFile]

# Iterate the list and split on space
for string in tweetList:
    tempTokens.append(string.split(" "))

# Classify tokens into Code(IV, OOV, NO)
for tokensArray in tempTokens:
    for tokens in tokensArray:
       if (tokens.startswith(":") or tokens.startswith("\"") or
          tokens.startswith("!") or tokens.startswith("'") or
          tokens.startswith("?") or tokens.startswith(".") or
          tokens.startswith("(") or tokens.startswith(")") or
          tokens.startswith(" ")):
          pass
       elif (tokens.startswith("@") or tokens.startswith("#") or
             tokens.startswith("http") or tokens.startswith("0") or
             tokens.startswith("1") or tokens.startswith("2") or
             tokens.startswith("3") or tokens.startswith("4") or
             tokens.startswith("5") or tokens.startswith("6") or
             tokens.startswith("7") or tokens.startswith("8") or
             tokens.startswith("9")):
          # NO Code
          token = tokens + "\t" + "NO" + "\t" + tokens
          writer.append(token)
       else:
          # Read dictionary file
          dictFile = open("dict.txt", 'r')

          # Default comparison values
          best_edit_val = 999999999L
          best_ngram_val = 0.3

          # Iterate over dictionary file and compare it with tokens
          for dictLine in dictFile:
             # Edit distance calculations
             distance_val = editdistance.eval(tokens,dictLine.strip())
             if distance_val < best_edit_val:
                 best_edit_val = distance_val
                 best_match = dictLine.strip()

             # N-Gram calculations, n=2
             ngram_val_edit = ngram.NGram.compare(best_match,dictLine,N=2)
             if ngram_val_edit > best_ngram_val:
                best_ngram_val = ngram_val_edit
                ngram_match = dictLine.strip()

          # Comparison based on token values, 0 is a match with dictionary
          if (best_edit_val == 0L):
             # match in dictionary then IV from edit distance
             token = tokens + "\t" + "IV" + "\t" + best_match
          else:
             # not match in dictionary then OOV from n-gram value
             token = tokens + "\t" + "OOV" + "\t" + ngram_match

          writer.append(token)

# Write contents of list in the output file
writeContents = open("tokenResults.txt", 'w')
for item in writer:
   writeContents.write("%s\n" % item)
dictFile.close()
tweetFile.close()