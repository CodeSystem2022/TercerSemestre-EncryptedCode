-- Andrea LLavel:Instalacion y trabajar en Crud ,Mysql.A la base de datos le puse otors nombres porque no podia utilizar los mismos.Clase 11 .Parte 1 y 2.
-- Nombres que ya habia ulizado."estudiantes = encrypted",la tabla "estudiantes2022= encryptedcode"
-- Por ese motivo aparecemos los integrantes de Encrypted Code en el codigo
-- Comenzamos con CRUD: create(insertar), read(leer), update(actualizar), delete(eliminar)
-- Listar los estudiantes (read)
SELECT * FROM encrypted.encryptedcode;
-- Insertar estudiante
INSERT INTO encrypted.encryptedcode (nombre, apellido, telefono, email) VALUES ("Rocio", "Pulitta", "0614545456", "rocioencod@mail.com");
-- Update(modificar)
UPDATE encrypted.encryptedcode SET nombre="Luis", apellido="Mayorga" WHERE idencryptedcode= 1;
-- Delete(eliminar)
DELETE FROM encrypted.encryptedcode WHERE idencryptedcode=6;
-- Para modificar el idencryptedcode y comience en 1
ALTER TABLE encrypted.encryptedcode AUTO_INCREMENT = 3;


