import heapq
def alienDict (all_words):
    '''Create a Trie'''
    adj_list={w: [] for word in all_words for w in word}
    for i in range(len(all_words)-1):
        w1, w2=all_words[i], all_words[i+1]
        if len(w1)==len(w2):
            
