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


