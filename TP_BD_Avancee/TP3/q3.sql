SET VERIFY OFF;
SET SERVEROUTPUT ON;

DECLARE
  CURSOR CU3 IS
    SELECT L.*, C.Nf
    FROM Tarif T, LIGNE_COMMANDE L, Commande C
    WHERE L.nc = C.nc and 
    C.nf = T.nf and 
    T.refa = L.refa AND 
    qtecd > 500 and
    PU > 2000;
  ncm commande.nc%TYPE;
  r1 tarif%rowtype;

BEGIN 
  for rec in cu3 LOOP
    DBMS_OUTPUT.PUT_LINE('Refa = ' || rec.refa || ' | NF = ' || rec.nf || ' | qtecd = ' || rec.qtecd);
    select * into r1
    -- from tarif where refa = rec.refa and pu = (select min(pu) from tarif where refa = rec.refa); # unnecessary check in the main select (refa = rec.refa)
    from tarif where pu = (select min(pu) from tarif where refa = rec.refa);
    
    if r1.nf != rec.nf then
      -- DBMS_OUTPUT.PUT_LINE('I am inside the condition');
      update LIGNE_COMMANDE
      set qtecd = qtecd * 0.5
      where nc = rec.nc and refa = rec.refa;

      select Max(nc) into ncm from commande;
      INSERT INTO commande values(ncm+1, sysdate, r1.nf);
      insert into LIGNE_COMMANDE VALUES(ncm + 1, rec.refa, rec.qtecd * 0.5);
    end if;
  end LOOP;
end;
/
