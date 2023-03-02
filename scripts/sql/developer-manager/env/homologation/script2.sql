--Run this script on hmg databases except hmg master dbs

--Part 1 (For Developers): Creating Role, Grating Role Permission, Creating User and Adding this User to the Role Created
DECLARE @ROLE VARCHAR(250)
SET @ROLE = 'develop_role_evl_evlos_hmg'--Insert DEV Role Here

DECLARE @USER VARCHAR(250)
SET @USER = 'develop_user_evl_evlos_hmg'--Insert DEV User Here

DECLARE @LOGIN VARCHAR(250)
SET @LOGIN = 'develop_login_evl_evlos_hmg'--Insert DEV Login Here

DECLARE @ROLE_CREATING VARCHAR(250)

DECLARE @ROLE_PERMISSIONS VARCHAR(250)

DECLARE @USER_CREATING VARCHAR(250)

DECLARE @USER_TO_ROLE VARCHAR(250)

--Creating DEV Role
SET @ROLE_CREATING='CREATE ROLE ['+@ROLE +']'
EXEC (@ROLE_CREATING)

--Granting DEV Role Permission
SET @ROLE_PERMISSIONS='GRANT SELECT, INSERT, UPDATE, DELETE TO ['+@ROLE +']'
EXEC (@ROLE_PERMISSIONS)

--Creating DEV User
SET @USER_CREATING='CREATE USER ['+@USER +'] FOR LOGIN ['+@LOGIN +']'
EXEC (@USER_CREATING)

--Adding DEV User To Role
SET @USER_TO_ROLE='ALTER ROLE ['+@ROLE +'] ADD MEMBER ['+@USER +']'
EXEC (@USER_TO_ROLE)

--Part 2 (For manager): Creating Role, Grating Role Permission, Creating User and Adding this User to the Role Created

SET @ROLE = 'manager_role_evl_evlos_hmg'--Insert manager Role Here

SET @USER = 'manager_user_evl_evlos_hmg'--Insert manager User Here

SET @LOGIN = 'manager_login_evl_evlos_hmg'--Insert manager Login Here

--Creating manager Role
SET @ROLE_CREATING='CREATE ROLE ['+@ROLE +']'
EXEC (@ROLE_CREATING)

--Granting manager Role Permission
SET @ROLE_PERMISSIONS='GRANT SELECT, INSERT, UPDATE, DELETE TO ['+@ROLE +']'
EXEC (@ROLE_PERMISSIONS)

--Creating manager User
SET @USER_CREATING='CREATE USER ['+@USER +'] FOR LOGIN ['+@LOGIN +']'
EXEC (@USER_CREATING)

--Adding manager User To Role
SET @USER_TO_ROLE='ALTER ROLE ['+@ROLE +'] ADD MEMBER ['+@USER +']'
EXEC (@USER_TO_ROLE)