from typing import Optional

from tortoise.expressions import Q

from app.core.crud import CRUDBase
from app.models.admin import Category
from app.schemas.categories import CategoryCreate, CategoryUpdate


class CategoryController(CRUDBase[Category, CategoryCreate, CategoryUpdate]):
    def __init__(self):
        super().__init__(model=Category)

    async def list_categories(
        self,
        page: int = 1,
        page_size: int = 100,
        name: Optional[str] = None,
        is_active: Optional[bool] = None,
    ):
        q = Q()
        if name:
            q &= Q(name__contains=name)
        if is_active is not None:
            # Only filter by status if explicitly provided
            q &= Q(is_active=is_active)
        # If is_active is None, show all categories (for admin panel)

        total, categories = await self.list(
            page=page, page_size=page_size, search=q, order=["order", "name"]
        )
        return total, categories

    async def get_all_active_categories(self):
        """Get all active categories for dropdowns"""
        categories = await self.model.filter(is_active=True).order_by(
            "order", "name"
        ).all()
        return categories


category_controller = CategoryController()
