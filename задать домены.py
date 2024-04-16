# Запускать из консоли Python ArcGIS
# изменить при необходимости пути к БД со справочными таблицами и БД для загрузки доменов

import arcpy

referencedb = r'D:\Шарох\НИОКТР\Кадастровая карта (НКА)\6. ТП\ReferenceTables.gdb'
arcpy.env.workspace = referencedb
targetdb = r'Подключения к базам данных\portaltest(192.168.51.17).sde'

# Удалить все домены из БД. Если домены назначены полям, выдаст ошибку. Тогда разназначить вручную
for i in arcpy.da.ListDomains(targetdb):
    print (i.name)
    arcpy.DeleteDomain_management(targetdb, i)

# Создать новые домены в БД путем импорта таблиц из справочной БД
for i in arcpy.ListTables():
    desc = arcpy.Describe(i).aliasName
    print (i)
    print (desc)
    arcpy.TableToDomain_management(i, code_field='code', description_field='description', in_workspace=targetdb, domain_name=i, domain_description=desc, update_option='REPLACE')