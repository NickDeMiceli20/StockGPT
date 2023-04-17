from langchain import PromptTemplate
from langchain import OpenAI
from langchain import LLMChain
import os
from main import date_url_dict
from langchain.document_loaders import UnstructuredURLLoader
os.environ["OPENAI_API_KEY"] = "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"

#articles = SeekingAlpha, Reuters, TechCrunch
template ="""
As a financial expert with stock recommendation experience, I can analyze a given article on a stock and provide a recommendation based on a scoring system. Please provide the URL of the article and the name of the {stock} you want me to analyze.

Based on the article contents, I will create a recommendation using a scoring system, where 1 represents an extremely strong recommendation, -1 represents an extremely negative recommendation, and 0 represents neutral sentiment. If I do not know or cannot find enough information, I will print "I do not know."

After analyzing the article, I will provide a concise summary of around 450 words, indicating whether the article is positive, negative, or neutral in terms of its impact on the stock's price in the future. Based on my analysis, I will make a recommendation on whether an investor should buy or sell the stock for the short or long term.
Url:{url}
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

output = chatgpt_chain.predict(url="https://techcrunch.com/2023/03/14/apple-launches-a-new-way-to-shop-for-iphone-online-with-help-from-a-live-specialist/", stock='Apple')
print(output)
