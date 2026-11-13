CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS chunks (
    id        SERIAL PRIMARY KEY,
    doc       TEXT NOT NULL,
    page      INT  NOT NULL,
    text      TEXT NOT NULL,
    embedding vector(384) NOT NULL
);
