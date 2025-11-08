-- DEPARTEMENT( NumDep, NomDep)
-- EMPLOYE( NumEmp, NomEmp, Fonction, DateRec, Salaire,Commission, #NumDep)

-- CREATE TABLE DEPARTEMENT (
--   NumDep number PRIMARY KEY,
--   NomDep Varchar2(20)
-- )

--CREATE TABLE employe(
--  NumEmp NUMBER PRIMARY KEY,
--  NomEmp VARCHAR2(20),
--  Fonction varchar2(20),
--  DateRec DATE,
--  Salaire NUMBER CHECK(Salaire > 0),
--  Commission NUMBER,
--  NumDep NUMBER REFERENCES DEPARTEMENT(NumDep) ON DELETE CASCADE
--)

---- Departements
--INSERT INTO DEPARTEMENT VALUES (10, 'Informatique');
--INSERT INTO DEPARTEMENT VALUES (20, 'Ressources Humaines');
--INSERT INTO DEPARTEMENT VALUES (30, 'Marketing');
--INSERT INTO DEPARTEMENT VALUES (40, 'Ventes');
--
---- Programmeurs (with varying salaries and dates)
--INSERT INTO EMPLOYE VALUES (1001, 'Ahmed', 'Programmeur', '10/05/2010', 3000, NULL, 10);
--INSERT INTO EMPLOYE VALUES (1002, 'Samir', 'Programmeur', '12/03/2012', 3200, NULL, 10);
--INSERT INTO EMPLOYE VALUES (1003, 'Omar', 'Programmeur', '01/07/2008', 2800, NULL, 10); -- Oldest
--INSERT INTO EMPLOYE VALUES (1004, 'Nadia', 'Programmeur', '23/09/2015', 3500, NULL, 20);
--INSERT INTO EMPLOYE VALUES (1005, 'Fatima', 'Programmeur', '15/01/2018', 3700, NULL, 30);
--INSERT INTO EMPLOYE VALUES (1006, 'Youssef', 'Programmeur', '30/06/2020', 4000, NULL, 30);
--
---- Other employees
--INSERT INTO EMPLOYE VALUES (2001, 'Karim', 'Manager', '22/04/2011', 5000, NULL, 10);
--INSERT INTO EMPLOYE VALUES (2002, 'Salma', 'Analyste', '11/10/2013', 4500, NULL, 20);
--INSERT INTO EMPLOYE VALUES (2003, 'Rami', 'Technicien', '05/11/2016', 2800, NULL, 10);
--INSERT INTO EMPLOYE VALUES (2004, 'Laila', 'Vendeur', '18/02/2019', 2600, 100, 40);
--INSERT INTO EMPLOYE VALUES (2005, 'Hana', 'Secretaire', '20/08/2021', 2300, NULL, 20);
--
---- Représentant with NULL commission
--INSERT INTO EMPLOYE VALUES (2006, 'Tariq', 'Représentant', '15/04/2023', 3000, NULL, 40);


-- Représentant with 0 commission
--INSERT INTO EMPLOYE VALUES (2007, 'Imane', 'Représentant', '01/12/2022', 3100, 0, 40);

SET SERVEROUTPUT ON;
DECLARE 
  moy NUMBER;
  vnumemp employe.NumEmp%TYPE;
  vnomemp employe.NomEmp%TYPE;
  vdaterec employe.DateRec%TYPE;
  vsalaire employe.Salaire%TYPE;

  vnumdep Departement.numdep%TYPE;
  vnomdep Departement.nomdep%TYPE;

  nbprog NUMBER;
  nbemp NUMBER;

  vcommiss employe.COMMISSION%TYPE;
BEGIN
  -- 1)   
  -- SELECT AVG(salaire) INTO moy FROM employe;
  -- dbms_output.put_line('La moyenne de salaires = ' || moy);
  
--  2) 
  -- SELECT NumEmp, NomEmp, DateRec, Salaire INTO vnumemp, vnomemp, vdatrec, vsalaire
  -- FROM employe
  -- WHERE LOWER(fonction) = 'programmeur' AND daterec = (SELECT min(daterec) FROM employe WHERE lower(fonction) = 'programmeur');

  -- IF salaire >= moy THEN
  --   UPDATE employe
  --   SET salaire = salaire * 1.1
  --   WHERE NumEmp = vnumemp;
  -- ELSE
  --   UPDATE employe
  --   SET salaire = moy
  --   WHERE NumEmp = vnumemp;
  -- END IF;

  
--  3)
  -- SELECT COUNT(numemp) INTO nbprog
  -- FROM employe
  -- WHERE lower(fonction) = 'programmeur';

  -- SELECT COUNT(numemp) INTO nbemp
  -- FROM employe;

  -- DBMS_OUTPUT.PUT_LINE("Le pourcentage des programmeurs = " || (nbprog * 100 / nbemp));


  -- 4) 
  -- SELECT D.numdep, nomdep, COUNT(numemp) into vnumdep, vnomdep, nbprog
  -- FROM employe E, departement D
  -- WHERE E.numdep = D.numdep and lower(fonction) = 'programmeur'
  -- GROUP BY E.numdep, nomdep
  -- HAVING COUNT(numemp) = (SELECT MAX(COUNT(*)) FROM employe E, Departement D WHERE E.numdep = D.numdep and lower(fonction) = 'programmeur');

  SELECT numemp, commission, salaire into vnumemp, vcommiss, vsalaire
  from employe
  where lower(fonction) = 'representant' and daterec = (select max(daterec) from employe where lower(fonction) = 'representant');

  if vcommiss is NULL OR vcommiss = 0 THEN
    update EMPLOYE
    set commission = SALAIRE * 0.1
    where numemp = vnumemp;
  end if;

END;


