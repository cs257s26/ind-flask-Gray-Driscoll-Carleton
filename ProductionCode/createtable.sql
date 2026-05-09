--Literacy rate table
DROP TABLE IF EXISTS education_data;

CREATE TABLE education_data (
    entity TEXT,
    code CHAR(3),
    year INTEGER,
    literacy_rate NUMERIC,
    avg_years_education NUMERIC,
    population BIGINT,
    region TEXT
);


--Women in gov table
DROP TABLE IF EXISTS women_in_gov_data;

CREATE TABLE women_gov_data (
    entity TEXT,
    code CHAR(3),
    year INTEGER,
    women_gov_percentage NUMERIC,
    region TEXT
);