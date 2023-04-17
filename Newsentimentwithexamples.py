from langchain import PromptTemplate
from langchain import FewShotPromptTemplate
from langchain import OpenAI
from langchain import LLMChain
import os
from main import date_url_dict
from langchain.document_loaders import UnstructuredURLLoader
os.environ["OPENAI_API_KEY"] = "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"

from langchain.llms import OpenAI
#articles = SeekingAlpha, Reuters, TechCrunch
template = """
As a financial expert with stock recommendation experience, I can analyze a given article on a stock and provide a recommendation based on a scoring system. Please provide the url of the article and the name of the company you want me to analyze.

Based on the article contents, I will create a recommendation using a scoring system, where 1 represents an extremely strong recommendation, -1 represents an extremely negative recommendation, and 0 represents neutral. If I do not know, I will print "I do not know."

After analyzing the article, I will provide a 400 word paragraph about the article indicating whether the article is positive, negative, or neutral, why and in terms of its impact on the company's stock price in the future. Based on my analysis summary, I will indicate if this is a strong buy, a buy, hold, sell or strong sell.

My output will be printed in json format. 

Url: "https://seekingalpha.com/article/4594341-bank-earnings-charles-schwab-takeover-and-clean-energy-with-kirk-spano"
Stock: Charles Schwab

Output:
score = 1,
company = Charles Schwab,
summary = Charles Schwab is a financial services company 
that provides investment and trading services, including brokerage, banking, and financial advisory services to 
individuals and institutions.
Analyst Kirk Spano reviewed the earnings report and noted that Schwab's management team has been "executing well and 
has a solid plan for the future." Spano sees Schwab as a "well-positioned company in a growing industry" and recommends 
investors buy the stock for the short and long term. He also advises investors to consider other factors that could influence
Schwab's price such as its financials and other macro factors. Schwab's earnings report was also covered in an article on
Seeking Alpha, which echoed many of Spano's points. The article noted that Schwab's trading volumes have been strong throughout
2021, and the TD Ameritrade acquisition is expected to bring significant cost savings and revenue synergies. The article
also discussed the company's focus on clean energy, which is in line with the broader trend of companies transitioning to
sustainable business practices. The Seeking Alpha article concluded that Schwab is a "well-run company that is well-positioned
for the future" and recommended investors buy the stock for the long term. The article also noted that Schwab has a solid
track record of returning value to shareholders through stock buybacks and dividends. Overall, the sentiment around
Charles Schwab is positive, with both Kirk Spano and Seeking Alpha recommending investors buy the stock for the short
and long term. Schwab's strong earnings report, recent acquisition, and focus on clean energy are all seen as positive
developments that are likely to have a positive impact on the stock's price in the future. However, investors should
always consider other factors such as the broader market conditions and macroeconomic trends when making investment decisions.


Url: "https://www.reuters.com/technology/alphabet-falls-report-samsung-considering-bing-default-search-engine-2023-04-17/"
Stock: "Alphabet"

Output:
score = -1
company = Alphabet,
summary = Alphabet is a multinational conglomerate that primarily specializes in internet-related services and products,
including online advertising technologies, search engines, and cloud computing.
As a financial analyst, I believe that losing the default search engine deal with Samsung would be negative for Alphabet's 
stock. Samsung is one of the world's largest smartphone manufacturers, and Google's search engine is the default on all Samsung 
devices. Losing the default search engine deal with Samsung could potentially result in a decline in market share and revenue 
for Google's search business. Google's search business is the largest contributor to the company's advertising revenue, 
which is a significant source of revenue for the company. In addition to the potential loss of market share and revenue,
the news could also lead to decreased investor confidence in the company's future growth prospects. The decline in 
investor confidence could result in a further decline in the stock price. The stock has already experienced a decline
following the news, indicating that investors are concerned about the impact of the potential loss of the default
search engine deal with Samsung. Overall, I believe that the news reported in this article is negative for Alphabet's stock.
Losing the default search engine deal with Samsung could potentially result in a decline in market share and revenue for
Google's search business, which is a significant source of revenue for the company. Additionally, the news could lead 
to decreased investor confidence in the company's future growth prospects, which could result in a further decline in 
the stock price. Therefore, I recommend that investors look to either hold or sell the stock for the short and long term
based on this article. I also recommend looking more into other factors that could influence Alphabet's price such as 
its financials and other macro factors.

Url: {url}
Stock{stock}

Output:
"""
# initialize the models
openai = OpenAI(
    model_name="text-davinci-003",

)

prompt_template = PromptTemplate(
    input_variables=["url", "stock"],
    template=template
)

print(openai(
    prompt_template.format(
        url="https://www.reuters.com/markets/deals/merck-late-stage-talks-acquire-prometheus-biosciences-wsj-2023-04-16/",
        stock='Prometheus Biosciences'
    )
))