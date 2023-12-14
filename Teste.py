# Teste data

from Classe import Data

try:
    Calendario = Data(13, 12, 2023)
except ValueError as e:
    print(f"Erro ao criar a Data! {e}")
    Calendario = None

# Exibição do meu calendário
if Calendario is not None:
    print('\n\t\t\t ---- Data ----')
    print(Calendario)
else:
    print("A Data é inválida.")


