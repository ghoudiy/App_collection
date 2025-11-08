DECLARE
  CURSOR CU2 IS
    SELECT A.refa
    FROM Article A
    WHERE lower(categorie) = 'informatique' and refa not in (select refa from ligne_commande L) FOR UPDATE;
BEGIN 

  for rec in cu2 LOOP
    delete from article
    where current of cu2;
  END LOOP;
END;
    