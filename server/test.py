from langchain.agents.agent_toolkits import create_python_agent
from langchain.tools.python.tool import PythonREPLTool
from langchain.python import PythonREPL
from langchain.llms.openai import OpenAI
from langchain.agents.agent_types import AgentType
from langchain.chat_models import ChatOpenAI
from langchain.experimental.plan_and_execute import (
    PlanAndExecute,
    load_agent_executor,
    load_chat_planner,
)
from langchain import SerpAPIWrapper
from langchain.agents.tools import Tool
from langchain import LLMMathChain


def read_csv_and_concatenate(filename):
    result = ""
    with open(filename, "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            result += " ".join(row) + "\n"
    return result


agent_executor = create_python_agent(
    llm=ChatOpenAI(temperature=0, model="gpt-4"),
    tool=PythonREPLTool(),
    verbose=True,
    agent_type=AgentType.OPENAI_FUNCTIONS,
    agent_executor_kwargs={"handle_parsing_errors": True},
)

agent_executor.run(
    f"""Parse and understand the tabular data in the CSV file at https://doc-0o-5c-sheets.googleusercontent.com/export/tki1je60si8g7pe1pg0udl5fuc/a61jeb4e2q377qb6fe8da91b4s/1689452985000/117949082269606279369/117949082269606279369/1L2yoSLFiw_XuD-EwL5CR4XtEDisv9Swnum2B6dBaVmM?format=csv&id=1L2yoSLFiw_XuD-EwL5CR4XtEDisv9Swnum2B6dBaVmM&gid=94256002&dat=AIZXBe4hL5qgKCkJgmcCffrbRnN6igt2CkjG0LfFZDVLtuk1QrHDbI8xhT_ulSfxH3895Sh12ZNQjq2iKdMG3k-KafZStE_yv2YPSOibGtEH9W7Ws8xh2lVYPQBxL2fnHGyFY6nlA6g6WYyxBNoCFmVhuYxpMUSkvK82wzvEv-obribTxkE-QF4zN5NjYekV4ySKF3XtqaFezjlhh1XFcw-YcasVItd1k4dqd8-r4bAKmoc93xcxma-PJw8MPBHs1mmPZebO9Mi6M5MQuUdI7vK8L4C3twwxTs5mFUyf8o4EwzZ04NHdtk_824fhitCToEyoF6R-iMtbWhfXMvRneQOcPXYJjtTZeiSAGH5trd_0w4dEqm8rotGsvy0nfTkUfSKigRkIAhEnjt3qxeLbRdH2aI7l3bJgOe3xcuVH7nkA38R2VEr1IGTkuvcyBtRkf83SIm6Hm8-AISQxQjgVqBiV1Gc66RM7Lq-ji60HdjH1kF86hg8_xScyjNlWoUrfsK5XGPMXs3hAL4WR7ghMEanOZEsR8_scNRh0X5ldaIJli9Fyz_87XpG6sFp3l8-d6l_Dtrl5ZDqImWIQzbewZLGPyN0jfkP7lRoloVInLfq5qfwbi0w5xCmQxDAtpEshZqLMV4tuZIlUOz7tRGjNb01H7BWoovi20ns-mTOb3VzWmEskA0XV0T855pEB7q-G8f9dPqz2jdsInrfUD3IlHXx72bdzyAov2Q-abceCmYG0g1JDWfWfOLCFhmFMguC6F5ispTA1CFcJ3PqbntNAyb1m2zSTiFGol1p56SOMmWwejvb8mKki1K1oxiJU-Wa3vxPNHoFcSsVIrWK4AFFoDIJqlc-oMspa1NQQKnf_bfpZXthWMjp4zcKWvnqfjrS00S-078wnEtsNYHi0Y93dmLr8UHGOUOHY_G2d5QWQOKOeEM69tQUJtMuiZpasUWJ7ZeRzG6l2B8onJJlOxaXweqBW2fLvyoAgLjJ1CLUt3XOjCf0M9u_D0jLwPBDW1KcltFBu3MoRwBHig8VtfO_8Y8Q

	Decide what the best model is to predict housing prices based on the data.
	
	Train a classification machine learning model to predict housing prices based on the data
"""
)
