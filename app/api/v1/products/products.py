from fastapi import APIRouter, Query

from app.controllers.product import product_controller
from app.i18n import t
from app.schemas import Success, SuccessExtra
from app.schemas.products import ProductCreate, ProductUpdate

router = APIRouter()


@router.get("/list", summary=t("api.products.list_summary"))
async def list_products(
    page: int = Query(1, description=t("api.products.page_description")),
    page_size: int = Query(10, description=t("api.products.page_size_description")),
    name: str = Query(None, description=t("api.products.name_description")),
    category_id: int = Query(None, description=t("api.products.category_id_description")),
    category: str = Query(None, description=t("api.products.category_description")),
    is_active: bool = Query(None, description=t("api.products.is_active_description")),
):
    total, products = await product_controller.list_products(
        page=page, page_size=page_size, name=name, category_id=category_id, category=category, is_active=is_active
    )
    data = [await product.to_dict() for product in products]
    return SuccessExtra(data=data, total=total, page=page, page_size=page_size)


@router.get("/get", summary=t("api.products.get_summary"))
async def get_product(
    id: int = Query(..., description=t("api.products.id_description")),
):
    product = await product_controller.get(id=id)
    data = await product.to_dict()
    return Success(data=data)


@router.post("/create", summary=t("api.products.create_summary"))
async def create_product(
    product_in: ProductCreate,
):
    await product_controller.create_with_category(obj_in=product_in)
    return Success(msg="Created Successfully")


@router.post("/update", summary=t("api.products.update_summary"))
async def update_product(
    product_in: ProductUpdate,
):
    await product_controller.update_with_category(obj_in=product_in)
    return Success(msg="Update Successfully")


@router.delete("/delete", summary=t("api.products.delete_summary"))
async def delete_product(
    id: int = Query(..., description=t("api.products.id_description")),
):
    await product_controller.delete(id=id)
    return Success(msg="Deleted Success")

