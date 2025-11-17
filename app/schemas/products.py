from typing import List, Optional

from pydantic import BaseModel, Field


class BaseProduct(BaseModel):
    name: str = Field(..., description="产品名称", example="Lubricants")
    description: Optional[str] = Field(None, description="产品描述", example="High-performance lubricants")
    category_id: Optional[int] = Field(None, description="产品分类ID", example=1)
    category: Optional[str] = Field(None, description="产品分类(兼容字段)", example="Lubricants")
    image_url: Optional[str] = Field(None, description="产品图片URL")
    features: Optional[List[str]] = Field(None, description="产品特性列表", example=["Industrial grade", "Long-lasting"])
    is_active: bool = Field(True, description="是否启用")
    order: int = Field(0, description="排序")


class ProductCreate(BaseProduct):
    pass


class ProductUpdate(BaseProduct):
    id: int

    def update_dict(self):
        return self.model_dump(exclude_unset=True, exclude={"id"})

