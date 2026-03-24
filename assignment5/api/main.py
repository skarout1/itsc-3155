from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from .models import models, schemas
from .controllers import orders
from .dependencies.database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#ORDER...............................................................................................
@app.post("/orders/", response_model=schemas.Order, tags=["Orders"])
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return orders.create(db=db, order=order)


@app.get("/orders/", response_model=list[schemas.Order], tags=["Orders"])
def read_orders(db: Session = Depends(get_db)):
    return orders.read_all(db)


@app.get("/orders/{order_id}", response_model=schemas.Order, tags=["Orders"])
def read_one_order(order_id: int, db: Session = Depends(get_db)):
    order = orders.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return order


@app.put("/orders/{order_id}", response_model=schemas.Order, tags=["Orders"])
def update_one_order(order_id: int, order: schemas.OrderUpdate, db: Session = Depends(get_db)):
    order_db = orders.read_one(db, order_id=order_id)
    if order_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return orders.update(db=db, order=order, order_id=order_id)


@app.delete("/orders/{order_id}", tags=["Orders"])
def delete_one_order(order_id: int, db: Session = Depends(get_db)):
    order = orders.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return orders.delete(db=db, order_id=order_id)

#SANDWHCH...............................................................................................
@app.post("/sandwich/", response_model=schemas.Sandwich, tags=["Sandwichs"])
def create_sandwich(sandwich: schemas.SandwichCreate, db: Session = Depends(get_db)):
    return sandwich.create(db=db, sandwich=sandwich)





@app.delete("/sandwich/{sandwich_id}", tags=["Sandwichs"])
def delete_one_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    sandwich = sandwich.read_one(db, sandwich_id=sandwich_id)
    if sandwich is None:
        raise HTTPException(status_code=404, detail="User not found")
    return sandwich.delete(db=db, sandwich_id=sandwich_id)

#ORDER_DETAILS................................................................................
@app.post("/orderDetails/", response_model=schemas.OrderDetail, tags=["OrderDetail"])
def create_orderDetails(orderDetails: schemas.OrderDetailCreate, db: Session = Depends(get_db)):
    return orderDetails.create(db=db, orderDetails=orderDetails)



@app.delete("/orderDetails/{orderDetails_id}", tags=["OrderDetail"])
def delete_one_orderDetails(orderDetails_id: int, db: Session = Depends(get_db)):
    orderDetails = orderDetails.read_one(db, orderDetails_id=orderDetails_id)
    if orderDetails is None:
        raise HTTPException(status_code=404, detail="User not found")
    return orderDetails.delete(db=db, orderDetails_id=orderDetails_id)

#RECIPE........................................................................
@app.post("/recipes/", response_model=schemas.Recipe, tags=["Recipe"])
def create_recipes(recipes: schemas.RecipeCreate, db: Session = Depends(get_db)):
    return recipes.create(db=db, recipes=recipes)



@app.delete("/recipes/{recipes_id}", tags=["Recipe"])
def delete_one_recipes(recipes_id: int, db: Session = Depends(get_db)):
    recipes = recipes.read_one(db, recipes_id=recipes_id)
    if recipes is None:
        raise HTTPException(status_code=404, detail="User not found")
    return recipes.delete(db=db, recipes_id=recipes_id)

#RECOURCES.....................................................................
@app.post("/resources/", response_model=schemas.Resource, tags=["Resource"])
def create_resources(resources: schemas.ResourceCreate, db: Session = Depends(get_db)):
    return resources.create(db=db, resources=resources)



@app.delete("/resources/{resources_id}", tags=["Resource"])
def delete_one_resources(resources_id: int, db: Session = Depends(get_db)):
    resources = resources.read_one(db, resources_id=resources_id)
    if resources is None:
        raise HTTPException(status_code=404, detail="User not found")
    return resources.delete(db=db, resources_id=resources_id)