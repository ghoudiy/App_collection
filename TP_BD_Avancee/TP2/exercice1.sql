SET SERVEROUTPUT ON;
--ACCEPT nume NUMBER PROMPT 'Donner le numero d'employe: ';
--ACCEPT fct VARCHAR2(15) PROMPT 'Donner la fonction d'employe: ';
--ACCEPT commiss NUMBER PROMPT 'Donner la commission d'employe: ';

DECLARE 
    commiss_null EXCEPTION;
    nume Employe.numemp%TYPE := &nume;
    fct Employe.fonction%TYPE := &fct;
    commiss Employe.commission%TYPE := &commiss;
    numemploye Employe.numemp%TYPE;
BEGIN
    if commiss = 0 AND lower(fct) = 'representant' then
        RAISE commiss_null;
    else
        INSERT INTO employe values(nume, 'yassine', fct, 33, SYSDATE, 5000, commiss, 10);
    end if;
EXCEPTION
    when commiss_null then dbms_output.put_line('un représentant ne doit pas avoir une commission nulle');
end;

