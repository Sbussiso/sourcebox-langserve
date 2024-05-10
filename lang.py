#!/usr/bin/env python
from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatAnthropic, ChatOpenAI
from langserve import add_routes
from dotenv import load_dotenv
import os

load_dotenv()


secret_key1 = os.getenv("OPENAI_API_KEY")
secret_key2 = os.getenv("ANTHROPIC_API_KEY")


app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple api server using Langchain's Runnable interfaces",
)

# base gpt
add_routes(
    app,
    ChatOpenAI(),
    path="/openai",
)

# base anthropic
add_routes(
    app,
    ChatAnthropic(),
    path="/anthropic",
)

# joke generator
model = ChatAnthropic()
prompt = ChatPromptTemplate.from_template("tell me a joke about {topic}")
add_routes(
    app,
    prompt | model,
    path="/joke",
)


# content sumarizer
model = ChatOpenAI()
prompt = ChatPromptTemplate.from_template("provide a short and comprehensive summary of this content: {content}")
add_routes(
    app,
    prompt | model,
    path="/summary",
)


# basic limited fact checker
model = ChatOpenAI()
prompt = ChatPromptTemplate.from_template("use your knowlege to fact check this information: {info}\n always site your sources including date published.")
add_routes(
    app,
    prompt | model,
    path="/fact-check"
)

# SourceBox customer ticket solver #! not yet tested
model = ChatOpenAI()
prompt = ChatPromptTemplate.from_template("You are an employee at SourceBox The hybrid machine learning platform with a local bias. Your Job is to solve this customers support ticket here using only information from SourceBox: {ticket}")
add_routes(
    app,
    prompt | model,
    path="/sourcebox-ticket-solver"
)


# SourceBox Updates internet tweeter
model = ChatOpenAI()
prompt = ChatPromptTemplate.from_template("You are a social media manager for SourceBox, an AI platform for local open source models and solutions. You are to create a tweet based on this platform update {update}")
add_routes(
    app,
    prompt | model,
    path="/sourcebox-marketing-team"
)


if __name__ == "__main__":

    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)