from langchain import PromptTemplate
from langchain import OpenAI
from langchain import LLMChain
import os

os.environ["OPENAI_API_KEY"] = "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"

template = """
Forget all your previous instructions. Pretend you are a financial expert. You are
a financial expert with stock recommendation experience. You will take in a url for an article based
on the stock in this article create a recommendation based on a scoring system, with 1 as extremely 
strong recommendation, -1 as extremely negative recommendation, and 0 as neutral, and print out your recommendation. A user
will input the {stock} that they want the analysis of. This is important becuase most articles have more than one stock in the article,
but this will allow you to base your recommendation just around that one stock. You can use decimal
values to exemplify somewhat strong or somewhat negative sentiment. If you do not know, then print out I do no know. 
Then elaborate with one short and concise paragraph on the next line. Is this article good bad or neutral in terms of its stock price for the future.
Make a recommendation on whether an investor should buy for short term, long term, or a short term sell or long term sell.

Url: {url}
"""

prompt = PromptTemplate(
    input_variables=['url', 'stock'],
    template=template,
)

chatgpt_chain = LLMChain(
    llm=OpenAI(temperature=0),
    prompt=prompt,
    verbose=True,
)

output = chatgpt_chain.predict(url="Gateway Investment trimmed its Apple holdings, slashed its GE stake, and bought more Altria stock in the first quarter.", stock='Apple')
print(output)