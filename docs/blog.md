# Funcionalidade: Blog

Esta seção descreve a aplicação de blog e sua API.

## Modelos

O aplicativo de blog inclui os seguintes modelos:

- **Post**: O modelo principal para as postagens do blog.
- **Category**: Para categorizar as postagens.
- **Tag**: Para marcar as postagens com palavras-chave.

## API

A API do blog fornece endpoints CRUD completos para gerenciar as postagens.

- `GET /api/blog/posts/`: Lista todas as postagens.
- `POST /api/blog/posts/`: Cria uma nova postagem (requer autenticação).
- `GET /api/blog/posts/{slug}/`: Recupera uma única postagem.
- `PATCH /api/blog/posts/{slug}/`: Atualiza uma postagem existente (requer ser o autor).
- `DELETE /api/blog/posts/{slug}/`: Deleta uma postagem existente (requer ser o autor).

## Integração com Produtos

Os posts do blog podem ser associados a produtos da loja, permitindo uma maior integração entre o conteúdo e o e-commerce.
