# This is a sample Python script.
import pandas as pd
from datetime import datetime

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def import_cartao_bradesco(path_extrato_excel):

    df = pd.read_excel(path_extrato_excel, skiprows=10 )



    final_line = 0
    for i in range(0,len(df.index)):
        if str(df.iloc[i]).find('Total')>0:
            final_line = i
            break
    final_line = final_line-1

    df = df.iloc[:final_line]
    df["Data"] = df["Data"] + f"/{2025}"  # Transforma "13/12" em "13/12/2024"
    df["Data"] = pd.to_datetime(df["Data"], format="%d/%m/%Y")

    datas = df.iloc[:,0]
    desc =  df.iloc[:,1]
    val = df.iloc[:,4]

    df_out = pd.DataFrame(data=None, columns=['Data', 'Valor', 'Descrição'])
    # Atribuindo os valores das colunas diretamente ao df_out
    df_out["Data"] = datas.values
    df_out["Valor"] = val.values
    df_out["Descrição"] = desc.values
    df_out.set_index('Data')

    # df_out.to_excel(path_extrato_excel.replace('.xls','-exportMeuDinheiro.xlsx'),index=False, index_label="")
    df_out.to_csv(path_extrato_excel.replace('.xls','-exportMeuDinheiro.csv'))

# Função para limpar e converter os valores
def converter_moeda(valor):
    if isinstance(valor, str):  # Verifica se é string
        valor = valor.replace("R$ ", "").replace(".", "").replace(",", ".")  # Remove "R$ ", remove milhar e troca vírgula por ponto
    return float(valor)

def import_cartao_XP(path_extrato_csv):

    df = pd.read_csv(path_extrato_csv, delimiter=';' )




    df["Data"] = pd.to_datetime(df["Data"], format="%d/%m/%Y")

    datas = df.iloc[:,0]
    desc =  df.iloc[:,1]
    val = df.iloc[:,3].apply(converter_moeda)
    print(datas)
    print(desc)
    print(val)

    df_out = pd.DataFrame(data=None, columns=['Data', 'Valor', 'Descrição'])
    # Atribuindo os valores das colunas diretamente ao df_out
    df_out["Data"] = datas.values
    df_out["Valor"] = val.values
    df_out["Descrição"] = desc.values
    df_out.set_index('Data')

    # df_out.to_excel(path_extrato_excel.replace('.xls','-exportMeuDinheiro.xlsx'),index=False, index_label="")
    df_out.to_csv(path_extrato_csv.replace('.csv','-exportMeuDinheiro.csv'))


def main(name):
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    path_extrato_cartao_bradesco = (f"C:\\Users\\rafaelb1\\OneDrive\\Finanças\\extratos\\2025-02-04\\Cartão Bradesco\\"
                                    f"Cartao_Bradesco_242025_10329 PM-fev.xls")
    path_extrato_cartao_XP=("C:\\Users\\rafaelb1\\OneDrive\\Finanças\\extratos\\2025-02-04\\Cartão XP\\"
                            "Fatura2025-02-10.csv")
    # import_cartao_bradesco(path_extrato_cartao_bradesco)
    import_cartao_XP(path_extrato_cartao_XP)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
