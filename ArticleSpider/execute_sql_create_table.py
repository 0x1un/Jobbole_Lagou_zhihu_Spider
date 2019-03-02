import pymysql

sql = """
CREATE TABLE tourongjie_spider (
      project_need varchar(200) NOT NULL,
      location varchar(15) not null,
      financing_entity varchar(20) ,
      industry varchar(100) NOT NULL,
      industry_nature varchar(100),
      financing_use varchar(100),
      financing_funds varchar (30),
      total_funds varchar(30),
      financing_method varchar(20),
      information varchar (100),
      stage varchar(50),
      capital_account_persent varchar (20),
      financing_exit_method varchar (20),
      min_exit_period varchar (20),
      company_url varchar (300) not null,
      company_profile varchar(100),
      url_object_id varchar(200) not null primary key
  )engine=innodb default character set utf8;

"""

"""
front_image_path varchar(200),

"""


conn = pymysql.connect('127.0.0.1', 'root', 'qingfing', 'article_spider', charset="utf8", use_unicode=True)
cursor = conn.cursor()
try:
    cursor.execute('desc tourongjie_spider;')
except pymysql.err.ProgrammingError:
    cursor.execute(sql)
else:
    print(cursor.fetchall())
conn.close()
