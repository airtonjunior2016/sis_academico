📚 Sistema Acadêmico – Relatório Técnico

📝 1. Introdução

Este projeto consiste no desenvolvimento de um Sistema Acadêmico em Python, executado via interface de linha de comando (CLI), com foco em boas práticas de programação orientada a objetos, modularização, persistência de dados e validações robustas.
O sistema permite gerenciar cursos, turmas, alunos, matrículas, notas, frequência e cálculo de CR.

🎯 2. Objetivos do Sistema

Organizar dados acadêmicos de forma estruturada.

Aplicar princípios de POO, como encapsulamento, herança e métodos especiais.

Utilizar persistência em SQLite para garantir armazenamento seguro dos registros.

Disponibilizar funções essenciais para operações acadêmicas reais:

Cadastro e edição de entidades

Matrícula com controle de vagas

Detecção de conflitos

Registro de notas e frequência

Histórico acadêmico

Cálculo de Coeficiente de Rendimento (CR)

🧩 3. Arquitetura Geral

O sistema é dividido em camadas lógicas:

🔸 Entidades (Modelos)

Implementadas com @dataclass, representando cada elemento do domínio acadêmico:

Curso

Turma

Aluno

Matricula

Todas herdam de EntidadeBase, que fornece métodos especiais e padronização.

🔸 Persistência

Banco: SQLite

Acesso via módulo interno (DAO)

Tabelas criadas automaticamente no primeiro uso

🔸 Camada de Lógica (Serviços)

Responsável por:

Validações

Regras de negócio

Controle de vagas

Pré-requisitos

Registro de notas e frequência

Cálculo de CR

🔸 Interface CLI

Menu textual simples e organizado, permitindo navegação rápida.

📋 4. Funcionalidades do Sistema

O menu oferece as seguintes operações:

Nº	Função
1	Adicionar curso
2	Adicionar turma
3	Adicionar aluno
4	Matricular aluno
5	Registrar nota
6	Registrar frequência
7	Histórico do aluno
8	Editar curso
9	Excluir curso
10	Editar turma
11	Excluir turma
12	Editar aluno
13	Excluir aluno
14	Listar cursos
15	Listar turmas
16	Listar alunos
17	Calcular CR
0	Sair
🧪 5. Tratamento de Erros e Validações

O sistema valida:

Pré-requisitos antes da matrícula

Choque de horário entre turmas

Limite máximo de vagas

Matrícula duplicada

Inserção de notas e frequência válidas

Exclusão segura sem corromper registros

🔢 6. Cálculo do Coeficiente de Rendimento (CR)

O CR do aluno é calculado com base nas notas finais das disciplinas concluídas, aplicando:

CR = soma(notas) / quantidade_de_disciplinas


O valor é exibido com duas casas decimais.

🖥️ 7. Tecnologias Utilizadas

Python 3.x

SQLite3

Dataclasses

JSON (para pré-requisitos)

Estrutura CLI

📦 8. Como Executar
python sistema_academico.py


O sistema cria automaticamente o banco academico.db se não existir.

🧱 9. Estrutura de Pastas (sugerida)
/sistema_academico
│── sistema_academico.py
│── database.py
│── models/
│     ├── curso.py
│     ├── turma.py
│     ├── aluno.py
│     └── matricula.py
│── README.md
│── RELATORIO.md
│── academico.db

🏁 10. Conclusão

O Sistema Acadêmico demonstra:

Aplicação prática de POO

Projeto organizado e modular

Persistência confiável com SQLite

Operações acadêmicas completas e robustas
