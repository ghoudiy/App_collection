SET SERVEROUTPUT ON;

DECLARE 
TYPE rec_emp is record(
  numemp Employe.numemp%TYPE,
  nomemp Employe.nomemp%TYPE,
  fonction Employe.fonction%TYPE,
  salaire Employe.salaire%TYPE,
  numdep DEPartement.numdep%TYPE
);

TYPE Tab_emp is TABLE of rec_emp index by binary_integer;
rec3 Rec_emp;
rec2 Rec_emp;
rec rec_emp;
T Tab_emp;
maxv Employe.salaire%TYPE;
numd Departement.numdep%TYPE;
max_pos NUMBER;
BEGIN

select numemp, nomemp, fonction, salaire, E.numdep into rec 
from Employe E
where salaire = (select max(salaire) from employe);

-- T(0).numemp := rec.numemp;
-- T(0).nomemp := rec.nomemp;
-- T(0).fonction := rec.fonction;
-- T(0).salaire := rec.salaire;
-- T(0).numdep := rec.numdep;
T(0) := rec;
DBMS_OUTPUT.PUT_LINE('Premier élément de T : Employé ayant le salaire le plus élevé');
DBMS_OUTPUT.PUT_LINE('-> ' || T(0).numemp || ', ' || T(0).nomemp || ', ' || T(0).fonction
                      || ', ' || T(0).salaire || ', ' || T(0).numdep);

select numemp, nomemp, fonction, salaire, E.numdep into rec2
from Employe E, Departement D
where E.numdep = D.numdep and
lower(fonction) = 'programmeur' and
lower(nomdep) = 'comptabilite' and
daterec = (
  select max(daterec) 
  from employe E, Departement D 
  where lower(fonction) = 'programmeur' 
  and lower(nomdep) = 'comptabilite' 
  and E.numdep = D.numdep
);


-- T(1).numemp := rec2.numemp;
-- T(1).nomemp := rec2.nomemp;
-- T(1).fonction := rec2.fonction;
-- T(1).salaire := rec2.salaire;
-- T(1).numdep := rec2.numdep;

T(1) := rec2;
DBMS_OUTPUT.PUT_LINE('   
');
DBMS_OUTPUT.PUT_LINE('Deuxième élément de T : Dernier programmeur recruté dans le département COMPTABILITE');
DBMS_OUTPUT.PUT_LINE('-> ' || T(1).numemp || ', ' || T(1).nomemp || ', ' || T(1).fonction
                      || ', ' || T(1).salaire || ', ' || T(1).numdep);

select D.numdep into numd
from Departement D, Employe E
where E.numdep = D.numdep and lower(fonction) = 'programmeur'
Group by D.numdep
having Count(E.numdep) = (
  Select Max(COUNT(E1.numdep))
  FROM Employe E1, Departement D1
  WHERE E1.numdep = D1.numdep and lower(fonction) = 'programmeur'
  Group by D1.numdep
);

select numemp, nomemp, fonction, salaire, E.numdep into rec3
From Employe E, Departement D
where E.numdep = D.numdep and lower(fonction) = 'programmeur' and daterec = (
  select min(daterec)
  from employe
  where numdep = numd
);

-- T(2).numemp := rec3.numemp;
-- T(2).nomemp := rec3.nomemp;
-- T(2).fonction := rec3.fonction;
-- T(2).salaire := rec3.salaire;
-- T(2).numdep := rec3.numdep;


T(2) := rec3;
DBMS_OUTPUT.PUT_LINE('   
');
DBMS_OUTPUT.PUT_LINE('Troisième élément de T : Premier programmeur recruté dans le département avec le plus d’employés');
DBMS_OUTPUT.PUT_LINE('-> ' || T(2).numemp || ', ' || T(2).nomemp || ', ' || T(2).fonction
                      || ', ' || T(2).salaire || ', ' || T(2).numdep);
max_pos := 0;
for i in 1..2 loop
  if T(i).salaire > T(max_pos).salaire then
    max_pos := i; 
  end if;
end loop;
DBMS_OUTPUT.PUT_LINE('   
');
DBMS_OUTPUT.PUT_LINE('Employé avec le salaire maximal dans T');
DBMS_OUTPUT.PUT_LINE('Num employe = ' || T(max_pos).numemp || ' | Nom employe = ' || T(max_pos).nomemp
|| ' | Fonction = ' || T(max_pos).fonction || ' | Salaire = ' || T(max_pos).salaire || ' | Numdep = ' || T(max_pos).numdep);

END;

/