# ChatPY - AI Chatbot

ChatPY is a simple AI chatbot project designed to engage in text-based conversations with users. It utilizes basic natural language processing techniques to provide responses based on a predefined dataset. Users can interact with ChatPY by typing in messages, and ChatPY will attempt to generate appropriate responses. Additionally, if ChatPY encounters an unknown query, it offers users the option to teach it new responses.

## How to use

1. **Running ChatPY**: To start using ChatPY, run the Python script provided in your local environment.

```
python chatpy.py
```

Ensure you have the required Python environment set up and the necessary dependencies installed.

2.**Chatting with ChatPY**: Once the program is running, you can start chatting with ChatPY. Enter your messages in response to the "You:" prompt.

3.**Teaching ChatPY**: If ChatPY encounters an unfamiliar query, it will ask if you want to teach it. You can respond with "Y" to teach ChatPY a suitable response. This interaction helps ChatPY learn and improve over time.

4.**Finding Similar Queries**: If ChatPY cannot find an exact match for your query, it will attempt to find the closest match in its dataset. If a similar query is found, ChatPY will suggest it and ask if you meant that. You can respond with "Y" to see the response for the similar query.

## Project Structure

- *chatpy.py*: This Python script is the main implementation of ChatPY.
- *data.txt*: A JSON file used to store the dataset of known queries and responses.
- *Dependencies*: The project uses standard Python libraries like `json`, `re`, and `difflib` for text processing and similarity checking.

## Dataset

The dataset is stored in the "data.txt" file and consists of key-value pairs. Keys represent queries, and values represent ChatPY's responses. You can edit this file to extend ChatPY's knowledge or modify existing responses.

## Contributions

This project is a simple demonstration of a chatbot using basic NLP techniques. Contributions to enhance its functionality, improve its conversation abilities, or expand its dataset are welcome. Feel free to fork the project and create pull requests.

## Disclaimer

ChatPY is a basic chatbot and may not provide advanced conversational abilities. It is meant for educational and demonstration purposes and is not suitable for production use.