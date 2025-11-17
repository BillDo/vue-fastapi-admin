from fastapi import APIRouter, Query

from app.controllers.dept import dept_controller
from app.i18n import t
from app.schemas import Success
from app.schemas.depts import DeptCreate, DeptUpdate

router = APIRouter()


@router.get("/list", summary=t("api.depts.list_summary"))
async def list_dept(
    name: str = Query(None, description=t("api.depts.name_description")),
):
    dept_tree = await dept_controller.get_dept_tree(name)
    return Success(data=dept_tree)


@router.get("/get", summary=t("api.depts.get_summary"))
async def get_dept(
    id: int = Query(..., description=t("api.depts.id_description")),
):
    dept_obj = await dept_controller.get(id=id)
    data = await dept_obj.to_dict()
    return Success(data=data)


@router.post("/create", summary=t("api.depts.create_summary"))
async def create_dept(
    dept_in: DeptCreate,
):
    await dept_controller.create_dept(obj_in=dept_in)
    return Success(msg="Created Successfully")


@router.post("/update", summary=t("api.depts.update_summary"))
async def update_dept(
    dept_in: DeptUpdate,
):
    await dept_controller.update_dept(obj_in=dept_in)
    return Success(msg="Update Successfully")


@router.delete("/delete", summary=t("api.depts.delete_summary"))
async def delete_dept(
    dept_id: int = Query(..., description=t("api.depts.id_description")),
):
    await dept_controller.delete_dept(dept_id=dept_id)
    return Success(msg="Deleted Success")
