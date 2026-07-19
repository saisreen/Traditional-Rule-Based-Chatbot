# Traditional Rule-Based Chatbot

## Project Overview

This project is a simple traditional chatbot developed using Python. Unlike modern AI chatbots that use Large Language Models (LLMs), this chatbot follows a rule-based approach. It identifies user input using predefined keywords and conditional statements and then returns an appropriate response.

The purpose of this project is to demonstrate the basic concepts of human-computer interaction by creating a chatbot capable of responding to common user questions without using artificial intelligence or machine learning techniques.

---

## Project Objectives

The objectives of this project are:

- Develop a chatbot using a traditional rule-based approach.
- Understand how keyword matching works in chatbot development.
- Learn how conditional statements can be used to simulate conversations.
- Handle both valid and invalid user input.
- Demonstrate the chatbot development lifecycle from planning through testing.

---

## Features

The chatbot supports the following features:

- Greets the user.
- Introduces itself.
- Responds to basic questions.
- Displays a list of available commands.
- Provides the current date.
- Provides the current time.
- Ends the conversation when the user enters "bye" or "exit".
- Responds politely when it does not understand a question.

---

## Technologies Used

- Python 3
- Visual Studio Code
- Git
- GitHub

No external Python libraries are required for this project.

---

## Project Structure

```
TraditionalChatbot/
│
├── chatbot.py
├── README.md
├── requirements.txt
└── screenshots/
```

---

## How the Chatbot Works

The chatbot follows a simple conversation flow.

1. The program starts and welcomes the user.
2. It waits for user input.
3. The input is converted to lowercase.
4. The chatbot compares the input with predefined keywords.
5. If a matching keyword is found, the chatbot returns the corresponding response.
6. If no keyword matches, it displays a default message indicating that the question is not recognized.
7. The conversation continues until the user types "bye" or "exit".

This approach is known as a traditional rule-based chatbot because it depends entirely on predefined rules instead of artificial intelligence.

---

## Example Conversation

```
Bot: Hello! Welcome to the Traditional Chatbot.

You: hi

Bot: Hello! How can I help you today?

You: what is your name?

Bot: My name is StudentBot.

You: help

Bot: I can answer greetings, date, time, my name, and say goodbye.

You: time

Bot: Here is the current system time.

You: bye

Bot: Goodbye! Have a great day.
```

---

## Challenges

Some of the challenges encountered during this project include:

- Understanding how traditional chatbots differ from AI-powered chatbots.
- Designing conversation rules for different user questions.
- Handling unexpected user input.
- Testing multiple conversation scenarios.
- Organizing the project files for GitHub.

---

## Future Improvements

The chatbot can be enhanced in several ways:

- Add more predefined questions and answers.
- Store conversations in a database.
- Build a graphical user interface.
- Support voice input and speech output.
- Integrate Natural Language Processing (NLP).
- Connect the chatbot with cloud-based AI services in the future.

---

## Learning Outcomes

Through this project, I learned:

- The basic concepts of chatbot development.
- The chatbot development lifecycle.
- Rule-based conversation design.
- Keyword matching techniques.
- Python conditional statements and loops.
- Basic software testing and debugging.
- Using Git and GitHub for version control.

---

## Author

Student Name: Sai Sree Narla

Course: MSAI-631 – Artificial Intelligence for Human-Computer Interaction

University of the Cumberlands

Summer 2026

---

## License

This project was created for educational purposes as part of a university course assignment.