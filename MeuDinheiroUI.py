import MeuDinheiroAPIs
from pathlib import Path

def main(name):
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # path_extrato_cartao_bradesco = (
    #     f"C:\\Users\\rafaelb1\\OneDrive\\Finanças\\extratos\\2025-03-12\\Bradesco_12032025_125331.xls")
    # path_extrato_cartao_XP=(
    #     "C:\\Users\\rafaelb1\\OneDrive\\Finanças\\extratos\\2025-03-12\\Fatura2025-04-10.csv")
    # path_extrato_cc_XP = (
    #     "C:\\Users\\rafaelb1\\OneDrive\\Finanças\\extratos\\2025-03-12\\extrato_de_10-02-2025_ate_12-03-2025.csv")
    # path_extrato_cc_inv_XP = (
    #     "~/Downloads/cc_inv_extrato_de_02-01-2026_ate_01-02-2026.xlsx")
    path_extrato_cartao_nubank = Path(
        "~/Downloads/Nubank_2026-02-10.csv")
    # path_extrato_cc_XP2 = (
    #     "C:\\Users\\rafaelb1\\OneDrive\\Finanças\\extratos\\2025-03-06\\extrato_de_04-02-2025_ate_06-03-2025.xlsx")

    # import_cartao_bradesco(path_extrato_cartao_bradesco)
    # import_cartao_XP(path_extrato_cartao_XP)
    # import_cc_XP(path_extrato_cc_XP)
    # import_cc_inv_XP(path_extrato_cc_inv_XP)
    MeuDinheiroAPIs.import_cartao_nubank(path_extrato_cartao_nubank)