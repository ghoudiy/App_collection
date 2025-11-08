-- FOURNISSEUR (NF, NOMF, ADRESSE, CODPOSTAL, VILLE, TEL )
-- ARTICLE (REFA, LIBELLE, Frs.CA TEGORIE, QTESTOCK )
--FRS.CA   TARIF ( #NF , #REFA , PU )
-- COMMANDE (NC, DATECOM, #NF )
-- DET_COMMANDE (#NC, #REFA, QTECD )


DECLARE
  TYPE REC_FRS IS RECORD ( 
    num FOURNISSEUR.nf%type;
    nom FOURNISSEUR.nomf%type;
    ca NUMBER;
    Classe Varchar
  );
  frs REC_FRS;
BEGIN

  FRS.NUM := 50;
  
  SELECT nomf into frs.nom
  FROM FOURNISSEUR
  WHERE nf = 50;

  SELECT SUM(PU * QTECD) INTO FRS.ca
  from COMMANDE C, DET_COMMANDE D, TARIF T
  where C.nf = 50 and C.nc = D.nc and T.refa = D.refa AND T.nf = 50;

  if FRS.CA >100 000 then
    frs.classe := 'A';
  ELSIF Frs.CA <= 100 000 AND FRS.CA > 50 000 then
    frs.classe := 'B';
  else
    frs.classe := 'C';
  end if;

end;

