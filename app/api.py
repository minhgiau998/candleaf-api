from fastapi import FastAPI, HTTPException
from fastapi import responses
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.schemas.benefit import BenefitSchema
from app.schemas.hero import HeroSchema
from app.schemas.product import ProductSchema
from app.schemas.testimonial import TestimonialSchema

import json

app = FastAPI(
    title="Candleaf",
    description="Welcome to Candleaf API",
    version="1.0.0",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Rich Nguyen",
        "url": "https://github.com/minhgiau998",
        "email": "minhgiau04041998@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)


@app.get("/", include_in_schema=False)
def get_root() -> dict:
    return {"message": "Welcome to the candleaf api."}


# Benefit
@app.get("/benefit", status_code=200, tags=["Benefit"], response_model=BenefitSchema)
def get_all_benefits() -> dict:
    """
    Get all data of the benefits
    """
    f = open("app/db/benefits.json")
    data = json.load(f)
    f.close()
    return JSONResponse(jsonable_encoder(data))


# Hero
@app.get("/hero", status_code=200, tags=["Hero"], response_model=HeroSchema)
def get_all_heroes() -> dict:
    """
    Get all data of the heroes
    """
    f = open("app/db/heroes.json")
    data = json.load(f)
    f.close()
    return JSONResponse(jsonable_encoder(data))


# Product
@app.get("/product", status_code=200, tags=["Product"], response_model=ProductSchema)
def get_all_products() -> dict:
    """
    Get all data of the products
    """
    f = open("app/db/products.json")
    data = json.load(f)
    f.close()
    return JSONResponse(jsonable_encoder(data))


@app.get(
    "/product/{product_id}",
    status_code=200,
    tags=["Product"],
    response_model=ProductSchema,
)
def get_product(product_id: str) -> dict:
    """
    Get the product by id
    """
    f = open("app/db/products.json")
    data = json.load(f)
    f.close()
    result = [item for item in data if item["id"] == product_id]
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Product with ID {product_id} not found"
        )
    return JSONResponse(jsonable_encoder(result))


# Testimonial
@app.get(
    "/testimonial",
    status_code=200,
    tags=["Testimonial"],
    response_model=TestimonialSchema,
)
def get_all_testimonials() -> dict:
    """
    Get all data of the testimonials
    """
    f = open("app/db/testimonials.json")
    data = json.load(f)
    f.close()
    return JSONResponse(jsonable_encoder(data))
