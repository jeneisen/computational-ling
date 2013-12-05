#1. 
nouns = ["dog", "cat", "apple", "book"]
 
#2. 
nouns[1]
# returns'cat'
 
#3. 
sorted(nouns)
# returns ['apple', 'book', 'cat', 'dog'] in alphabetical order
 
#4. 
animals = nouns[:2]
#animals now equals ['dog', 'cat']
 
#5. 
copy1 = nouns
copy2 = ["dog", "cat", "apple", "book"]
#copy1 returns ['dog', 'cat', 'apple', 'book']
#copy2 returns ["dog", "cat", "apple", "book"]
copy1 == copy2
#returns True
 
#6. 
nouns.append('egg')
#now nouns returns ['dog', 'cat', 'apple', 'book', 'egg']
 
#7. Because the append method is destructive, the methods changes the 
object itself so the noun object now has the word "egg" appended to the 
list.
# However copy2 was not affected because we manually assigned the value to 
be ["dog", "cat", "apple", "book"] and we would have to manually appened 
the word "egg" to copy2 in order to copy2 to have "egg" included in the 
list.
# Thus now when I type copy1 == copy2, False is returned.
 
#8. 
ani3 = animals * 3
# animals * 3 returns ['dog', 'cat', 'dog', 'cat', 'dog', 'cat']
 
#9. 
ani = set(ani3)
#ani returns set(['dog', 'cat'])
 
#10. 
len(ani)
# returns 2
 
#11. 
'elephant' in ani
#returns False
 
#12. 
#nouns returns ['dog', 'cat', 'apple', 'book', 'egg']
nouns[2] + 's'
#returns 'apples'
 
#13. 
alphabet = ["ant", "bee", "cee", "dee", "el", "eph", "gee"]
alphabet[4] + alphabet[5] + alphabet[0]
#returns 'elephant'
 
#14. 
alphabet[1][0:2] + alphabet[0][1:3]
returns 'bent'
