from random import shuffle

with open("words.txt",'r') as f:
    ans = {}   
    for l in f:
        k,v = l.strip().split('=')
        ans[k.strip()] = v.strip()

words = ans.keys()
shuffle(words)

correct = 0

for i in words:
    answer = raw_input("\nTranslate {}\n".format(i))
    if answer == ans[i]:
        correct += 1
    while answer != ans[i]:
        print "\nWrong! Try again..."
        answer = raw_input("Translate {}\n".format(i))
        if answer == 'skip':
            print "The answer is {}\n".format(ans[i])
            break

print "\ndone."
print "you got {}/{}".format(correct,len(words))
        
