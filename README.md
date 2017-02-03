# Proyecto ateam
## App cdap
Pequeña aplicacion la cual pretende gestionar los permisos de acceso de personal interno y externo a una o varias sucursales de una determinada EMPRESA. El personal de admision y o seguridad de mencionada sucursal podria filtrar el listado de personas y verificar que este, este autorizada o no apara el acceso.

Modelo de base de datos:
* personas: Las personas son personal interno o externo las cuales podrian o no tener acceso a la sucursal.
* empresas: Las empresas son las prestadoras de servicios externas o sectores internos de la EMPRESA.
* locaciones: Las locaciones son sucursales de la EMPRESA y no todas las empresas estan autorizadas a entrar a todas las sucursales de la EMPRESA.

## create a new repository on the command line
echo "# mysite" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/mardeltux/mysite.git
git push -u origin master

## push an existing repository from the command line
git remote add origin https://github.com/mardeltux/mysite.git
git push -u origin master
