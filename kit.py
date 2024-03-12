import openai
import os
import json

openai.api_key = "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"

def xyi(question):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": question}
        ]
    )
    return completion.choices[0].message.content

def zxc(file_path, question, answer):
    data = {"question": question, "answer": answer}
    with open(file_path, "a") as file:
        if os.stat(file_path).st_size > 0:
            
            file.write(",\n")
        json.dump(data, file, ensure_ascii=False, indent=None)

def main():
    question = "являются ли кентавры насекомыми т к у них 6 конечностей??"
    answer = xyi(question)
    
   
    file_path = "C:/Users/ka1zj7/Desktop/kitkit/chat_log.json"
    
   
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
   
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            file.write("[\n")
    
    
    zxc(file_path, question, answer)
    
    
    with open(file_path, "a") as file:
        file.write("\n]")

    print("зачилься ошибок нет")

if __name__ == "__main__":
    main()

