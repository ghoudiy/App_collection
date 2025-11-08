SET VERIFY OFF;
SET SERVEROUTPUT ON;

DECLARE
  ART_NOTFOUND_ERR EXCEPTION;
  CURSOR CU2b IS
  SELECT a.refa, sum(qtecd * pu) AS sc
  FROM article a, LIGNE_COMMANDE L, tarif t, commande c
  WHERE t.refa = l.refa AND
  a.refa = t.refa AND
  c.nc = l.nc AND
  TO_CHAR(datecom, 'yyyy') = 2020 AND
  LOWER(categorie) = 'informatique'
  GROUP BY a.refa;

  aug_qte NUMBER(1, 2);
  rec CU2b%ROWTYPE;
BEGIN

  OPEN CU2b;
  FETCH CU2b INTO rec;
  IF CU2b%NOTFOUND THEN
    RAISE ART_NOTFOUND_ERR;
  END IF;
  CLOSE CU2b;

  FOR rec in CU2b LOOP
    DBMS_OUTPUT.PUT_LINE('Refa = ' || rec.refa || ' | sc = ' || rec.sc);
    if rec.sc > 100000 THEN
      UPDATE article
      set qtemin = qtemin * 1.2
      where refa = rec.refa;
    ELSE
      UPDATE article
      set qtemin = qtemin * 1.1
      where refa = rec.refa;
    end if;
  end loop;
EXCEPTION
  when ART_NOTFOUND_ERR then DBMS_OUTPUT.PUT_LINE('il n’existe aucun article `informatique` commandé durant l''année 2020');
END;
/