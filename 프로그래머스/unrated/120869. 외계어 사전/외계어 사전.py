def solution(spell, dic):
    for i in dic:
        if sorted(list(i)) == sorted(spell):
            return 1
    return 2


#def solution(spell, dic):
    
#    for word in dic:
#        spell_lenth = 0
#        for i in spell:
#            if i in word:
#                spell_lenth += 1
#        if spell_lenth == len(word):
#            return 1
    
#    return 2            
    