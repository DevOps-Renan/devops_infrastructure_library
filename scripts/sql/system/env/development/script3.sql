--Run this script on dev master dbs

USE [master]

DECLARE @USER VARCHAR(250)
SET @USER = 'sys_user_evl_evlos_dev'--Insert SYS User Here

DECLARE @LOGIN VARCHAR(250)
SET @LOGIN = 'sys_login_evl_evlos_dev'--Insert SYS Login Here

DECLARE @USER_CREATING VARCHAR(250)

--Creating SYS User
SET @USER_CREATING='CREATE USER ['+@USER +'] FOR LOGIN ['+@LOGIN +']'
EXEC (@USER_CREATING)