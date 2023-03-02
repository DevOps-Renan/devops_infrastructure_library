--Run this script on dev databases except dev master dbs

DECLARE @DATA_BASE VARCHAR(250)
SET @DATA_BASE = 'sqldb-evl-<nome_do_cliente>-dev'

USE [@DATA_BASE]

--Creating Role, Grating Role Permission, Creating User and Adding this User to the Role Created
DECLARE @ROLE VARCHAR(250)
SET @ROLE = 'sys_role_evl_evlos_dev'--Insert SYS Role Here

DECLARE @USER VARCHAR(250)
SET @USER = 'sys_user_evl_evlos_dev'--Insert SYS User Here

DECLARE @LOGIN VARCHAR(250)
SET @LOGIN = 'sys_login_evl_evlos_dev'--Insert SYS Login Here

DECLARE @ROLE_CREATING VARCHAR(250)

DECLARE @ROLE_PERMISSIONS VARCHAR(250)

DECLARE @USER_CREATING VARCHAR(250)

DECLARE @USER_TO_ROLE VARCHAR(250)

--Creating SYS Role
SET @ROLE_CREATING='CREATE ROLE ['+@ROLE +']'
EXEC (@ROLE_CREATING)

--Granting SYS Role Permission
SET @ROLE_PERMISSIONS='GRANT SELECT, INSERT, UPDATE, DELETE TO ['+@ROLE +']'
EXEC (@ROLE_PERMISSIONS)

--Creating SYS User
SET @USER_CREATING='CREATE USER ['+@USER +'] FOR LOGIN ['+@LOGIN +']'
EXEC (@USER_CREATING)

--Adding SYS User To Role
SET @USER_TO_ROLE='ALTER ROLE ['+@ROLE +'] ADD MEMBER ['+@USER +']'
EXEC (@USER_TO_ROLE)