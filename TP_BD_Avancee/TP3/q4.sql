SET SERVEROUTPUT ON;

DECLARE 
  CURSOR CU4 (ref_arg article.refa%TYPE) IS
    select PU
    from tarif T, FOURNISSEUR F
    where T.nf = F.nf and lower(ville) = 'sfax' and refa = ref_arg and pu = (
        select Min(Pu) from Tarif T1, Fournisseur F1
        where T1.nf = F1.nf and lower(ville) = 'sfax' and refa = ref_arg
    );
  cursor ct is 
    select F.nf, refa
    from Fournisseur F, Tarif T
    where F.nf = T.nf and lower(ville) = 'tunis';
  
BEGIN
  for rec in CT LOOP
    for r2 in CU4(rec.refa) LOOP
      DBMS_OUTPUT.PUT_LINE('refa = '  || rec.refa || ' PU = ' || r2.pu || 'nf = ' || rec.nf);
      update Tarif
      set PU = r2.pu * 0.9
      where nf = rec.nf and refa = rec.refa;
    end loop;
  end loop;
END;