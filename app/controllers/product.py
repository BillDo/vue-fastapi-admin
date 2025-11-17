from tortoise.expressions import Q

from app.core.crud import CRUDBase
from app.models.admin import Category, Product
from app.schemas.products import ProductCreate, ProductUpdate


class ProductController(CRUDBase[Product, ProductCreate, ProductUpdate]):
    def __init__(self):
        super().__init__(model=Product)

    async def list_products(self, page: int = 1, page_size: int = 10, name: str = None, category_id: int = None, category: str = None, is_active: bool = None):
        q = Q()
        if name:
            q &= Q(name__contains=name)
        if category_id:
            q &= Q(category_id=category_id)
        if category:
            q &= Q(category=category)
        if is_active is not None:
            q &= Q(is_active=is_active)
        else:
            # Default to only show active products for public
            q &= Q(is_active=True)
        
        total, products = await self.list(page=page, page_size=page_size, search=q, order=["order", "-id"])
        return total, products

    async def get_product_by_id(self, product_id: int):
        return await self.get(id=product_id)

    async def create_with_category(self, obj_in: ProductCreate):
        """Create product and set category name from category_id if provided"""
        if obj_in.category_id:
            category = await Category.get(id=obj_in.category_id)
            obj_in.category = category.name
        return await self.create(obj_in=obj_in)

    async def update_with_category(self, obj_in: ProductUpdate):
        """Update product and set category name from category_id if provided"""
        if obj_in.category_id:
            category = await Category.get(id=obj_in.category_id)
            obj_in.category = category.name
        product = await self.get(id=obj_in.id)
        product.update_from_dict(obj_in.update_dict())
        await product.save()
        return product


product_controller = ProductController()

