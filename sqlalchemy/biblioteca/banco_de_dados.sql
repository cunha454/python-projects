USE biblioteca;

INSERT INTO autores (id, nome, data_nascimento, nacionalidade) VALUES
(1, 'Machado de Assis', '1839-06-21', 'BRA'),
(2, 'Clarice Lispector', '1920-12-10', 'BRA'),
(3, 'Jorge Amado', '1912-08-10', 'BRA'),
(4, 'Graciliano Ramos', '1892-10-27', 'BRA'),
(5, 'Jane Austen', '1775-12-16', 'GBR'),
(6, 'George Orwell', '1903-06-25', 'GBR'),
(7, 'Gabriel García Márquez', '1927-03-06', 'COL'),
(8, 'Agatha Christie', '1890-09-15', 'GBR'),
(9, 'Fyodor Dostoevsky', '1821-11-11', 'RUS'),
(10, 'Mary Shelley', '1797-08-30', 'GBR');

INSERT INTO livros (id, nome, genero, data_lancamento, disponibilidade, id_autor) VALUES
(1, 'Dom Casmurro', 'Romance', '1899-01-01', TRUE, 1),
(2, 'Memórias Póstumas de Brás Cubas', 'Romance', '1881-01-01', TRUE, 1),
(3, 'A Hora da Estrela', 'Drama', '1977-01-01', TRUE, 2),
(4, 'Perto do Coração Selvagem', 'Romance', '1943-01-01', TRUE, 2),
(5, 'Gabriela, Cravo e Canela', 'Romance', '1958-01-01', TRUE, 3),
(6, 'Capitães da Areia', 'Drama', '1937-01-01', FALSE, 3),
(7, 'Vidas Secas', 'Drama', '1938-01-01', TRUE, 4),
(8, 'São Bernardo', 'Romance', '1934-01-01', TRUE, 4),
(9, 'Orgulho e Preconceito', 'Romance', '1813-01-28', TRUE, 5),
(10, 'Razão e Sensibilidade', 'Romance', '1811-01-01', TRUE, 5),
(11, '1984', 'Ficção', '1949-06-08', FALSE, 6),
(12, 'A Revolução dos Bichos', 'Sátira', '1945-08-17', TRUE, 6),
(13, 'Cem Anos de Solidão', 'Realismo mágico', '1967-05-30', TRUE, 7),
(14, 'O Amor nos Tempos do Cólera', 'Romance', '1985-01-01', TRUE, 7),
(15, 'O Assassinato de Roger Ackroyd', 'Mistério', '1926-06-01', TRUE, 8),
(16, 'E Não Sobrou Nenhum', 'Mistério', '1939-11-06', FALSE, 8),
(17, 'Crime e Castigo', 'Romance', '1866-01-01', TRUE, 9),
(18, 'Os Irmãos Karamázov', 'Romance', '1880-01-01', TRUE, 9),
(19, 'Frankenstein', 'Terror', '1818-01-01', TRUE, 10),
(20, 'O Último Homem', 'Ficção', '1826-01-01', TRUE, 10);
