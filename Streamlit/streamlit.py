
import streamlit as st
from PIL import Image
st.header("Decoding Wall Street: Sentiment Analysis of Tesla's Earnings Calls")
# Create two columns
col1, col2 = st.columns([5,2])
with col1:

    st.write("""Sentiment analysis, often referred to as opinion mining, is a powerful tool in the field of data analysis and
             natural language processing (NLP) that aims to determine the underlying sentiment within text-based data. As we
             transition further into an age dominated by digital communication, sentiment analysis serves as a crucial mechanism
             for understanding and interpreting vast amounts of unstructured information. Implementing sentiment analysis 
             can uncover hidden insights that might otherwise remain buried in the sheer volume of data. It can aid in
             the understanding of a company's current standing by identifying trends in sentiment, tracking investor
             perceptions in real-time, and potentially predicting future market behaviors based on historical patterns.""")
    st.write("""In this case study, we introduce a unique approach to sentiment analysis.
             Instead of the common methods that typically focus on individual words or phrases, we developed a more 
             personalized model that analyzes the sentiment of company earnings calls. Our model considers the broader
             context in which words and phrases are used, providing a more comprehensive and accurate sentiment profile.
                 """)

    st.write("""Our analysis delves into the linguistic nuances of company earnings calls, which are rich sources of
             corporate information and sentiment. We demonstrate how our personalized model can help decode these
             intricacies, translating them into actionable investing insights. Through this article, we seek to not only
             showcase the potential of our unique sentiment analysis model but also to reinforce the importance of
             sentiment analysis in today's data-driven investing landscape.""")
# Use the second column for the image
with col2:
    st.image('el.JPG', width=500)

st.header("Industry Challenge")
st.write("""
             Traditional sentiment analysis models often underperformed in the finance sector, primarily due to
             industry-specific lexicon and the varying significance of certain statements. The complexity of
             financial jargon, coupled with the unequal relevance of text in financial documents, often results
             in less accurate sentiment interpretation. Notably, critical statements such as CEO remarks on future
             earnings or risk disclaimers carry substantial weight, despite their brevity. Conventional models,
             which typically assign uniform weight to all text, struggle to capture these nuances, thereby compromising
             the accuracy and value of their analysis.""")

st.header(" ")
st.header("EarningsEdge.ai vs. Industry Standard")

col3, col4, col5 = st.columns([1, 1, 1])
with col3:
    st.image('earningsedge.jpg', width=235)
    st.write('Figure 1 - EarningsEdge.ai sentiment of sentence from Tesla\'s Q1 2023 earnings call')

with col4:
    st.image('finbert.JPG', width=235)
    st.write('Figure 2 - FinBert sentiment of sentence from Tesla\'s Q1 2023 earnings call')

with col5:
    st.image('nltk.png', width=235)
    st.write('Figure 3 - NLTK Vader sentiment of sentence from Tesla\'s Q1 2023 earnings call')

st.header(" ")
st.write("""
The comparison above demonstrates the sentiment analysis accuracy of three models—EarningsEdge.ai, FinBERT, and NLTK 
Vader—using a sample statement from Tesla's Q1 2023 earnings call. EarningsEdge.ai accurately predicted the sentiment, while 
FinBERT diverged and NLTK Vader partially aligned. This highlights the effectiveness and potential application of the
EarningsEdge.ai model.""")

st.header(" ")
st.subheader('EarningsEdge.ai Solution')
st.write("""
EarningsEdge.ai's sentiment model offers a specialized solution for the financial sector, incorporating
industry-specific understanding and the ability to prioritize key sentences for enhanced accuracy. By employing a
financial-specific lexicon, our model adeptly interprets sector-specific jargon, delivering nuanced and precise
sentiment analysis tailored for financial discourse.""")

st.header(" ")

col6, col7 = st.columns([1, 1])
with col6:
    st.image('industry.jpg', width=375)
    st.write("Figure 4 - EarningsEdge sentiment prediction of a sentence from Ford's 2022 Q4 earnings call")

with col7:
    st.image('earningsedgenegative.jpg', width=375)
    st.write("Figure 5 - EarningsEdge sentiment prediction of a sentence from GM's 2022 Q4 earnings call")


st.write("""
Figures 4 and 5 illustrate the EarningsEdge.ai model's tailored approach, analyzing sentences from Ford's and GM's Q4
2022 earnings calls. They exemplify its capacity to handle industry-specific language and prioritize pivotal information,
providing a nuanced and precise sentiment analysis for the automotive finance sector.
""")
st.header(" ")
st.subheader("EarningsEdge.ai Performance & Correlation Analysis of Tesla Stock")
st.image("teslasentiment.jpg", width=950)


st.write("""
The line chart depicts the relationship between sentiment analysis scores and the subsequent stock price difference for
Tesla following each earnings call. The sentiment analysis scores reflect the overall sentiment expressed during the
earnings calls, while the stock price difference represents the change in Tesla's stock price after the calls. By
examining the chart, we can observe the patterns and trends that emerge between sentiment scores and stock price
movements. This analysis provides insights into how changes in market sentiment, as captured by the sentiment
analysis model, potentially impact Tesla's stock price.
""")

st.header(" ")
col7, col8 = st.columns([2, 1])

with col7:
    st.image('heatmap.jpg')

with col8:
    st.write("""
    The sentiment analysis heat map visually represents the sentiment scores for each of the features presented in this
    case study. It uses color gradients to indicate the intensity or polarity of sentiment, with darker green colors
    typically representing positive sentiment and lighter green colors representing negative sentiment. Looking a the
     the heat map, you will see each feature mapped to another. For example, sentiment_value and 3MonthDiff have a 
     .48 sentiment, whereas sentiment_value and 1DayDiff have a .24 sentiment""")

st.header("Call to Action")
