--CREATE TABLE MOIS(
--  nummois NUMBER PRIMARY KEY,
--  libmois Varchar2(10)
--);
--
BEGIN
    FOR i in 1..12 LOOP
        INSERT INTO MOIS VALUES(i, TO_CHAR(TO_DATE(i, 'mm'), 'month'));
    END LOOP;
END;
--ALTER SESSION SET NLS_DATE_FORMAT = 'DD/MM/YYYY';

/
