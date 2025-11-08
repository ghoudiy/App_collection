DECLARE
  ca reservation.punuit%TYPE;
  nbj number;
  pu reservation.punuit%type;
  cl_nonvalable_err EXCEPTION;
  cat client.categorie%TYPE;
BEGIN
  SELECT SUM((Datefin - DateDeb) * punuit) INTO ca
  from reservation
  where numcl = 20;
  if ca = 0 THEN
  raise cl_nonvalable_err;
  ELSE
    cat := 'fidele';
    if ca < 1000 THEN
      cat := 'passager';
    end if;
    update client
    set categorie = cat
    where numcl = 20;
  end if;
EXCEPTION
  when cl_nonvalable_err then DBMS_OUTPUT.PUT_LINE('Client n''est pas valable');
END;
/
commit;

