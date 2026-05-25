# Sistema de Locação de Veículos - Back-end

Projeto da avaliação A3 da unidade curricular Sistemas Distribuídos e Mobile,
ministrada pelo professor Antônio Leães na UniRitter.

Integrantes: Marcelo Duarte de Aguiar e Thiago Roncoli Brusch.

## Sobre o projeto

A aplicação é uma API REST que dá suporte a uma locadora de veículos: cadastro
de clientes, agências, frota, categorias de veículo, reservas, pagamentos,
seguros, adicionais, manutenções e multas. A modelagem nasceu de um diagrama de
classes que foi validado com o professor antes do início do desenvolvimento.

O foco do back-end foi cumprir o contrato da UC: construir um conjunto coerente
de microservices/apps em Django com persistência em Oracle, expostos via
Django Rest Framework, com versionamento amplo via Git.

## Stack

- Python 3.14
- Django 6.0
- Django Rest Framework 3.17
- python-decouple para gerenciamento de segredos
- oracledb (modo thin) como driver Oracle
- Oracle Autonomous Database hospedado na Oracle Cloud Infrastructure (região
  sa-saopaulo-1)

## Estrutura

O projeto segue uma organização por domínio. Cada classe do diagrama virou um
app Django independente dentro de `apps/`, com seus próprios `models.py`,
`serializer.py`, `views.py`, `urls.py` e `migrations/`.

```
apps/
  pessoa/               (classe abstrata)
  cliente/
  carteira_motorista/
  funcionario/
  agencia/
  categoria_veiculo/
  veiculo/
  adicional/
  seguro/
  reserva/
  pagamento/
  item_adicional/
  manutencao/
  multa/
locadoraApp/
  settings.py
  urls.py
manage.py
requirements.txt
.env.example
```

`locadoraApp/urls.py` centraliza um `DefaultRouter` do DRF que registra todos os
ViewSets, expondo-os sob o prefixo `/api/`. A app `pessoa` é abstrata e por
isso seu endpoint informativo fica em rota separada.

## Modelagem

São 14 classes no total. A herança usa o modelo abstrato `Pessoa` como base
para `Cliente` e `Funcionario`. As relações principais são:

- Cliente 1-1 CarteiraMotorista
- Agencia 1-* Veiculo
- Agencia 1-* Funcionario
- CategoriaVeiculo 1-* Veiculo
- Cliente 1-* Reserva
- Veiculo 1-* Reserva
- Reserva 1-1 Pagamento
- Reserva *-* Adicional (associativa: ItemAdicional, com `quantidade` própria)
- Veiculo 1-* Manutencao
- Reserva 1-* Multa

Todos os models possuem no mínimo quatro atributos e fazem uso de tipos
variados (`CharField`, `DateField`, `DecimalField`, `BooleanField`,
`PositiveIntegerField`, `TextField`, `ForeignKey`, `OneToOneField`).

Métodos de domínio relevantes foram implementados nos próprios models. Alguns
exemplos:

- `Cliente.verificarElegibilidadeLocacao()`
- `CarteiraMotorista.isValida()`
- `Veiculo.atualizarDisponibilidade()`
- `Reserva.calcularValorTotal()`, `confirmarReserva()`, `cancelarReserva()`
- `Pagamento.processarPagamento()`, `estornarPagamento()`
- `Manutencao.finalizarManutencao()`
- `Multa.registrarPagamento()`

## Banco de dados

A persistência roda em um Oracle Autonomous Transaction Processing (tier Always
Free) provisionado na OCI. A conexão é feita via `oracledb` em modo thin, usando
o wallet baixado do painel da OCI. O caminho do wallet e as credenciais ficam
fora do código, em `.env` (ignorado pelo `.gitignore`).

Trecho relevante de `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'OPTIONS': {
            'config_dir': config('TNS_ADMIN'),
            'wallet_location': config('TNS_ADMIN'),
            'wallet_password': config('DB_PASSWORD'),
        },
    }
}
```

