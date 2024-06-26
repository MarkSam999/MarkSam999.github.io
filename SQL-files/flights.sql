-- Создание таблицы flights
CREATE TABLE flights (
    id SERIAL PRIMARY KEY,                  -- Уникальный идентификатор рейса
    origin VARCHAR(3) NOT NULL,             -- Аэропорт вылета (IATA код)
    destination VARCHAR(3) NOT NULL,        -- Аэропорт прилета (IATA код)
    duration INTEGER NOT NULL               -- Длительность рейса в минутах
);

-- Вставка данных в таблицу flights
INSERT INTO flights (origin, destination, duration) VALUES
('New York', 'London', 415),
('Shanghai', 'Paris', 760),
('Istanbul', 'Tokyo', 700),
('New York', 'Paris', 435),
('Moscow', 'Paris', 245),
('Lima', 'New York', 455);