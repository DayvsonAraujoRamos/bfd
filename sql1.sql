Mostre todos os registros da tabela Aluno.
(Use SELECT e FROM)
SELECT * 
FROM Aluno;

Exiba apenas o nome e a nota1 de todos os alunos.
(Use SELECT com colunas específicas)
SELECT nome, nota1 
FROM Aluno;

Liste todos os alunos cuja nota2 seja maior que 8.
(Use WHERE)
SELECT * 
FROM Aluno 
WHERE nota2 > 8;

Mostre os alunos que nasceram após o ano de 2000.
(Use WHERE com data)
SELECT * 
FROM Aluno 
WHERE data_nascimento > '2000-12-31';

Exiba o nome e a mensalidade de todos os cursos que custam mais de 600 reais.
(Use WHERE com condição numérica)
FROM Curso 
WHERE mensalidade > 600;

Mostre o nome das turmas e o ano correspondente, ordenados pelo ano em ordem crescente.
(Use ORDER BY)
SELECT nome, ano 
FROM Turma 
ORDER BY ano ASC;
