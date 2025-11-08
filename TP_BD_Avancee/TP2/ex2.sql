DECLARE 
  elimi_err EXCEPTION;
  m1 NUMBER(5,2);
  m2 NUMBER(2);
  moy NUMBER(5, 2);
  mention VARCHAR2(30);
  ett etudiant.etat%TYPE;

BEGIN
  SELECT SUM(moymat * coefficient), sum(coefficient), etat into m1, m2, ett
  FROM ETUDIANT E, Matiere M, Resultat R
  WHERE R.noet = 20 and M.CODMAT = R.CODMAT and e.noet = 20
  GROUP BY E.noet, etat;

  if ett = 'éliminé' then
    RAISE elimi_err;
  ELSE
    UPDATE ETUDIANT
    set MOYENNEG = m1 / m2
    where NOET = 20;
  end if;

    moy := m1 / m2;
    IF moy < 10 THEN
        mention := 'Non admis';
    ELSIF moy >= 10 AND moy < 12 THEN
        mention := 'Admis avec mention Passable';
    ELSIF moy >= 12 AND moy < 14 THEN
        mention := 'Admis avec mention Assez Bien';
    ELSIF moy >= 14 AND moy < 16 THEN
        mention := 'Admis avec mention Bien';
    ELSE  -- moyenne >= 16
        mention := 'Admis avec mention Très Bien';
    END IF;

    DBMS_OUTPUT.PUT_LINE('Moyenne = ' || moy || ', Mention = ' || mention);


EXCEPTION
  when NO_DATA_FOUND then DBMS_OUTPUT.PUT_LINE('Etudiant non existante');
  when elimi_err then DBMS_OUTPUT.PUT_LINE('Etudiant deja eliminee');
end;
/
