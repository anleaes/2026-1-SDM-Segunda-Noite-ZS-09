# Distribuição de tarefas - Front-end React Native

Documento interno do grupo para organizar a entrega do front-end mobile
prevista para 01/06/2026.

Integrantes: Marcelo Duarte de Aguiar e Thiago Roncoli Brusch.

Data do combinado: 25/05/2026.

## Regra geral

A divisão segue o mesmo critério usado no back-end: cada um cuida das telas
referentes às classes que implementou no Django. Isso evita conflitos no Git
e mantém quem conhece a regra de negócio responsável pela interface dela.

## O que cabe a cada um

### Marcelo

- Tela inicial / navegação principal do app
- CRUD de Cliente
- CRUD de CarteiraMotorista
- CRUD de Funcionario
- CRUD de Agencia
- CRUD de CategoriaVeiculo
- CRUD de Veiculo
- Tela informativa de Pessoa (estrutura abstrata)

### Thiago

- CRUD de Adicional
- CRUD de Seguro
- CRUD de Reserva
- CRUD de Pagamento
- CRUD de ItemAdicional
- CRUD de Manutencao
- CRUD de Multa

## Como combinamos trabalhar

- Cada tela vira uma branch separada no repositório do front (segue a mesma
  ideia do back: branch por entrega + pelo menos um commit e Pull Request por
  branch).
- Cada um faz seus próprios pushes e Pull Requests, sem commitar direto na
  main.
- Pulls regulares na main antes de começar cada tela para evitar conflito.
- Conversas e dúvidas via WhatsApp do grupo da dupla.
- Em caso de bloqueio em algo da metade do outro, conversa antes de mexer.

## Padrões mínimos que vamos seguir

- Cada tela consome o endpoint correspondente do back já publicado.
- Listagem, detalhe, criação e edição quando fizer sentido pra entidade.
- Layout simples e funcional (foco é cumprir o requisito, não capricho
  visual).
- Componentes reutilizáveis (input, botão, card de lista) ficam em pasta
  comum para que os dois aproveitem.

## Itens compartilhados

Algumas tarefas ficam fora da divisão por entidade e podem ser feitas por
qualquer um dos dois (combinar antes para não duplicar):

- Setup inicial do projeto React Native
- Configuração da base URL da API e cliente HTTP
- Componentes reutilizáveis (input, botão, card)
- Tema de cores e estilos globais
- README do repositório de front-end
