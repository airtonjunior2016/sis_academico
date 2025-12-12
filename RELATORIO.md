📘 RELATÓRIO TÉCNICO – SISTEMA ACADÊMICO (CLI + SQLite)
1. Introdução

O presente relatório descreve o desenvolvimento de um Sistema Acadêmico implementado em Python, com interface em linha de comando (CLI) e persistência de dados utilizando o banco de dados SQLite.
O objetivo principal do projeto é demonstrar conceitos de orientação a objetos, arquitetura modular, persistência, validação de regras de negócio e boas práticas de programação.

O sistema permite gerenciar cursos, turmas, alunos, matrículas, notas, frequência e cálculo de CR (Coeficiente de Rendimento), oferecendo assim uma solução completa e funcional para gerenciamento acadêmico básico.

2. Objetivos do Sistema
2.1 Objetivo Geral

Desenvolver um sistema acadêmico simples, robusto e modular que permita o cadastro e controle de informações essenciais ao ambiente educacional.

2.2 Objetivos Específicos

Criar uma solução baseada em Python + SQLite.

Implementar um menu interativo para execução de operações.

Utilizar classes e dataclasses para modelagem do domínio.

Garantir validações como:

pré-requisitos

limite de vagas

conflito de horários

Registrar notas e frequência dos alunos matriculados.

Gerar histórico acadêmico e cálculo do CR.

3. Tecnologias Utilizadas

Python 3.x

SQLite (sqlite3)

JSON (para pré-requisitos)

Dataclasses

Arquitetura procedural + orientada a objetos

4. Arquitetura do Sistema

O sistema é dividido em quatro blocos principais:

4.1 Camada de Banco de Dados

Responsável pela criação e manutenção das tabelas:

cursos

turmas

alunos

matriculas

Realiza operações CRUD e consultas para validações.

4.2 Modelos (Classes)

Representados via dataclasses:

Curso

Turma

Aluno

Matricula

Todas herdando de EntidadeBase, que fornece um __repr__ automático.

4.3 Serviços (Regras de Negócio)

Funções que implementam:

Matrícula com validações

Registro de notas e frequência

Busca de entidades

Relatório e cálculo de CR

4.4 Interface (CLI)

Menu interativo com todas as opções da aplicação.


5. Funcionalidades Implementadas
5.1 Cursos

Cadastro, edição e exclusão

Pré-requisitos usando JSON

Listagem

5.2 Turmas

Cadastro, edição e exclusão

Controle de vagas

Checagem de conflito de horários

Listagem

5.3 Alunos

Cadastro, edição e exclusão

Listagem

5.4 Matrículas

Verificação de pré-requisitos

Verificação de vagas disponíveis

Verificação de choque de horário

Salvamento da matrícula

5.5 Notas e Frequência

Registro de nota final

Registro de frequência

5.6 Relatórios

Histórico completo do aluno

Cálculo do CR com base na média das notas

6. Menu Principal
=== MENU DO SISTEMA ACADÊMICO ===
1. Adicionar curso
2. Adicionar turma
3. Adicionar aluno
4. Matricular aluno
5. Registrar nota
6. Registrar frequência
7. Histórico do aluno
8. Editar curso
9. Excluir curso
10. Editar turma
11. Excluir turma
12. Excluir aluno
14. Listar cursos
15. Listar turmas
16. Listar alunos
17. Calcular CR (aluno)
0. Sair

7. Regras de Negócio Importantes

Pré-requisitos: O aluno só pode se matricular se já tiver concluído com nota ≥ 6 todos os cursos exigidos.

Conflito de horário: Não é permitido matricular um aluno em duas turmas com o mesmo horário.

Limite de vagas: A matrícula só ocorre se vagões disponíveis.

CR: Média aritmética das notas registradas.

8. Execução do Sistema

Instale Python 3.x

Execute:

python3 sistema_academico.py


O banco gestor_academico.db será criado automaticamente.

9. Conclusão

O sistema acadêmico desenvolvido cumpre todos os requisitos propostos, proporcionando um ambiente robusto e funcional para cadastro, controle e consulta de dados educacionais.
Além disso, demonstra de forma prática conceitos importantes de:

orientação a objetos

persistência de dados

regras de negócio

modularização

encapsulamento