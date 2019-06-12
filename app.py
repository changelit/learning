from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:88888888@127.0.0.1/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 用于追踪对象修改，可以关闭
db = SQLAlchemy(app)


@app.route('/')
def index():
    from main.dao.contacts import Contacts
    # 查询一条记录
    get_row = Contacts.query.first()
    print(get_row.name)

    # 删除一条记录
    get_id = Contacts.query.get(14)
    if get_id:
        db.session.delete(get_id)
        db.session.commit()

    # 插入一条记录
    insert_row = Contacts(id='14', name='xiangsuwei', tel='18822222222')
    db.session.add(insert_row)
    db.session.commit()

    # 更新一条记录
    update_name = Contacts.query.get(14)
    update_name.name = 'YangZhi'
    db.session.commit()

    get_specific_rows = Contacts.query.filter(Contacts.name.like('c%')).all()
    array = ''
    for row in get_specific_rows:
        id = row.id
        name = row.name
        tel = row.tel
        array += str(id) + name + tel + '\n'
    return array, 200


if __name__ == '__main__':
    app.run()
