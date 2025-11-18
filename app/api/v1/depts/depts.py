from fastapi import APIRouter, Query

from app.controllers.dept import dept_controller
from app.schemas import Success
from app.schemas.depts import *

router = APIRouter()


@router.get("/list", summary="View department list")
async def list_dept(
    name: str = Query(None, description="Department name"),
):
    dept_tree = await dept_controller.get_dept_tree(name)
    return Success(data=dept_tree)


@router.get("/get", summary="View department")
async def get_dept(
    id: int = Query(..., description="Department ID"),
):
    dept_obj = await dept_controller.get(id=id)
    data = await dept_obj.to_dict()
    return Success(data=data)


@router.post("/create", summary="Create department")
async def create_dept(
    dept_in: DeptCreate,
):
    await dept_controller.create_dept(obj_in=dept_in)
    return Success(msg="Created Successfully")


@router.post("/update", summary="Update department")
async def update_dept(
    dept_in: DeptUpdate,
):
    await dept_controller.update_dept(obj_in=dept_in)
    return Success(msg="Update Successfully")


@router.delete("/delete", summary="Delete department")
async def delete_dept(
    dept_id: int = Query(..., description="Department ID"),
):
    await dept_controller.delete_dept(dept_id=dept_id)
    return Success(msg="Deleted Successfully")