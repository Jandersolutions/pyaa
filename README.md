<p align="center">
    <a href="https://github.com/paulocoutinhox/pyaa" target="_blank" rel="noopener noreferrer">
        <img width="250" src="extras/images/logo.png" alt="PyAA Logo">
    </a>
    <br>
    PyAA - Python Advanced Application
    <br>
</p>

O PyAA é uma poderosa aplicação de template open-source em Python + Django, projetada para construir aplicações web robustas com todas as funcionalidades essenciais já pré-construídas. Seja para um site, uma plataforma de e-commerce, ou uma aplicação SaaS, o PyAA tem tudo o que você precisa – de graça!

Este projeto foi refatorado para seguir os princípios da [Metodologia 12 Fatores](https://12factor.net/pt_br/), garantindo que a aplicação seja mais portátil, escalável e fácil de manter.

[![Build](https://github.com/paulocoutinhox/pyaa/actions/workflows/build.yml/badge.svg)](https://github.com/paulocoutinhox/pyaa/actions/workflows/build.yml)

[![codecov](https://codecov.io/gh/paulocoutinhox/pyaa/graph/badge.svg?token=KQ1H9SVD4Y)](https://codecov.io/gh/paulocoutinhox/pyaa)

## 🚀 Funcionalidades

- **Gerenciamento de Usuários**: Cadastro, login, gerenciamento de perfil, recuperação de conta, e ativação de conta configurável.
- **Sistema de Blog**: Uma aplicação de blog completa com API CRUD, categorias, tags e integração com outros módulos.
- **Integração de Produtos no Blog**: Associe produtos da loja diretamente nos posts do blog.
- **Gerenciamento de Assinaturas**: Gerencie assinaturas de usuários por créditos ou data de expiração.
- **Sistema de Créditos**: Suporte para venda e gerenciamento de créditos de usuário.
- **Sistema de Checkout**: Fluxo de pagamento completo para produtos e serviços.
- **Produtos Digitais**: Venda de produtos digitais com links de download seguros após a compra.
- **Sistema de Banners**: Gerencie banners com rastreamento de visualizações e cliques, além de relatórios detalhados no painel de administração.
- **Painel de Administração Completo**: Um dashboard de administração funcional para gerenciar a aplicação.
- **Relatórios Administrativos**: Sistema de relatórios abrangente com tabelas e gráficos interativos.
- **Sistema de Newsletter**: Gerenciamento de inscrições com funcionalidade de exportação em CSV.
- **Novo Design**: Tipografia inspirada no site do Ubuntu, com o tema "United" do Bootswatch e ícones Font Awesome.
- **Integração de E-mail**: Envio de e-mails transacionais.
- **Suporte a Recaptcha**: Aumente a segurança com a integração do Recaptcha.
- **Galeria de Imagens**: Gerencie uma galeria de imagens de forma eficiente.
- **Gerenciamento de Conteúdo Estático**: Organize e gerencie conteúdo estático em seu site.
- **Logs do Sistema**: Sistema de log abrangente com múltiplos níveis e categorização.
- **Suporte a Múltiplos Idiomas**: Lide facilmente com múltiplos idiomas.
- **Suporte a Múltiplas Moedas**: Processe pagamentos em diferentes moedas.
- **Integração com Stripe**: Gerenciamento de pagamentos de assinaturas e compras avulsas através do Stripe.
- **Fila de Tarefas em Background**: Alimentado por DjangoQ com suporte a workers para tarefas assíncronas.
- **Suporte a Docker**: Configurações Docker para a aplicação web e para tarefas agendadas (cron).
- **Alta Cobertura de Testes**: Mais de 50% de cobertura de testes, garantindo confiabilidade e robustez.

## 💻 Como Usar

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/paulocoutinhox/pyaa.git
    cd pyaa
    ```

2.  **Configure o Ambiente:**
    Crie um arquivo `.env` a partir do exemplo. Este arquivo conterá suas variáveis de ambiente locais.
    ```bash
    cp .env.example .env
    ```
    *Você pode customizar as variáveis no arquivo `.env` se necessário.*

3.  **Execute os comandos de setup:**
    ```bash
    make deps
    make setup
    make migrate
    make create-su
    make fixtures
    make run
    ```

## 📚 Documentação

- [API](docs/api.md)
- [Banco de Dados](docs/database.md)
- [Docker](docs/docker.md)
- [Ngrok](docs/ngrok.md)
- [Produção](docs/production.md)
- [Segurança](docs/security.md)
- [Stripe](docs/stripe.md)
- [Solução de Problemas](docs/troubleshooting.md)
- [WebApp](docs/webapp.md)
- [Cron](docs/cron.md)
- [Fila](docs/queue.md)
- [VSCode](docs/vscode.md)

## 🛡️ Licença

[MIT](http://opensource.org/licenses/MIT)

Copyright (c) 2024-2025, Paulo Coutinho
