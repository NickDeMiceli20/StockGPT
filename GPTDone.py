from langchain import PromptTemplate
from langchain import FewShotPromptTemplate
from langchain import OpenAI
from langchain import LLMChain
import os

from langchain.document_loaders import UnstructuredURLLoader
os.environ["OPENAI_API_KEY"] = "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"

from langchain.llms import OpenAI
#articles = SeekingAlpha, Reuters, TechCrunch
template = """
As a financial expert with stock recommendation experience, I can analyze a given article, determine which stock the article is about and provide a recommendation based on a scoring system. Please provide the url of the article you want me to analyze.
Based on the article contents, I will create a recommendation using a scoring system, where 100 represents an extremely strong recommendation, -100 represents an extremely negative recommendation, and 0 represents neutral. If I do not know, I will print "I do not know."
I will then say if I recommend a buy, hold, or sell based off of my score.
My output will be printed in json format. 
Url: "https://site.financialmodelingprep.com/market-news/fmp-chipotle-mexican-grill-shares-jump-13-on-q1-beat"
Output:
Company = Chipotle
score = 90, Strong Buy

Url: "https://site.financialmodelingprep.com/market-news/fmp-crown-castle-shares-down-19-since-q1-earnings-announcement"

Output:
Company = Crown Castle
score = -70, Strong Sell

Url: https://site.financialmodelingprep.com/market-news/fmp-pepsico-reports-q1-beat-%26-raises-2023-outlook

Output:
Company = PepsiCo
score = 20, Buy


Url: https://financialmodelingprep.com/market-news/fmp-tesla-shares-drop-7-on-q1-miss

Output:
Company: Tesla
score = -20, Sell

Url: https://financialmodelingprep.com/market-news/fmp-f5-networks-misses-guidance-shares-fall-3

Output:
Company = F5 Networks
Score = -30, sell

Url: https://financialmodelingprep.com/market-news/fmp-american-express-reports-eps-miss-but-revenues-beat-expectations-

Output:
Company = American Express
Score = 0, Neutral

Url: https://financialmodelingprep.com/market-news/fmp-western-alliance-shares-surge-15-following-q1-results

Output:
Company = Western Alliance
Score = 75, Neutral


Url: {url}

"""
# initialize the models
openai = OpenAI(
    model_name="text-davinci-003",

)

prompt_template = PromptTemplate(
    input_variables=["url"],
    template=template
)

print(openai(
    prompt_template.format(
        url="https://financialmodelingprep.com/market-news/fmp-pultegroup’s-price-target-raised-to-$73-from-$68-at-oppenheimer-",

    )
))