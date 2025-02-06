# py-cosmetic-api ✨

### Esta API será usada para gerenciar produtos como maquiagem 💄, skincare 🧴, para cabelos 💇‍♀️, perfumes 🌸, entre outros.

## Como executar 🚀

1. Instale as dependências:

```bash
pip install -r requirements.txt
```

2. Inicie o servidor com o comando:

```bash
uvicorn main:app --reload
```

## Estrutura do Produto 🛍️

A API gerencia os seguintes atributos para cada produto:

| Produto     |                           |
|-------------|------------------------------------|
| **id**      | INT (chave primária)              |
| **name**    | VARCHAR                            |
| **brand**   | VARCHAR                            |
| **rate**    | INT (1-5)                          |
| **price**   | DECIMAL                            |
| **annotation** | TEXT                            |


- id: Um identificador único para o produto (chave primária).
- nome: Nome do produto.
- marca: Marca do produto.
- avaliacao: Avaliação do produto (1-5).
- preco: Preço do produto.
- comentario: Comentário adicional sobre o produto.

## Funcionalidades 📝

A API deve permitir as seguintes operações:

- **Visualizar todos os produtos**: 📋 Listar todos os produtos cadastrados.
- **Adicionar novo produto**: ➕ Criar um novo produto com os atributos mencionados.
- **Buscar produto por atributo**: 🔍 Realizar buscas por Tipo, Nome ou Marca.
- **Atualizar atributos**: 🛠️ Permitir pequenas correções ou atualizações nos atributos do produto.
- **Avaliar/reavaliar o produto**: 🌟 Adicionar ou atualizar a avaliação de um produto.
- **Apagar produto**: 🗑️ Excluir um produto que tenha sido cadastrado incorretamente ou por duplicidade.

## Endpoints 📡

1. **GET /produtos**: Retorna todos os produtos cadastrados.
2. **POST /produtos**: Adiciona um novo produto.
3. **GET /produtos/{atributo}**: Busca produtos por um atributo (Tipo, Nome, Marca).
4. **PUT /produtos/{id}**: Atualiza os atributos de um produto existente.
5. **POST /produtos/{id}/avaliacao**: Avalia ou reavalia um produto.
6. **DELETE /produtos/{id}**: Apaga um produto do cadastro.

---

