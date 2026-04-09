import MeuDinheiroAPIs
from pathlib import Path

def main(name):
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # path_extrato_cartao_bradesco = Path(
    #     f"~/Downloads/Bradesco_12032025_125331.xls")
    # path_extrato_cartao_XP= Path(
    #     "~/Downloads/Fatura2026-03-25.csv")
    # path_extrato_cc_XP = Path(
    #     "~/Downloads/extrato_de_10-02-2025_ate_12-03-2025.csv")
    path_extrato_cc_inv_XP = Path(
         "~/Downloads/cc_inv_extrato_de_10-03-2026_ate_09-04-2026.xlsx")
    # path_extrato_cartao_nubank = Path(
    #     "~/Downloads/Nubank_2026-04-10.csv")
    # path_extrato_cc_XP2 = Path(
    #     "~/Downloads/extrato_de_04-02-2025_ate_06-03-2025.xlsx")





    # MeuDinheiroAPIs.import_cartao_bradesco(path_extrato_cartao_bradesco)
    # MeuDinheiroAPIs.import_cartao_XP(path_extrato_cartao_XP)
    # MeuDinheiroAPIs.import_cc_XP(path_extrato_cc_XP)
    MeuDinheiroAPIs.import_cc_inv_XP(path_extrato_cc_inv_XP)
    # MeuDinheiroAPIs.import_cartao_nubank(path_extrato_cartao_nubank)