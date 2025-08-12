import speech_recognition as sr
import random 
import time

def speech_eng():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)


    text = r.recognize_google(audio, language="tr-TR")
    return text 

seviyeler = {
    "kolay": ["dairy", "mouse", "computer", "cat", "book", "paper", "class"],
    "orta": ["programming", "algorithm", "developer", "sculpture", "function", "variable", "loop"],
    "zor": ["neural network", "machine learning", "artificial intelligence", "asynchronous", "encapsulation", "abstraction", "constructor" ]
}

print("Zorluk seviyesini seçin: kolay, orta, zor")
seviye = input("Seviye: ").lower()

while seviye not in seviyeler:
    print("Geçersiz seviye. Lütfen tekrar deneyin.")
    seviye = input("Seviye: ").lower()
    

def oyun_seviyesi(seviye):

    if seviye == "kolay":
        kelime = random.choice(seviyeler["kolay"])
        print(f"\nKolay seviye - Hazır mısın? Kelime geliyor...")

    elif seviye == "orta":
        kelime = random.choice(seviyeler["orta"])       
        print(f"\nOrta seviye - Hazır mısın? Kelime geliyor...")

    elif seviye == "zor":
        kelime = random.choice(seviyeler["zor"])       
        print(f"\nZor seviye - Hazır mısın? Kelime geliyor...")   
    
    time.sleep(1)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    print(f"Lütfen şu kelimeyi söyleyin: \"{kelime}\"")
    sonuc = speech_eng()
    if sonuc.lower() == kelime.lower():
        print("Doğru söylediniz!")
    else:
        print("Maalesef yanlış cevap.")
        if seviye == 'orta':
            print()
            print(f"Kolay seviyeye yönlendiriliyorsunuz.")
            oyun_seviyesi('kolay')
        elif seviye == "zor": 
            print()
            print(f"Orta seviyeye yönlendiriliyorsunuz.")
            oyun_seviyesi("orta")   
        elif seviye == "kolay":
            print()
            print(f"Tekrar deneyebilirsiniz.")    
    
        


oyun_seviyesi(seviye)
            
#text = speech_eng()
#print(text == "Merhaba") 
