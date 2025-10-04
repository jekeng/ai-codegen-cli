from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
import argparse
from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain.schema.runnable import RunnableMap

load_dotenv()

parser = argparse.ArgumentParser()
parser.add_argument("--language", type=str, default="python")
parser.add_argument("--task", type=str, default="return list of numbers from 1 to 10")
args = parser.parse_args()

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY"),
)

code_template = PromptTemplate(
    template=(
        "Write only the {language} code that will {task}. "
        "Do not define any function, class, or add explanations. "
        "Just give the code lines needed to perform it."
    ),
    input_variables=["language", "task"],
)

test_template = PromptTemplate(
    template=(
        "Write only the {language} code that tests the following code: {code}. "
        "Do not define any function, class, or add explanations. "
        "Just give the test code lines."
    ),
    input_variables=["language", "code"],
)

code_chain = code_template | llm
test_chain = test_template | llm

chain = (
    code_chain
    | (lambda x: {"language": args.language, "code": x.content})
    | RunnableMap({
        "code": lambda x: {"language": x["language"], "code": x["code"]},
        "test": lambda x: {
            "language": x["language"],
            "code": test_chain.invoke({"language": x["language"], "code": x["code"]}).content,
        }
    })
)

result = chain.invoke({
    "language": args.language,
    "task": args.task
})

print(result["test"])
print("--------------------------------")
print(result["code"])
