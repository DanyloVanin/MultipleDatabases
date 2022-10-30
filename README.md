# Multiple Databases

## Description

Comparing different databases used for one purpose:
- MongoDB (document)
- PostgreSQL (relational)
- Neo4j (graph)

## Task

Візьмемо приклад HR системи, що має опрацювати резюме.

Для цього створимо сутність користувач (логін, пароль) і його резюме (стандартні поля). 

Напишіть застосування яке збереже дані сутності в реляційній, документній та графовій базах даних.

**Обов'язкові умови:**

1. [x] мають бути зв'язки one to many
2. [x] мають бути зв'язки many to many
3. [x] мають бути різні запити
4. [x] забрати рюзюме (get resume by user)
5. [x] забрати всі хоббі які існують в резюме (get all languages from resume)
6. [x] забрати всі міста, що зустрічаються в резюме (get all cities from resume)
7. [x] забрати хоббі всіх здобувачів, що мешкають в заданому місті (get all languages from people in city)
8. [x] забрати всіх здобувачів, що працювали в одному закладі (заклад ми не вказуємо) (group by organization)

## Common ER for all databases

![ER Diagram](./img/Postgres_ER.png)