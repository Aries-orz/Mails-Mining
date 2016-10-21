__author__ = 'a_medelyan'

import rake
import operator

# EXAMPLE ONE - SIMPLE
stoppath = "SmartStoplist.txt"

# 1. initialize RAKE by providing a path to a stopwords file
rake_object = rake.Rake(stoppath, 1, 3, 5)

# 2. run on RAKE on a given text
sample_file = open("2006.txt", 'r')
text = sample_file.read()

keywords = rake_object.run(text)

# 3. print results
#print "Keywords:", keywords
fout = open("./keywords/keywords2006.txt", 'w')
fout.write('Keywords:\n%s' %keywords)
fout.close()
#print "Keywords:", keywords
'''
print "----------"
# EXAMPLE TWO - BEHIND THE SCENES (from https://github.com/aneesha/RAKE/rake.py)

# 1. initialize RAKE by providing a path to a stopwords file
rake_object = rake.Rake(stoppath)

text = "Compatibility of systems of linear constraints over the set of natural numbers. Criteria of compatibility " \
       "of a system of linear Diophantine equations, strict inequations, and nonstrict inequations are considered. " \
       "Upper bounds for components of a minimal set of solutions and algorithms of construction of minimal generating"\
       " sets of solutions for all types of systems are given. These criteria and the corresponding algorithms " \
       "for constructing a minimal supporting set of solutions can be used in solving all the considered types of " \
       "systems and systems of mixed types."



# 1. Split text into sentences
sentenceList = rake.split_sentences(text)

for sentence in sentenceList:
    print "Sentence:", sentence

# generate candidate keywords
stopwordpattern = rake.build_stop_word_regex(stoppath)
phraseList = rake.generate_candidate_keywords(sentenceList, stopwordpattern)
print "Phrases:", phraseList

# calculate individual word scores
wordscores = rake.calculate_word_scores(phraseList)

# generate candidate keyword scores
keywordcandidates = rake.generate_candidate_keyword_scores(phraseList, wordscores)
for candidate in keywordcandidates.keys():
    print "Candidate: ", candidate, ", score: ", keywordcandidates.get(candidate)

# sort candidates by score to determine top-scoring keywords
sortedKeywords = sorted(keywordcandidates.iteritems(), key=operator.itemgetter(1), reverse=True)
totalKeywords = len(sortedKeywords)

# for example, you could just take the top third as the final keywords
for keyword in sortedKeywords[0:(totalKeywords / 3)]:
    print "Keyword: ", keyword[0], ", score: ", keyword[1]

print rake_object.run(text)'''
