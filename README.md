#Natural Language Processing Programming Assignments

##Project 1: English words stemming

###Goals

  1. Input a word and get its attributes such as characteristic and explanation.
  2. If the word matches a rule which could restore the word to its original state, and the restored word exists in the dictionary. Then we could get the attributes of the restored word.
  3. If none of the original and restored word(if exists) could be found in dictionary, we get nothing.

###Rules
####Regular verbs:

    *s -> * (SINGULAR3)
    *es -> * (SINGULAR3)
    *ies -> *y (SINGULAR3)
    *ing -> * (VING)
    *ing -> *e (VING)
    *ying -> *ie (VING)
    *??ing -> *? (VING)
    *ed -> * (PAST)(VEN)
    *ed -> *e (PAST)(VEN)
    *ied -> *y (PAST)(VEN)
    *??ed -> *? (PAST)(VEN)

####Irregular verbs:
**not included yet**

###Dictionary
The dictionary in this repo is converted from a [original ISO-8859 version](http://nlp.nju.edu.cn/MT_Lecture/dic_ec.rar) to UTF-8.

**DO NOT** use them for any commercial purposes.


##Project 2: Chinese words segmentation

**TODO**