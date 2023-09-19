#1 - Calculadora de Idade com Tratamento de Data de Nascimento:
# Peça ao usuário para inserir sua data de nascimento no formato "dd/mm/aaaa".
# Utilize try, except para capturar erros de entrada e calcular a idade da pessoa.
# Em seguida, use um bloco else para exibir a idade calculada e um bloco finally
# para agradecer ao usuÃ¡rio por usar a calculadora.

#
# from datetime import datetime
#
# class DataInvalidaError(ValueError):
#     ...
# now = datetime.now()
# while True:
#     try:
#         data_nascimento = input("Digite a data de nascimento no formato dd/mm/yyyy: ")
#         data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
#         if data_nascimento > now:
#             raise DataInvalidaError("A data inserida é maior que a data de hoje.")
#     except DataInvalidaError:
#         print(DataInvalidaError)
#     except ValueError:
#         print("Data inválida. Atente-se ao formato dd/dd/yyyy")
#         print("tente novamente")
#         print()
#     except KeyboardInterrupt:
#         print("Não to afim")
#     else:
#         idade = (datetime.now() - data_nascimento).days // 365
#         print(f"Sua idade é {idade}")
#     # finally:
#
#
# print("Obrigado por utilizar a calculadora")



