SET SERVEROUTPUT ON;
DECLARE 
  moy NUMBER;
  vnumemp employe.NumEmp%TYPE;
  vnomemp employe.NomEmp%TYPE;
  vdaterec employe.DateRec%TYPE;
  vsalaire employe.Salaire%TYPE;

  vnumdep Departement.numdep%TYPE;
  vnomdep Departement.nomdep%TYPE;
  vdatrec employe.daterec%TYPE;


  nbprog NUMBER;
  nbemp NUMBER;

  vcommiss employe.COMMISSION%TYPE;
BEGIN
  -- 1)   
  -- SELECT AVG(salaire) INTO moy FROM employe;
  -- dbms_output.put_line('La moyenne de salaires = ' || ROUND(moy, 4));
  
--  2) 
  -- SELECT NumEmp, NomEmp, DateRec, Salaire INTO vnumemp, vnomemp, vdatrec, vsalaire
  -- FROM employe
  -- WHERE LOWER(fonction) = 'programmeur' AND daterec = (SELECT min(daterec) FROM employe WHERE lower(fonction) = 'programmeur');

  -- IF vsalaire >= moy THEN
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

  -- DBMS_OUTPUT.PUT_LINE('Le pourcentage des programmeurs = ' || ROUND(nbprog * 100 / nbemp, 2) || '%');


  -- 4) 
--   SELECT D.numdep, nomdep, COUNT(numemp) into vnumdep, vnomdep, nbprog
--   FROM employe E, departement D
--   WHERE E.numdep = D.numdep and lower(fonction) = 'programmeur'
--   GROUP BY D.numdep, nomdep
--   HAVING COUNT(numemp) = (SELECT MAX(COUNT(*)) FROM employe E, Departement D WHERE E.numdep = D.numdep and lower(fonction) = 'programmeur' group by E.numdep);

--   DBMS_OUTPUT.put_line('Num Departement = ' || vnumdep || '
-- Nom Departement = ' || vnomdep || '
-- Nombre de programmeurs = ' || nbprog);

  -- 5)  
  SELECT numemp, commission, salaire into vnumemp, vcommiss, vsalaire
  from employe
  where lower(fonction) = 'représentant' and daterec = (select max(daterec) from employe where lower(fonction) = 'représentant');

  if vcommiss is NULL OR vcommiss = 0 THEN
    update EMPLOYE
    set commission = SALAIRE * 0.1
    where numemp = vnumemp;
  end if;

END;
/