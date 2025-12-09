from langchain_core.prompts import PromptTemplate
from src.logger import logging

router_template="""
    You are an expert router for a Fraud Detection RAG system.
    Analyze the user's input.
    {query}
"""

template = PromptTemplate(
    template=router_template,
    input_variables=['query']
)

logging.info('saving router template')
template.save('router_template.json')