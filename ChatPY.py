import json
import re
import difflib

print("\n" * 100)
print("   _____ _           _   _______     __\n  / ____| |         | | |  __ \ \   / /\n | |    | |__   __ _| |_| |__) \ \_/ / \n | |    | '_ \ / _` | __|  ___/ \   /  \n | |____| | | | (_| | |_| |      | |   \n  \_____|_| |_|\__,_|\__|_|      |_|   ")
print("\n")
print("----------------- ChatPY -----------------")
print("\n")
print("=> New Chat \n")

def ChatPY(query):
    print("ChatPY : " + query)

def You():
    return input("You : ")

def filter(text):
    filtered = re.sub(r'[^a-zA-Z]+', '', text)
    filtered = filtered.lower()
    return filtered

def lern(query):
    global data
    unknow = query
    ChatPY("I don't know what to say to that, will you teach me ? (Y/N)")
    query = You()
    if query.lower() == "y":
        ChatPY(f"What should I say to : '{unknow}' ?")
        query = You()
        data[filter(unknow)]= query

        # write data
        with open("data.txt", "w") as fp:
            json.dump(data, fp)  # encode dict into JSON
    else:
        ChatPY("Okay ;)")

# read data
with open("data.txt", "r") as fp:
    data = json.load(fp)

while True:        
    query = You()
    if query not in data:
        
        # find similar key
        closest_match = difflib.get_close_matches(query, data.keys(), n=1, cutoff=0.6)
        if closest_match:
            closest_key = closest_match[0]
            ChatPY(f"Did you mean: {closest_key}? (Y/N)")
            choice = You()
            if choice.lower() == "y":
                print(data[closest_key])
            else:
                lern(query)
        else:
            lern(query)

    else:
        ChatPY(data[query])
