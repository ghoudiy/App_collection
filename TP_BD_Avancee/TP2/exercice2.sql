DECLARE 
  etud_not_found EXCEPTION;
  elimi_err EXCEPTION;
  m1 NUMBER(2, 3);
  m2 NUMBER(2, 3);
  mg NUMBER(2, 3);
  ett etudiant.etat%TYPE;

BEGIN
  SELECT SUM(moymat * coefficient), sum(coefficient), etat into m1, m2, ett
  FROM ETUDIANT E, Matiere M, Resultat R
  WHERE E.NOET = R.noet and M.CODMAT = R.CODMAT and e.noet = 20
  GROUP BY E.noet, etat;

  if m1 is NULL THEN
    RAISE etud_not_found;
  elsif ett = 'elimine' then
    RAISE elimi_err;
  ELSE
    UPDATE ETUDIANT
    set MOYENNEG = m1 / m2
    where NOET = 20;
  end if;

EXCEPTION
  when etud_not_found then DBMS_OUTPUT.PUT_LINE('Etudiant non existante');
  when elimi_err then DBMS_OUTPUT.PUT_LINE('Etudiant deja eliminee');
end;
-- select * from etudiant;
-- Table ETUDIANT
-- CREATE TABLE ETUDIANT (
--     Noet        NUMBER(10)       PRIMARY KEY,
--     Nomet       VARCHAR2(50)     NOT NULL,
--     Adret       VARCHAR2(100),
--     DateNais    DATE,
--     Etat        VARCHAR2(20),
--     MoyenneG    NUMBER(4,2)
-- );

-- -- Table MATIERE
-- CREATE TABLE MATIERE (
--     CodMat      VARCHAR2(10)     PRIMARY KEY,
--     NomMat      VARCHAR2(50)     NOT NULL,
--     Responsable VARCHAR2(50),
--     Coefficient NUMBER(3,1)
-- );

-- -- Table EXAMEN
-- CREATE TABLE EXAMEN (
--     CodMat      VARCHAR2(10),
--     Type        VARCHAR2(20),
--     DateExam    DATE,
--     Salle       VARCHAR2(20),
--     Duree       NUMBER(4,2),
--     PRIMARY KEY (CodMat, Type, DateExam),
--     FOREIGN KEY (CodMat) REFERENCES MATIERE(CodMat)
-- );

-- -- Table RESULTAT
-- CREATE TABLE RESULTAT (
--     Noet        NUMBER(10),
--     CodMat      VARCHAR2(10),
--     MoyMat      NUMBER(4,2),
--     PRIMARY KEY (Noet, CodMat),
--     FOREIGN KEY (Noet) REFERENCES ETUDIANT(Noet),
--     FOREIGN KEY (CodMat) REFERENCES MATIERE(CodMat)
-- );




-- INSERT INTO ETUDIANT (Noet, Nomet, Adret, DateNais, Etat, MoyenneG)
-- VALUES (20, 'Ali Ben Ahmed', '123 Rue Principale', TO_DATE('2000-05-15','YYYY-MM-DD'), 'Actif', NULL);

-- INSERT INTO ETUDIANT (Noet, Nomet, Adret, DateNais, Etat, MoyenneG)
-- VALUES (21, 'Sara Kacem', '45 Avenue des Fleurs', TO_DATE('1999-11-30','YYYY-MM-DD'), 'Actif', NULL);
-- INSERT INTO MATIERE (CodMat, NomMat, Responsable, Coefficient)
-- VALUES ('MAT101', 'Mathematiques', 'Dr. Bensaid', 3);

-- INSERT INTO MATIERE (CodMat, NomMat, Responsable, Coefficient)
-- VALUES ('PHY101', 'Physique', 'Dr. Haddad', 2);

-- INSERT INTO MATIERE (CodMat, NomMat, Responsable, Coefficient)
-- VALUES ('INF101', 'Informatique', 'Dr. Karim', 4);

-- INSERT INTO EXAMEN (CodMat, Type, DateExam, Salle, Duree)
-- VALUES ('MAT101', 'Partiel', TO_DATE('2025-11-10','YYYY-MM-DD'), 'Salle A', 2.0);

-- INSERT INTO EXAMEN (CodMat, Type, DateExam, Salle, Duree)
-- VALUES ('PHY101', 'Partiel', TO_DATE('2025-11-12','YYYY-MM-DD'), 'Salle B', 2.5);

-- INSERT INTO EXAMEN (CodMat, Type, DateExam, Salle, Duree)
-- VALUES ('INF101', 'Partiel', TO_DATE('2025-11-15','YYYY-MM-DD'), 'Salle C', 3.0);

-- -- Résultats pour l'étudiant 20
-- INSERT INTO RESULTAT (Noet, CodMat, MoyMat)
-- VALUES (20, 'MAT101', 15);

-- INSERT INTO RESULTAT (Noet, CodMat, MoyMat)
-- VALUES (20, 'PHY101', 12);

-- INSERT INTO RESULTAT (Noet, CodMat, MoyMat)
-- VALUES (20, 'INF101', 18);

-- -- Résultats pour l'étudiant 21
-- INSERT INTO RESULTAT (Noet, CodMat, MoyMat)
-- VALUES (21, 'MAT101', 14);

-- INSERT INTO RESULTAT (Noet, CodMat, MoyMat)
-- VALUES (21, 'PHY101', 16);

-- INSERT INTO RESULTAT (Noet, CodMat, MoyMat)
-- VALUES (21, 'INF101', 13);
