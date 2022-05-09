import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC6adb2f9231ae3987b6223061c52c2c90"
# Your Auth Token from twilio.com/console
auth_token  = "126f693fd0e2a0f66ad293b4dc54ab26"
client = Client(account_sid, auth_token)

lista_meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho"]

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f"{mes}.xlsx")
    if (tabela_vendas["Vendas"] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, "Vendedor"].values[0]
        vendas = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, "Vendas"].values[0]
        print(f"No mês de {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}")
        message = client.messages.create(
            to="+5521981959663",
            from_="+17472986590",
            body=f"No mês de {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}")
        print(message.sid)






