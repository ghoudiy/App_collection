DECLARE
  CURSOR CU1 IS 
    SELECT A.refa from fournisseur F, Article A, Tarif T
    WHERE T.nf = F.nf AND A.refa = T.refa
    GROUP BY A.refa
    HAVING COUNT(distinct T.nf) <= 2;

BEGIN 
  FOR rec in CU1 LOOP
    UPDATE article
    set qtemax = Qtemax * 1.3 
    WHERE refa = rec.refa;
  END LOOP;
END;
