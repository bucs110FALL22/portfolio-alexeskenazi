from functools import reduce

class StringUtility:
    def __init__(self, string: str) -> None:
        self.st = string
    
    def __str__(self) -> str:
        return self.st

    def vowels(self) -> str:
        return str(self.st.lower().count('a') + self.st.lower().count('e') + self.st.lower().count('i') + self.st.lower().count('o') + self.st.lower().count('u')) if self.st.lower().count('a') + self.st.lower().count('e') + self.st.lower().count('i') + self.st.lower().count('o') + self.st.lower().count('u') < 5 else 'many'
  
    def bothEnds(self) -> str:
        return self.st[0] + self.st[1] + self.st[len(self.st)-2] + self.st[len(self.st)-1] if len(self.st) > 2 else ''

    def fixStart(self) -> str:
        return self.st[0] + self.st[1: len(self.st):].replace(self.st[0], '*') if len(self.st) > 0 else self.st

    def asciiSum(self) -> int:
        return sum(map(lambda c: ord(c), self.st))

    
    def cipher(self) -> str:
        return ''.join(map(lambda c: chr((((ord(c) - ord('a')) + len(self.st)) % (ord('Z')-ord('A')+1)) + ord('a')) if ord(c) >= ord('a') and ord(c) <= ord('a')+(ord('Z')-ord('A')+1) else (chr((((ord(c) - ord('A')) + len(self.st)) % (ord('Z')-ord('A')+1)) + ord('A')) if ord(c) >= ord('A') and ord(c) <= ord('A')+(ord('Z')-ord('A')+1) else c)
, self.st))
      
  #####################################################################################################
  ########  Long versions of the methods used to debug and arrive to the one line solutions.
     
    def vowels_long(self) -> str:
        lower = self.st.lower()
        total = lower.count('a') +\
            lower.count('e') +\
            lower.count('i') +\
            lower.count('o') +\
            lower.count('u')
        return str(total) if total < 5 else 'many'

    def fixStart_long(self) -> str:
        length = len(self.st)
        if length <= 0:
            return self.st
        # get a new string without the first char.
        last_part = self.st[1: length:]
        # replace all the ocurrences of the first char with *
        replaced = last_part.replace(self.st[0], '*')
        # combine the original first char with the replaced string.
        return self.st[0] + replaced

    def cipher_long(self) -> str:
        def char_plus_delta(c):

            abc_length = ord('Z')-ord('A')+1
            delta = len(self.st)
            orda = ord('a')
            ordz = ord('z')
            ordA = ord('A')
            ordZ = ord('Z')
            ordc = ord(c)

            # Between a and z
            if ordc >= orda and ordc <= ordz:
                # get the position of c in the alphabet
                pos_c = ordc - orda
                # do the mod calcuation to wrap around the abc
                new_pos_c = (pos_c + delta) % abc_length
                # restore the character in ascii
                new_c = new_pos_c + orda
                return chr(new_c)

            # do the same for upper case and in short form
            if ordc >= ordA and ordc <= ordA+abc_length:
                return chr((((ordc - ordA) + delta) % abc_length) + ordA)

            return c

        return ''.join(map(char_plus_delta, self.st))

    