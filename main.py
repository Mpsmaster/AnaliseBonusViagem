import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "insert here"
# Your Auth Token from twilio.com/console
auth_token  = "insert here"
client = Client(account_sid, auth_token)

lista_meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho"]

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f"{mes}.xlsx")
    if (tabela_vendas["Vendas"] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, "Vendedor"].values[0]
        vendas = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, "Vendas"].values[0]
        print(f"No mês de {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}")
        message = client.messages.create(
            to="+55000000000",
            from_="insert here",
            body=f"No mês de {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}")
        print(message.sid)






