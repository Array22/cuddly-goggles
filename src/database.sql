--stock table
CREATE TABLE eod_prices (
  id SERIAL PRIMARY KEY,
  Ticker VARCHAR(10) NOT NULL,
  Date DATE NOT NULL,
  Open FLOAT8 NOT NULL,
  High FLOAT8 NOT NULL,
  Low FLOAT8 NOT NULL,
  Close FLOAT8 NOT NULL,
  Adjusted_close FLOAT8 NOT NULL,
  Volume INT NOT NULL,
  CONSTRAINT unique_ticker_date UNIQUE(Ticker, Date));