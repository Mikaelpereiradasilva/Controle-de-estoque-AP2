# Sistema de Controle de Estoque Escolar - Crede

Este projeto é um sistema de gerenciamento de estoque desenvolvido para a rede municipal de ensino (com foco inicial no município de Juazeiro do Norte). Ele conecta as escolas municipais à Crede, digitalizando e otimizando o controle de materiais para garantir transparência e eficiência no uso do dinheiro público.

## Objetivo do Projeto

Atualmente, o controle de estoque em muitas escolas públicas é feito de forma manuscrita, o que abre margem para erros de contagem, perda de produtos por vencimento e desvio de materiais. 

O objetivo principal deste sistema é **manter o estoque de materiais atualizado**, evitando desperdícios e desvios de verbas. Através da plataforma, é possível:
* Rastrear a entrada e saída de produtos (incluindo quem solicitou a retirada).
* Monitorar a validade dos itens.
* Agilizar o processo de compras por meio do envio de pesquisas de preço para aprovação da CREDE.

## Funcionalidades

O sistema é dividido em dois módulos principais, atendendo às necessidades de cada nível da administração:

### Módulo das Escolas (Colégios)
* **Entrada de produtos:** Registro detalhado dos materiais recebidos.
* **Saídas de produtos:** Controle de retirada com identificação do solicitante.
* **Sistema de Alertas:** Notificações automáticas para **estoque mínimo** e **produtos próximos ao vencimento**.
* **Solicitações à Crede:** Funcionalidade para encaminhar pesquisas de preços e solicitar a compra de novos materiais com o recurso destinado à escola.

### Módulo da CREDE
* **crede_autorizacao:** Análise das pesquisas de preço enviadas pelas escolas e indicação/autorização dos locais de compra.
* **crede_fiscalizacao:** Acesso em tempo real ao inventário de cada colégio da rede.
* **crede_login_e_cadastro:** Capacidade de entrar em credes já existentes e criar novas
* **crede_menus:** Apresentação das ações da crede
* **crede.json:** Armazenamento das credenciais das credes

## Benefícios Esperados

* **Para as Escolas:** Maior agilidade e resposta rápida nas futuras compras de materiais de uso diário.
* **Para a Crede:** Maior controle sobre o uso das verbas públicas, auditoria facilitada e garantia de um melhor investimento financeiro.
* **Para a Sociedade:** Transparência, redução de desperdícios e melhoria na infraestrutura de suporte à educação.


