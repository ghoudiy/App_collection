SET SERVEROUTPUT ON;
ACCEPT N NUMBER PROMPT 'Donner un entier N: ';
DEFINE N = &N

DECLARE
  S NUMBER := 0;
  F NUMBER := 1;
  D NUMBER := 0;
BEGIN
  FOR i IN 1..&N LOOP
    S := S + i;
    F := F * i;
    IF &N MOD i = 0 THEN
      D := D + i;
    END IF;
  END LOOP;

  dbms_output.put_line('La somme 1+2+..N = ' || S);
  dbms_output.put_line('N! = ' || F);
  D := D - &N;
  IF (D = &N) THEN
    dbms_output.put_line('N est parfait');
  ELSE
    dbms_output.put_line('N n''est pas parfait');
  END IF;
END;
/
