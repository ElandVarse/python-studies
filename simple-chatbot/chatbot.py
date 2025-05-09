intents = {
    ("oi", "olá", "e aí", "ola", "aloha"): "Oi! Como posso te ajudar?",
    ("hi mark"): "Oh Hey Johnny, what's up?",
    ("nome", "quem é você"): "Eu sou um chatbot inteligente 😎",
    ("tchau", "até mais"): "Até logo! Volte sempre."
}

def chatbot():
    print("Bot: Olá! Como posso te ajudar hoje?")
    
    while True:
        user_input = input("Você: ").lower()
        
        if user_input in ["sair", "fechar"]:
            print("Bot: Encerrando conversa. Até mais!")
            break
        
        matched = False
        for keys, response in intents.items():
            if user_input in keys:
                print(f"Bot: {response}")
                matched = True
                break
        
        if not matched:
            print("Bot: Hmm... não entendi. Pode reformular?")

chatbot()
