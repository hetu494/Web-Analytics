def loadLexicon(fname):
    newLex=set()
    lex_conn=open(fname)
    #add every word in the file to the set
    for line in lex_conn:
        newLex.add(line.strip())# remember to strip to remove the lin-change character
    lex_conn.close()

    return newLex

def run(path):
    decisions=[] 
    reviews=[]
    PL=[]
    count = 0
    #load the positive and negative lexicons
    posLex=loadLexicon('positive-words.txt')
    #negLex=loadLexicon('negative-words.txt')
    
    fin=open(path)
    for line in fin: # for every line in the file (1 review per line)
        posList=[] #list of positive words in the review
        negList=[] #list of negative words in the review
        line=line.lower().strip()   
        reviews.append(line)
        
        words=line.split(' ') # slit on the space to get list of words
	for word in posLex:
		if word in words:
			PL.append(word)
			count = count + 1
			print PL,count
    #print PL
    #for i in PL:
	#print i
    result = dict((i, PL.count(i)) for i in PL)
    print result
    fin.close()
    return reviews, decisions

if __name__ == "__main__": 
    reviews,decisions=run('textfile')
    #for i in range(len(reviews)):
	#print (reviews[i])
