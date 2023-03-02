--Run this script on prd master databases

USE [master]

DECLARE @LOGIN VARCHAR(250)

SET @LOGIN = 'sys_login_evl_evlos_prd'--Insert SYS Login Here

DECLARE @PASSWORD VARCHAR(250)
SET @PASSWORD = '<sys_password_here>'--Insert SYS Password Here

Declare @LOGIN_CREATING VARCHAR(250)

--Creating SYS Login
SET @LOGIN_CREATING='CREATE LOGIN '+@LOGIN +' WITH PASSWORD ='''+@PASSWORD +''''
EXEC (@LOGIN_CREATING)