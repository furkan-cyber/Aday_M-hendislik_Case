--CREATE FLIGHT TABLE


CREATE TABLE flight (
        flight_id INTEGER PRIMARY KEY,
	model_id  INTEGER,
	mission_id INTEGER,
	flight_date TIMESTAMP,
	landing_date TIMESTAMP,
	landing_success VARCHAR(1),
	flight_success  VARCHAR(1),
	flight_county VARCHAR(15),
	flight_province VARCHAR(15),
	flight_region VARCHAR(25),
	real_flight_time TIME ,
	mission_success  VARCHAR(1)
);

--CREATE GPS TABLE

CREATE TABLE gps(
        flight_id INTEGER,
	timee TIME,
	lat   FLOAT,
	lon   FLOAT,
	alt   FLOAT
);

--CREATE ANG-VEL TABLE

CREATE TABLE ang_vel(
        flight_id INTEGER,
        timee     TIMESTAMP,
	xyz0      FLOAT,
	xyz1      FLOAT,
	xyz2      FLOAT,
	typee     VARCHAR(50)
);






