# 📚 Sistema Acadêmico (SisAcademico)

> **Relatório Técnico – Sistema de Gestão Acadêmica**
> **Disciplina:** Programação Orientada a Objetos
> **Autores:** Airton Junior, Francisco Eduardo

---

## 📖 Introdução

O presente projeto tem como objetivo o desenvolvimento de um **Sistema de Gestão Acadêmica (SisAcademico)**, uma aplicação desenvolvida para automatizar e organizar os processos fundamentais de uma instituição de ensino.

A gestão manual de matrículas, turmas e notas é propensa a falhas humanas, como conflitos de horários ou matrículas indevidas. Este software visa mitigar esses erros por meio de um **sistema robusto de validação de dados**, utilizando a linguagem **Python** e persistência em **banco de dados relacional (SQLite)**.

O foco do desenvolvimento não se limita às operações básicas de cadastro (CRUD), mas prioriza a **integridade referencial** e a **aplicação rigorosa das regras de negócio acadêmicas**.

---

## 🎯 Objetivos

### Objetivo Geral

Desenvolver uma aplicação em linha de comandos (**CLI**) que permita o controle completo do ciclo de vida acadêmico, desde a criação de cursos até a emissão de históricos escolares.

### Objetivos Específicos

* Implementar persistência de dados eficiente utilizando **SQLite**;
* Aplicar conceitos de **Programação Orientada a Objetos (POO)** na modelagem das entidades;
* Desenvolver algoritmos de validação para impedir matrículas inválidas:

  * Conflitos de horário;
  * Falta de pré-requisitos;
  * Limite de vagas excedido;
* Gerar relatórios de desempenho acadêmico, incluindo o **Cálculo do Coeficiente de Rendimento (CR)**.

---

## 🛠️ Tecnologias e Arquitetura

### Ferramentas Utilizadas

* **Linguagem:** Python 3.x
  (Escolhida pela legibilidade, robustez e suporte nativo ao SQLite)
* **Banco de Dados:** SQLite3
  (Banco de dados serverless, leve e ideal para aplicações locais)

### Bibliotecas Auxiliares

* `dataclasses` – Redução de boilerplate na criação de objetos;
* `json` – Serialização de estruturas complexas (listas) para armazenamento em banco relacional.

---

## 🧱 Arquitetura de Software

O sistema adota uma **arquitetura modular implícita**, organizada em três camadas lógicas:

* **Modelo (Models)**
  Representado pelas *dataclasses* (`Curso`, `Turma`, `Aluno`), respons
