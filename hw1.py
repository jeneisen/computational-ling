1a.
8 + 2 * 3
14

1b.
(8+2) * 3
30

2.
20/3
6
This prompt 20/3 is dividing the two integers.
In order to get the actual answer "6.666666666666667" without doing from __future__ 
import division we can write "20.0/3.0" to get "6.666666666666667".

3a.
text1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'text1' is not defined

3b.
In order to get the expected result, I need to type "from nltk.book import *" to 
import the submodule available to us.

text1
<Text: Moby Dick by Herman Melville 1851>
This returns the text1 object.

4. Words that occur immediately after "great" in text6 "Monty Python and the Holy 
Grail": peril, escape, (. Arthur), idea. If we also count capital letters then the 
word "scott" also follows the word "Great".

5a. txt.condordance("monstrous")
In order to correct "txt" to "text" I would hit the "up" arrow key to return the text 
again and then I'd press Ctl-A to move the cursor 
immediately to the beginning of the line and then use the right arrow key to insert 
the letter "e" after the "t".
(This is all assuming MAC key strokes).

5b. If I notice a typo and hit the Return key, Python will throw some type of 
error like ">>> txt.condordance("monstrous")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'txt' is not defined"
To avoid retyping the whole line next time I just just hit the up arrow to reload 
the text I just wrote and edit the line from there (using ctrl+A again to get back 
to the beginning of the line.

6. The question "how many words are there in Genesis" is ambiguous.

6a. There are various ways to interpret this sentence. One may be asking how many 
words are there in the phrase 'Genesis' and the answer would be 1 ('genesis'). On 
the other hand, one may be asking how many words are there in the entire text of the 
book called "Genesis" where the answer could range up to hundreds of thousands.

6b. 1 and 44764

7. The word "multitude" occurs more often. Star: 5 & Multitude: 7.

8. 

x = len(text1)
y = len(set(text1))
z = text1.count("whale")
   
print "Tokens: ", x          
print "Types: ", y                 
print "Count of 'whale': ", z                      

(I ran new file called homework1.py to see the correct output below)

>>> execfile('homework1.py')
Tokens:  260819
Types:  19317
Count of 'whale':  906

