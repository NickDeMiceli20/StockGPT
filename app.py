import streamlit as st
import openai
import numpy as np

openai.api_key = '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'

def summarize():
    with open('TSLA.txt', 'r') as f:
        contents = f.read()
    words = contents.split(" ")

    chunks = np.array_split(words, 6)

    summary_responses = []

    for chunk in chunks:
        sentences = ' '.join(list(chunk))

        prompt = f""" You are a writing expert in finance. You understand the importance of certain {sentences} and ultimately judge of whether to
             include them in your summary or not. If a sentence is not of importance to an investor then do not include it. You will only include infromation
             about finance and will leave out all other irrelevant information or remarks. Do not make any sentences
              up, use only the context from the text you are provided. You will break this summary down into concise paragraphs with relevant titles for each section. You will
              not end any sentences mid-sentece. If you run out of tokens, you delete the sentence. 
              Let's first understand the problem and then carry this out step by step. You will not include your process to carry this out you will only print
              out the summary results.
             """

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            temperature=0.3,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=1
        )

        response_text = response["choices"][0]["text"]
        summary_responses.append(response_text)

    full_summary = "".join(summary_responses)
    return full_summary

def analyze(full_summary):
    prompt = f"""
    You are an extremely successful finance professional. You will give a strong buy, buy, strong sell, sell, or hold rating
    in your report and why you are giving this rating. You never end your report mid sentence. Always make sure you include a last sentence in
    your report. You have a great understanding of the exact context in an earnings call that can sway
    a companies stock in a certain way. You take in a summary of a companies earnings call and create an analyst report based only off of this
    summary. You will only use the {full_summary} and no other data given as guidance in your reports. Format the report as if you were an analyst
    working for EarningsEdge. If you run out of information to say, then
    end the report. Do not include anything in your report that is not from the {full_summary} or any questions from analyst. 
    You will structure this as if an analyst is showing a report to its boss. Break it up into relevant sections with appropriate titles. Let's first understand the problem and then carry this out step by step. You will not include your process to carry this out yo uwill only print
    out the summary results.
    """
    response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            temperature=0,
            max_tokens=200,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=1
        )

    response_text = response["choices"][0]["text"]
    return response_text

st.image('logo-transp-sky.png', width=400)
st.subheader("Tesla\'s Q1 2023 Earnings Call EarningsEdge.ai Summarization")
st.write("""
Tesla reported record vehicle production and deliveries in Q1, as well as record energy storage volumes. Elon Musk highlighted the importance of pushing for higher volumes and a larger fleet, even at lower margins, in order to lay the groundwork for future profit through autonomy. The Cyber Truck is expected to have a delivery event in Q3, and Tesla is making progress on cost reduction and logistics. Megapac deployment reached nearly 4 gigawatt hours in Q1, and Tesla is investing heavily in its future plans, including Autonomy and AI enabled products. Pricing adjustments are actively managed by a subset of the leadership team, and Tesla Energy is expected to be bigger than Auto in terms of total gigawatt hours deployed. 4680 cells are meeting expectations, and the lithium refinery in Corpus Christi is expected to start commissioning portions of the facility by the end of the year.
Tesla discussed their progress on battery day, cathode production, and structural pack manufacturing during the earnings call. They have successfully demonstrated a lower process cost zero waste water precursor process at both lab and pilot scale and are on the detailed design phase for incorporating this technology into the front end of their Austin cathode facility. In Texas, production increased 50%, quarter over quarter, through yields increased 12% and Cato peak rate increased by 20%. The team accomplished a 25% reduction in Cogs over the quarter and they are on track to achieve steady state cost targets over the next twelve months. 
""")
st.write("""
The company also discussed their FSD take rates and their plans to open up new markets around the world. 
Tesla is focused on maximizing the volume of their fleet and monetizing it over its life cycle. This includes autonomous capabilities, which they believe can be achieved with their current hardware. They are also looking into heat pumps for homes and commercial offices. Pricing is adjusted daily based on real-time data, and Tesla looks at market share in terms of cars rather than EVs. They anticipate improved costs from suppliers and a crash in lithium prices. Finally, they are ramping up megapac projects and being selective about which ones to pursue. 
Tesla's CEO Elon Musk discussed the company's strategy for increasing its market share in the auto industry. He noted that Tesla has a unique strategic advantage due to its ability to sell cars at zero profit and still yield tremendous economics in the future through autonomy. He also highlighted the importance of investing in 2024 and 2025, using the cash generated from the sale of products today. Additionally, he mentioned that Tesla is not taking pricing actions to deliberately undermine competitors, but rather is focused on making sure people like their cars, can afford them, and are provided with improved service. Finally, he stated that Tesla is not seeing any growth pains that would lead them to change their direct business model. Overall, Tesla is focused on increasing its market share in the auto industry by leveraging its cost position, improving service, and investing in the future.
Tesla is not concerned with short-term financial performance, as they are focused on scaling their business in order to improve their cost structure and unlock potential future revenue streams. 
""")

st.write("""
Tesla is targeting a mid-20% gross margin for automotive and energy storage over the long term. They have already made pricing adjustments in the second half of the quarter, which will continue to lower the possible margin floor. Elon Musk also mentioned that Tesla is aiming for a delivery event for the Cybertruck at the end of Q3, although this could change. Additionally, Tesla expects energy storage to be bigger than automotive in terms of total gigawatt hours deployed. """)
st.write("""
Tesla's earnings call discussed the progress of their energy storage business, which saw a 50% increase in quarter-over-quarter production and a 360% increase year-over-year.  Elon Musk also discussed FSD take rates, noting that it is still in development and that pricing adjustments are being made to drive orders. He also mentioned Dojo and its potential to become a multi-hundred billion dollar business. Lastly, he discussed the ramp up of the Lathrop factory and Tesla's plans to expand into new markets. Overall, the call emphasizes short-term losses for long-term growth.""")
st.header(" ")
st.subheader("Tesla\'s Q1 2023 EarningsEdge.ai GPT Analysis")
st.write("""
Tesla's Q1 earnings call highlighted the company's progress in its energy storage business, with production increasing 50% quarter-over-quarter
and 360% year-over-year. Elon Musk discussed Tesla's strategy for increasing its market share in the auto industry, noting that they are not
taking pricing actions to deliberately undermine competitors, but rather are focused on making sure people like their cars, can afford them,
and are provided with improved service. Additionally, he mentioned that Tesla is targeting a mid-20% gross margin for automotive and energy storage over the long term, and that they have already made pricing adjustments in the second half of the quarter.
""")
st.header(" ")
st.write("""
Overall, Tesla is investing heavily in its future plans, including Autonomy and AI enabled products, and is actively managing pricing adjustments.
 The company is also ramping up megapac projects and being selective about which ones to pursue. With these investments, 
 Tesla is looking to maximize the volume of their fleet and monetize it over its life cycle. We believe that Tesla's focus 
 on long-term growth and cost reduction will pay off in the future, and we rate the stock as a 'Buy' with a confidence rating of 8/10.
""")

