#Hashing Extention Second Edition v1.0
#Reimplemented All Features
import hashlib
class Hashing:
    #def __init__(self,salt):
        #self.salt=salt
    def __init__(self):
        self.salt="MeowTechHashing"#Please Change
    def hash(self,data):
        hasher = hashlib.md5()
        value = data + self.salt
        hasher.update(value.encode("utf-8"))
        hashed = hasher.hexdigest()
        return hashed
    def check(self,original,correct):
        hasher = hashlib.md5()
        value = original + self.salt
        hasher.update(value.encode("utf-8"))
        hashed = hasher.hexdigest()
        return hashed == correct
Hasher=Hashing()
