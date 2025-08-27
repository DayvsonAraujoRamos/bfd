# cadastro = {"nome": "Lucas","idade": 25,"email": "lucas@email.com"}
# cliente = {"nome": "Amanda", "idade": 31}
# if not cliente.get("telefone"):
#     print("ok")
# livro = {"título": "1984", "autor": "George Orwell", "ano": 1949}
# # for chave in livro.keys():
# #     print(chave)
# # livro["disponivel"] = "True"
# # print(livro)
# print(livro.pop("ano"))
# print(livro)
#===============
# compras = {"uva": 3, "pera": 5, "banana": 2}
# print(compras.values())
# =========================
# frutas = {"maçã": 3, "banana": 5, "laranja": 2}
# for fruta in frutas.items():
#     # print(fruta)
#     if fruta[1] > 2:
#      print(fruta)
# ========================
# usuario = {"login": "joaosilva"}
# usuario["senha"] = "123456"
# print(usuario)
# ==============
# capitais = {"SP": "São Paulo", "RJ": "Rio de Janeiro", "MG": "Belo Horizonte"} 
# for capital in capitais.items():
#         print(f"A capital de {capital[0]} é {capital[1]}")
produto = {"nome": "Teclado", "estoque": 15}
produto["estoque"] += 10
print(produto)
 