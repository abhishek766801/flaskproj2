import os

from sqlalchemy import create_engine,text
my_secret = os.environ['db_connection_string']
engine = create_engine(my_secret,connect_args={
        "ssl": {
            "ssl_ca":  "/etc/ssl/cert.pem"
    
        }
    })
with engine.connect() as conn:
  result=conn.execute(text("select * from jobs"))
  print(result.fetchall())