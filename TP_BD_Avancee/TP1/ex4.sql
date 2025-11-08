DECLARE 
TYPE rec_emp is record(
  numemp Employe.numemp%TYPE,
  nomemp Employe.nomemp%TYPE,
  fonction Employe.fonction%TYPE,
  salaire Employe.salaire%TYPE,
  numdep DEPartement.numdep%TYPE
);

TYPE Tab_emp is rec_emp index of BINary INTEGER;
rec3 Rec_emp;
rec2 Rec_emp;
rec rec_emp;
T Tab_emp;
maxv Employe.salaire%TYPE;
numd Departement.numdep%TYPE;
max_pos NUMBER;
BEGIN

select numemp, nomemp, fonction salaire, E.numdep into rec 
from Employe
where salaire = (select max(salaire) from employe);

T(0).numemp = rec.numemp;
T(0).nomemp = rec.nomemp;
T(0).fonction = rec.fonction;
T(0).salaire = rec.salaire;
T(0).numdep = rec.numdep;

select numemp, nomemp, fonction salaire, E.numdep into rec2
from Employe E, Departement
where E.numdep = DEPartement.numdep and
fct = 'programmeur' and
nomdep = 'comptabilite' and
daterec = (
  select max(daterec) 
  from employe E, Departement D 
  where fonction = 'programmeur' 
  and nomdep = 'comptabilite' 
  and E.numdep = D.numdep
);


T(1).numemp = rec2.numemp;
T(1).nomemp = rec2.nomemp;
T(1).fonction = rec2.fonction;
T(1).salaire = rec2.salaire;
T(1).numdep = rec2.numdep;


select numdep into numd
from Departement D, E Employe
where E.numdep = D.numdep and fonction = 'programmeur'
Group by numdep
having Count(E.numdep) = (
  Select Max(COUNT(E1.numdep))
  FROM Employe E1, Departement D1
  WHERE E1.numdep = D1.numdep and fonction = 'programmeur'
);

select numemp, nomemp, fonction salaire, E.numdep into rec3
From Employe E, Departement D
where E.numdemp = D.numdep and fonction = 'programmeur' and daterec = (
  select min(daterec)
  from employe
  where numdep = numd
);

T(2).numemp = rec3.numemp;
T(2).nomemp = rec3.nomemp;
T(2).fonction = rec3.fonction;
T(2).salaire = rec3.salaire;
T(2).numdep = rec3.numdep;


max_pos := 0;
for i in 1..2 loop
  if T(i).salaire > T(max_pos).salaire then
    max_pos := i; 
  end if;
end loop;
DBMS_OUTPUT.PUT_LINE('Num employe = ' || T(mas_pos).numemp || 'Nom employe = ' || T(max_pos).nomemp
|| ' Fonction = ' || T(max_pos).fonction || ' Salaire = ' || T(max_pos).salaire || ' Num dep = ' || T(max_pos).numdep);

END;
