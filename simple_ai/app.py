from langchain_ollama import OllamaLLM

llm = OllamaLLM(model = 'mistral')

print("Welcome to ollama text AI!")


def loader():
    print("\nThinking ...")

while True:
    question = input("\nI am a AI Agent! I am here to assist you :) -- ")
    if question.lower() == "exit":
        print("\nStay Happy! GoodBye see you tomorrow.....")
        break
    
        
    loader()

    response = llm.invoke(question)
  
    print("\n" + "Answer: " + response)
