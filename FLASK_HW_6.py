from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import databases
import sqlalchemy
from typing import List
from random import randint

DATABASE_URL = "sqlite:///mydatabase.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()


products = sqlalchemy.Table(
    "products",
    metadata,
    sqlalchemy.Column("product_id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("product_name", sqlalchemy.String(32)),
    sqlalchemy.Column("description", sqlalchemy.String(500)),
    sqlalchemy.Column("price", sqlalchemy.Integer),
)


orders = sqlalchemy.Table(
    "orders",
    metadata,
    sqlalchemy.Column("order_id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.Integer, sqlalchemy.ForeignKey("users.user_id"), nullable=False),
    sqlalchemy.Column("product_id", sqlalchemy.Integer, sqlalchemy.ForeignKey("products.product_id"), nullable=False),
    sqlalchemy.Column("status", sqlalchemy.String),
    sqlalchemy.Column("date_time_orders", sqlalchemy.Integer),
)


users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("user_id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(32)),
    sqlalchemy.Column("surname", sqlalchemy.String(32)),
    sqlalchemy.Column("email", sqlalchemy.String(128)),
    sqlalchemy.Column("password", sqlalchemy.String(32)),
)

engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)


class UserIn(BaseModel):
    name: str = Field(title='Username', max_length=32)
    surname: str = Field(title='UserSurname', max_length=32)
    email: str = Field(title='Email', max_length=128)
    password: str = Field(title='Password', max_length=32)


class User(BaseModel):
    user_id: int = Field(default=None, alias='user_id')
    name: str = Field(title='Username', max_length=32)
    surname: str = Field(title='UserSurname', max_length=32)
    email: str = Field(title='Email', max_length=128)
    password: str = Field(title='Password', max_length=32)


class OrderIn(BaseModel):
    user_id: int
    product_id: int
    date_time_orders: int = Field(default=100000)
    status: str = Field(default="created")


class Order(BaseModel):
    order_id: int
    user_id: int
    product_id: int
    date_time_orders: int = Field(default=100000)
    status: str = Field(default="Create")


class ProductIn(BaseModel):
    product_name: str = Field(title='product_name', max_length=50)
    description: str = Field(title='description', max_length=500)
    price: int = Field(title='price')


class Product(BaseModel):
    product_id: int = Field(default=None, alias='product_id')
    product_name: str = Field(title='product_name', max_length=32)
    description: str = Field(title='description', max_length=500)
    price: int = Field(title='price')


app = FastAPI()


@app.get("/")
def root():
    return {"Message": "Hello"}


#Заполняем таблицы


@app.get("/fake_users/{count}")
async def create_note(count: int):
    for i in range(count):
        query = users.insert().values(name=f'user{i}', surname=f'surname{i}', email=f'mail{i}@mail.ru', password=f'qwerty{i}')
        await database.execute(query)
    return {'message': f'{count} fake users create'}


@app.get("/fake_products/{count}")
async def create_note(count: int):
    for i in range(count):
        query = products.insert().values(product_name=f'product {i}', description=f'all about product {i}', price=(randint(1, 100000)))
        await database.execute(query)
    return {'message': f'{count} fake products create'}


@app.get("/fake_orders/{count}")
async def create_note(count: int):
    for i in range(count):
        query = orders.insert().values(user_id=randint(1, 20), product_id=randint(1, 20), status="created", date_time_orders=10000)
        await database.execute(query)
    return {'message': f'{count} fake orders create'}


#Читаем все из таблиц


@app.get("/users/", response_model=List[User])
async def read_users():
    query = users.select()
    return await database.fetch_all(query)


@app.get("/products/", response_model=List[Product])
async def read_products():
    query = products.select()
    return await database.fetch_all(query)


@app.get("/orders/", response_model=List[Order])
async def read_orders():
    query = orders.select()
    return await database.fetch_all(query)


#Читаем только то, что хотим


@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    query = users.select().where(users.c.user_id == user_id)
    user = await database.fetch_one(query)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.get("/products/{product_id}", response_model=Product)
async def read_product(product_id: int):
    query = products.select().where(products.c.product_id == product_id)
    product = await database.fetch_one(query)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@app.get("/orders/{order_id}", response_model=Order)
async def read_order(order_id: int):
    query = orders.select().where(orders.c.order_id == order_id)
    order = await database.fetch_one(query)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

#Меняем таблицы


@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, new_user: UserIn):
    query = users.update().where(users.c.user_id == user_id).values(**new_user.dict())
    await database.execute(query)
    return {**new_user.dict(), "id": user_id}


@app.put("/products/{product_id}", response_model=Product)
async def update_product(product_id: int, new_product: ProductIn):
    query = products.update().where(products.c.product_id == product_id).values(**new_product.dict())
    await database.execute(query)
    return {**new_product.dict(), "id": product_id}


@app.put("/orders/{order_id}", response_model=Order)
async def update_order(order_id: int, new_order: OrderIn):
    query = orders.update().where(orders.c.order_id == order_id).values(**new_order.dict())
    await database.execute(query)
    return {**new_order.dict(), "id": order_id}

#Удаляем таблицы


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = users.delete().where(users.c.user_id == user_id)
    await database.execute(query)
    return {'message': 'User deleted'}


@app.delete("/products/{product_id}")
async def delete_product(product_id: int):
    query = products.delete().where(products.c.product_id == product_id)
    await database.execute(query)
    return {'message': 'Product deleted'}


@app.delete("/orders/{order_id}")
async def delete_order(order_id: int):
    query = orders.delete().where(orders.c.order_id == order_id)
    await database.execute(query)
    return {'message': 'Order deleted'}