import re

def chat():
    # Start conversation off on topic
    response = raw_input("BEGIN CONVERSATION: DO YOU PLAY COMPUTER GAMES? ")

    # Run conversation indefinitely until user quits it
    while(True):
        if(re.search("games", response)):
            response = raw_input("WHAT GAMES DO YOU LIKE? ")
        elif(re.search("quake", response)):
            response = raw_input("AH, FIRST PERSON SHOOTERS. NOT MY THING. WHAT ELSE DO YOU PLAY? ")
        elif(re.search("mortal", response)):
            response = raw_input("I LIKE FIGHTING GAMES WITH FRIENDS ONLY. WHAT ELSE DO YOU PLAY? ")
        elif(re.search("scrolls", response)):
            response = raw_input("I LOVE RPGS! THEY'RE MY FAVOURITE. WHAT ELSE DO YOU PLAY? ")
        elif(re.search("don't", response)):
            response = raw_input("THAT'S TOO BAD - THEY'RE REALLY FUN! WHAT DO YOU DO THEN? ")
        elif(re.search("goodbye", response)):
            print("NICE CHATTING TO YOU! BYE FOR NOW.")
            break
        else:
            response = raw_input("I HAVEN'T HEARD OF THAT, BUT IT SOUNDS FUN. WHAT IS IT? ")

# Run chat method when file is executed
chat()