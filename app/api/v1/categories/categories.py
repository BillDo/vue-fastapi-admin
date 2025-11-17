from fastapi import APIRouter, Query

from app.controllers.category import category_controller
from app.i18n import t
from app.schemas import Success, SuccessExtra
from app.schemas.categories import CategoryCreate, CategoryUpdate

router = APIRouter()


@router.get("/list", summary=t("api.categories.list_summary"))
async def list_categories(
    page: int = Query(1, description=t("api.categories.page_description")),
    page_size: int = Query(
        100, description=t("api.categories.page_size_description")
    ),
    name: str = Query(None, description=t("api.categories.name_description")),
    is_active: bool = Query(
        None, description=t("api.categories.is_active_description")
    ),
):
    total, categories = await category_controller.list_categories(
        page=page, page_size=page_size, name=name, is_active=is_active
    )
    data = [await category.to_dict() for category in categories]
    return SuccessExtra(data=data, total=total, page=page, page_size=page_size)


@router.get("/active", summary=t("api.categories.active_summary"))
async def get_active_categories():
    """Get all active categories (for dropdowns and public site)"""
    categories = await category_controller.get_all_active_categories()
    data = [await category.to_dict() for category in categories]
    return Success(data=data)


@router.get("/get", summary=t("api.categories.get_summary"))
async def get_category(
    id: int = Query(..., description=t("api.categories.id_description")),
):
    category = await category_controller.get(id=id)
    data = await category.to_dict()
    return Success(data=data)


@router.post("/create", summary=t("api.categories.create_summary"))
async def create_category(
    category_in: CategoryCreate,
):
    await category_controller.create(obj_in=category_in)
    return Success(msg="Created Successfully")


@router.post("/update", summary=t("api.categories.update_summary"))
async def update_category(
    category_in: CategoryUpdate,
):
    await category_controller.update(id=category_in.id, obj_in=category_in)
    return Success(msg="Update Successfully")


@router.delete("/delete", summary=t("api.categories.delete_summary"))
async def delete_category(
    id: int = Query(..., description=t("api.categories.id_description")),
):
    await category_controller.remove(id=id)
    return Success(msg="Deleted Success")

