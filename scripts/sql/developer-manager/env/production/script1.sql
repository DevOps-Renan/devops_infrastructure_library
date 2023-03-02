--Run this script on prd master databases

--Part 1 (For Developers): Creating DEV Login

DECLARE @LOGIN VARCHAR(250)

SET @LOGIN = 'develop_login_evl_evlos_prd'--Insert Dev Login Here

DECLARE @PASSWORD VARCHAR(250)
SET @PASSWORD = '<develop_password_here>'--Insert Dev Password Here

Declare @LOGIN_CREATING VARCHAR(250)

SET @LOGIN_CREATING='CREATE LOGIN '+@LOGIN +' WITH PASSWORD ='''+@PASSWORD +''''
EXEC (@LOGIN_CREATING)

--Part 2 (For manager): Creating manager Login

SET @LOGIN = 'manager_login_evl_evlos_prd'--Insert manager Login Here

SET @PASSWORD = '<manager_password_here>'--Insert manager Password Here

SET @LOGIN_CREATING='CREATE LOGIN '+@LOGIN +' WITH PASSWORD ='''+@PASSWORD +''''
EXEC (@LOGIN_CREATING)