SET SERVEROUTPUT ON;

DECLARE
  TYPE REC_FRS IS RECORD ( 
    num FOURNISSEUR.nf%type,
    nom FOURNISSEUR.nomf%type,
    ca NUMBER,
    Classe char
  );
  frs REC_FRS;
BEGIN

  FRS.NUM := 50;
  
  SELECT nomf into frs.nom
  FROM FOURNISSEUR
  WHERE nf = 50;

  SELECT SUM(PU * QTECD) INTO FRS.ca  
  from COMMANDE C, Ligne_commande L, TARIF T
  where C.nf = 50 and C.nc = L.nc and T.refa = L.refa AND T.nf = 50;

  if FRS.CA >100000 then
    frs.classe := 'A';
  ELSIF Frs.CA <= 100000 AND FRS.CA > 50000 then
    frs.classe := 'B';
  else
    frs.classe := 'C';
  end if;
  
  DBMS_OUTPUT.PUT_LINE('Fournisseur: ' || frs.nom || ' | CA: ' || frs.ca || ' | Classe: ' || frs.classe);

end;
/
