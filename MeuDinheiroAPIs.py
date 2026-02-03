# This is a sample Python script.
import pandas as pd
from datetime import datetime
from pathlib import Path

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

BASE_DIR = Path(__file__).resolve().parent
TESTDB_DIR = BASE_DIR / "testDB"

def import_cartao_bradesco(path_extrato_excel:Path):

    df = pd.read_excel(path_extrato_excel, skiprows=10 )



    final_line = 0
    for i in range(0,len(df.index)):
        if str(df.iloc[i]).find('Total')>0:
            final_line = i
            break
    # final_line = final_line-1

    df = df.iloc[:final_line]
    df["Data"] = df["Data"] + f"/{2025}"  # Transforma "13/12" em "13/12/2024"
    df["Data"] = pd.to_datetime(df["Data"], format="%d/%m/%Y")
    

    
    df.iloc[:, 4] = df.iloc[:, 4].apply(lambda x: str(x).replace(",", "."))


    df['Valor(R$)'] = df['Valor(R$)'].astype(float)
    datas = df.iloc[:,0]
    desc =  df.iloc[:,1]
    val = df.iloc[:, 4]



    df_out = pd.DataFrame(data=None, columns=['Data', 'Valor', 'Descrição'])
    # Atribuindo os valores das colunas diretamente ao df_out
    df_out["Data"] = datas.values
    df_out["Valor"] = -val.values
    df_out["Descrição"] = desc.values
    df_out.set_index('Data')

    # df_out.to_excel(path_extrato_excel.replace('.xls','-exportMeuDinheiro.xlsx'),index=False, index_label="")
    output_file_name = path_extrato_excel.with_name(path_extrato_excel.stem + '-exportMeuDinheiro.csv')
    df_out.to_csv(output_file_name,index=False)

# Função para limpar e converter os valores
def converter_moeda(valor):
    if isinstance(valor, str):  # Verifica se é string
        valor = valor.replace("R$ ", "").replace(".", "").replace(",", ".")  # Remove "R$ ", remove milhar e troca vírgula por ponto
    return float(valor)

def converter_data(valor):
    if isinstance(valor, str):  # Verifica se é string
        valor = valor[0:8]
        # valor =pd.to_datetime(valor, format="%d/%m/%Y")
    return valor#pd.to_datetime(valor, format="%d/%m/%Y")

def import_cartao_XP(path_extrato_csv:Path):

    df = pd.read_csv(path_extrato_csv, delimiter=';' )




    # df["Data"] = pd.to_datetime(df["Data"], format="%d/%m/%Y")

    datas = df.iloc[:,0]
    desc =  df.iloc[:,1]
    val = df.iloc[:,3].apply(converter_moeda)
    # print(datas)
    # print(desc)
    # print(val)

    df_out = pd.DataFrame(data=None, columns=['Data', 'Valor', 'Descrição'])
    # Atribuindo os valores das colunas diretamente ao df_out
    df_out["Data"] = datas.values
    df_out["Valor"] = -1 * val.values
    df_out["Descrição"] = desc.values
    df_out.set_index('Data')

    # df_out.to_excel(path_extrato_excel.replace('.xls','-exportMeuDinheiro.xlsx'),index=False, index_label="")
    
    

    output_file_name = path_extrato_csv.with_name(path_extrato_csv.stem + '-exportMeuDinheiro.csv')
    df_out.to_csv(output_file_name,index=False)


def import_cartao_nubank(path_extrato_csv:Path):

    df = pd.read_csv(path_extrato_csv, delimiter=',' )




    

    datas = df.iloc[:,0]

    datas = pd.to_datetime(datas, format="%Y-%m-%d")
    
    # print(datas)
    # exit()
    
    desc =  df.iloc[:,1]
    val = df.iloc[:,2].apply(converter_moeda)
    # print(datas)
    # print(desc)
    # print(val)

    df_out = pd.DataFrame(data=None, columns=['Data', 'Valor', 'Descrição'])
    # Atribuindo os valores das colunas diretamente ao df_out
    df_out["Data"] = datas.values
    

    df_out["Valor"] = -1 * val.values
    df_out["Descrição"] = desc.values
    df_out.set_index('Data')

    # df_out.to_excel(path_extrato_excel.replace('.xls','-exportMeuDinheiro.xlsx'),index=False, index_label="")



    output_file_name = path_extrato_csv.with_name(path_extrato_csv.stem + '-exportMeuDinheiro.csv')
    df_out.to_csv(output_file_name,index=False)

def import_cc_XP(path_extrato_csv:Path):

    df = pd.read_csv(path_extrato_csv, delimiter=';' )
    datas = df.iloc[:, 0]
    datas = datas.apply(converter_data)

    # datas = pd.to_datetime(datas, format="%d/%m/%Y")

    # df["Data"] = pd.to_datetime(df["Data"], format="%d/%m/%Y")


    desc =  df.iloc[:,1]
    val = df.iloc[:,2].apply(converter_moeda)
    # print(datas)
    # print(desc)
    # print(val)

    df_out = pd.DataFrame(data=None, columns=['Data', 'Valor', 'Descrição'])
    # Atribuindo os valores das colunas diretamente ao df_out
    df_out["Data"] = datas.values
    df_out["Valor"] = val.values
    df_out["Descrição"] = desc.values
    df_out.set_index('Data')

    # df_out.to_excel(path_extrato_excel.replace('.xls','-exportMeuDinheiro.xlsx'),index=False, index_label="")
    

    output_file_name = path_extrato_csv.with_name(path_extrato_csv.stem + '-exportMeuDinheiro.csv')
    df_out.to_csv(output_file_name,index=False)


def import_cc_inv_XP(path_extrato_excel:Path):

    df = pd.read_excel(path_extrato_excel, skiprows=13 )




    final_line = 0
    for i in range(0,len(df.index)):
        cel = str(df.iloc[i,2])
        if cel == 'nan':
            final_line = i
            break
    final_line = final_line

    df = df.iloc[:final_line]

    datas = df.iloc[:,2]
    desc =  df.iloc[:,3]
    val = df.iloc[:,5]

    df_out = pd.DataFrame(data=None, columns=['Data', 'Valor', 'Descrição'])
    # Atribuindo os valores das colunas diretamente ao df_out
    df_out["Data"] = datas.values
    df_out["Valor"] = val.values
    df_out["Descrição"] = desc.values
    df_out.set_index('Data')

    # df_out.to_excel(path_extrato_excel.replace('.xls','-exportMeuDinheiro.xlsx'),index=False, index_label="")


    output_file_name = path_extrato_excel.with_name(path_extrato_excel.stem + '-exportMeuDinheiro.csv')
    df_out.to_csv(output_file_name,index=False)


if __name__ == '__main__':
    
    path_extrato_cartao_bradesco = (
         TESTDB_DIR / "CartaoBradesco.xls")
    path_extrato_cartao_XP=(
        TESTDB_DIR / "CartaoXP.csv")
    path_extrato_cc_XP = (
        TESTDB_DIR / "extrato_cc_xp.csv")
    path_extrato_cc_inv_XP = (
        TESTDB_DIR / "extrato_cc_xp_inv.xlsx")
    path_extrato_cartao_nubank = (
       TESTDB_DIR / "CartaoNubank.csv")    

    import_cartao_bradesco(path_extrato_cartao_bradesco)
    import_cartao_XP(path_extrato_cartao_XP)
    import_cc_XP(path_extrato_cc_XP)
    import_cc_inv_XP(path_extrato_cc_inv_XP)
    import_cartao_nubank(path_extrato_cartao_nubank)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
