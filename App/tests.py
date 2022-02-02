from django.http import request
from django.test import TestCase

# Create your tests here.


# test=request.GET.get


# def load_csv(csv_file_path, table_name, database='moviedata'):
#     file = open(ratings.csv, 'r')
#     reader = file.readline()
#     b = reader.split(',')
#     colum = ''
#     for a in b:
#         colum = colum + a + ' varchar(255),'
#     colum = colum[:-1]
#     #编写sql，create_sql负责创建表，data_sql负责导入数据
#     create_sql = 'create table if not exists ' + table_name + ' ' + '(' + colum + ')' + ' DEFAULT CHARSET=utf8'
#     data_sql = "LOAD DATA LOCAL INFILE '%s' INTO TABLE %s FIELDS TERMINATED BY ',' LINES TERMINATED BY '\\r\\n' IGNORE 1 LINES" % (csv_filename,table_name)
#
