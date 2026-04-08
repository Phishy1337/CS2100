from RSA import RSA

rsa = RSA()

string1 = """
Heed my words. I am Malenia, Blade of Miquella, and I have never known defeat
Heed my words. I am Malenia, Blade of Miquella, and I have never known defeat
Heed my words. I am Malenia, Blade of Miquella, and I have never known defeat
Heed my words. I am Malenia, Blade of Miquella, and I have never known defeat
Heed my words. I am Malenia, Blade of Miquella, and I have never known defeat
"""

string2 = """
You're absolutely right. It's all meaningless. No matter what dreams or hopes you had... 
No matter how happy a life you've led... it's all the same if you're shredded by rocks. 
Everyone will one day die. Does that mean life is meaningless? Was there no meaning in our being born? 
Would you say that of our fallen comrades? Their lives... were they meaningless? No, they weren't!

It's us who give meaning to our comrades' lives! The brave fallen! The anguished fallen! 
The ones who can remember them are us, the living! We die here and entrust the meaning to the next living! 
Because my soldiers do not buckle or yield when faced with the cruelty of this world! 
My soldiers push forward! 
My soldiers scream out! 
My soldiers RAGE!
"""

rsa.GenerateKeys(string1, string2)
rsa.encrypt("try_encrypting_long.txt", "test.txt")
