DROP TABLE IF EXISTS education;

CREATE TABLE education(
	id SERIAL PRIMARY KEY,
	region VARCHAR,
	edad INT,
	idioma_materno VARCHAR,
	nivel_educacion VARCHAR
)