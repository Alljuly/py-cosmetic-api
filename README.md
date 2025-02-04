# py-comestic-api

### Está api será usada para gerenciar produtos como maquiagem, skincare, para cabelos, perfumes e etc.

executar: 
pip install -r requirements.txt
uvicorn main:app --reload


Os produtos contém:
  - Produto
  - Nome
  - Marca
  - Avaliação 1-5 (De acordo o seu uso pessoal)
  - Preço
  - Comentário

Deve ser possivel:
  - Vizualizar todos os produtos.
  - Adicionar novo produto.
  - Buscar produto por atributo (Tipo, Nome, Marca).
  - Atualizar atributo para pequenas correções/atualizações.
  - Avaliar o produto e reavalia-lo.
  - Apagar um produto cadastrado errado (em caso de duplicatas por ex.). 