## Como rodar localmente

1. Clonar o repositório e entrar na pasta:

   ```
   git clone https://github.com/anleaes/2026-1-SDM-Segunda-Noite-ZS-09
   cd 2026-1-SDM-Segunda-Noite-ZS-09
   ```

2. Criar um ambiente virtual (Miniconda, venv ou similar) e instalar as
   dependências:

   ```
   pip install -r requirements.txt
   ```

3. Extrair o wallet da Autonomous DB em um diretório local (por exemplo
   `C:\oracle\wallet_locadora`).

4. Copiar `.env.example` para `.env` e preencher as variáveis:

   ```
   SECRET_KEY=...
   DEBUG=True
   ALLOWED_HOSTS=127.0.0.1,localhost
   DB_NAME=locadoradb_high
   DB_USER=ADMIN
   DB_PASSWORD=...
   TNS_ADMIN=C:\oracle\wallet_locadora
   ```

5. Aplicar as migrações no Oracle e subir o servidor:

   ```
   python manage.py migrate
   python manage.py runserver
   ```

6. A API fica disponível em `http://127.0.0.1:8000/api/`.

## Endpoints

Catálogo principal exposto em `GET /api/`:

| Recurso              | Rota                            |
|----------------------|---------------------------------|
| Clientes             | `/api/clientes/`                |
| Carteiras de motorista | `/api/carteiras-motorista/`   |
| Funcionários         | `/api/funcionarios/`            |
| Agências             | `/api/agencias/`                |
| Categorias de veículo | `/api/categorias-veiculo/`     |
| Veículos             | `/api/veiculos/`                |
| Adicionais           | `/api/adicionais/`              |
| Seguros              | `/api/seguros/`                 |
| Reservas             | `/api/reservas/`                |
| Pagamentos           | `/api/pagamentos/`              |
| Itens adicionais     | `/api/itens-adicionais/`        |
| Manutenções          | `/api/manutencoes/`             |
| Multas               | `/api/multas/`                  |
| Informação Pessoa    | `/api/pessoa/`                  |

Cada recurso oferece o conjunto padrão de operações REST (GET coleção, GET
detalhe, POST, PUT, PATCH, DELETE) com validações de unicidade, integridade
referencial e relacionamentos OneToOne / unique_together quando aplicável.

## Fluxo de versionamento

O contrato da UC pede um trabalho intenso com Git. O histórico do repositório
reflete isso. Para cada uma das 14 classes foram criadas quatro branches
separadas — uma para o model, uma para o serializer, uma para a view e uma
para as urls — com pelo menos dois commits cada e merge via Pull Request na
`main`. Outras branches cobrem o setup inicial, a integração com Oracle e
ajustes pontuais. No total, mais de 70 Pull Requests foram abertos, revisados
e mergeados durante o desenvolvimento.

## Divisão de trabalho

Para coordenar a dupla, dividimos a modelagem em duas metades:

- Marcelo: Pessoa, Cliente, CarteiraMotorista, Funcionario, Agencia,
  CategoriaVeiculo, Veiculo, configuração inicial do projeto, integração com
  Oracle Cloud e ajustes da API root.
- Thiago: Adicional, Seguro, Reserva, Pagamento, ItemAdicional, Manutencao,
  Multa.

Cada um trabalhou em sua própria máquina, com pulls regulares para evitar
conflito, e ambos usaram o mesmo banco Oracle compartilhado.

## Observações finais

Os arquivos de migração da pasta `migrations/` foram versionados
intencionalmente. Eles refletem a evolução incremental do schema durante o
desenvolvimento e são necessários para que qualquer pessoa que clone o repo
consiga reconstruir o banco rodando `python manage.py migrate`.

O `.env` real fica de fora do versionamento. Para subir o ambiente é preciso
ter as credenciais da Autonomous DB e o wallet correspondente.

A próxima etapa do trabalho é o front-end em React Native, que vai consumir
estes endpoints.
