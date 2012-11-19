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

The dictionary we employed is an English-Chinese one, which contains the word, charactertistic, and explanation.

The dictionary in this repo is converted from a [original ISO-8859 version](http://nlp.nju.edu.cn/MT_Lecture/dic_ec.rar "Nanjing University  NLP resource") to UTF-8.

**DO NOT** use them for any commercial purposes.


##Project 2: Chinese words segmentation

###Goals

Segment a sentence into phrases using the dictionary and rules.

###Segmentation Algorithm

Forwarding Maximum Matching(FMM).

In practice, we deploy the FMM method with a recursive function.

###Dictionary

The dictionary we employed is a Chinese-English one, and only the Chinese phrases are used for matching.

The dictionary in this repo is converted from a [original ISO-8859 version](http://nlp.nju.edu.cn/MT_Lecture/dic_ce.rar "Nanjing University  NLP resource") to UTF-8.

**DO NOT** use them for any commercial purposes.

###Usage

You can simply run the program with command `python segmentation.py` in a command line mode.

This program also provides a GUI mode built on [wxPython](http://www.wxpython.org/), a cross-platform GUI library with Python programming language. Please install wxPython 2.8 version to support the GUI mode.

##License

This program is distributed under GNU General Public License.

***

Copyright (C) 2012 Dongliang Yu

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.

***
