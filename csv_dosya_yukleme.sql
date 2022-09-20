--COPY CSV TO DATABASE


COPY flight
FROM 'C:\Users\PC\Desktop\Task (1)\flight.csv' 
DELIMITER ',' 
CSV HEADER;


SELECT * FROM flight



COPY gps
FROM 'C:\Users\PC\Desktop\Task (1)\gps.csv' 
DELIMITER ',' 
CSV HEADER;

SELECT * FROM gps

COPY ang_vel
FROM 'C:\Users\PC\Desktop\Task (1)\angular_velocity.csv' 
DELIMITER ',' 
CSV HEADER;

SELECT * FROM ang_vel
