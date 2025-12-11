class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        
        if len(words) != len(pattern):
            return False
        
        p_to_w = {}
        w_to_p = {}
        
        for ch, word in zip(pattern, words):
            if ch in p_to_w:
                if p_to_w[ch] != word:
                    return False
            else:
                p_to_w[ch] = word
            
            if word in w_to_p:
                if w_to_p[word] != ch:
                    return False
            else:
                w_to_p[word] = ch
        
        return True