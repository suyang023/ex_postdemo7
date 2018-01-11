import psycopg2



def conndb():
    # 链接数据库
    conn = psycopg2.connect(database="test", user="postgres", password="yucun", host="127.0.0.1", port="5432")
    print("open successfully")
    return conn
#创建数据库表格
def createtable():
    #调用conndb方法
    connpg = conndb()
    cur = connpg.cursor()
    # cur.execute('''create table found(
    # id int primary key not null,
    # name text not null,
    # tel char(20) not null
    # # )''');
    # cur.execute('''CREATE TABLE vender
    #     (
    #       sid numeric(15,0) NOT NULL  , -- 唯一序列号
    #       vender_id character varying(12) NOT NULL, -- Vender编号
    #       vender_name character varying(128), -- Vender名称    小于32个字符
    #       connector character varying(50), -- 联系人
    #       phone character varying(20), -- 联系电话
    #       email character varying(128), -- 邮件
    #       industry character varying(32), -- 行业
    #       created_by character varying(32) NOT NULL, -- 创建者
    #       created_dt timestamp without time zone NOT NULL, -- 创建时间
    #       version numeric(9,0) NOT NULL DEFAULT 1, -- 版本号
    #       updated_by character varying(32), -- 更新者
    #       updated_dt timestamp without time zone, -- 更新时间
    #       del_flg numeric(1,0) NOT NULL -- 删除标志  0：有效、1：无效
    #     )  ''')

    cur.execute('''CREATE TABLE founddemo  
            (  
              id character(50)   , -- 唯一序列号  
              leixi character(20),
              sid  character(20),
              chufa character(2000),
              anjian character(1000),
              zuzhi character(1000),
              faren character(500),
              shishi character(2000),
              chufajieguo character(2000),
              fangshi character(2000),
              danwei character(1000),
              beizhu character(200)
              )  ''')


    print("sive successfully")
    connpg.commit()
    connpg.close()
#插入数据
def insertdb():

    connpg = conndb()
    cur = connpg.cursor()
    cur.execute("insert into found(id,name,tel) values(1,'su','123456')");
    print("sive successfully")
    connpg.commit()
    connpg.close()
#查询数据
def selectdb():
    connpg = conndb()
    cur = connpg.cursor()
    cur.execute("select * from found")
    rows = cur.fetchall()
    for see in rows:
        print('id=',see[0])
        print('name=',see[1])
        print('tel=',see[2])
    print("open db all1")
    connpg.close()
# 修改数据
def update():
    connpg = conndb()
    cur = connpg.cursor()
    cur.execute("update found set tel = 87654321 where id = 1")
    connpg.close()