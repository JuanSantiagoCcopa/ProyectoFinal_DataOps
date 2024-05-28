USE Kaggle
GO

--En caso no exista la tabla netflix la creamos
IF NOT EXISTS(SELECT * FROM SYS.TABLES WHERE object_id= OBJECT_ID(N'dbo.netflix') AND type= 'U')
	CREATE TABLE netflix (
		show_id varchar(max),
		type_show varchar(max),
		tittle varchar(max),
		director varchar(max),
		cast_show varchar(max),
		country varchar(max),
		date_added varchar(max),
		release_year varchar(max),
		rating varchar(max),
		duration varchar(max),
		listed_in varchar(max),
		description_show varchar(max)
	)
-- Si la tabla ya existe entonces la trunco
TRUNCATE TABLE dbo.netflix

-- Ingestar dataset
BULK INSERT dbo.netflix
FROM 'C:\Users\Galgo.DESKTOP-NU9OB99\Documents\proyecto_parcial\python\dataset\netflix_titles.csv'
WITH
(
	FIRSTROW= 2, --empieza en la segunda fila
	FIELDTERMINATOR = ',', --indicamos separador de columnas
	ROWTERMINATOR = '0x0a' --hace referencia a un salto de linea
)

GO