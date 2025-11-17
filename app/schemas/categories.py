from pydantic import BaseModel, Field


class BaseCategory(BaseModel):
    name: str = Field(..., description="分类名称", example="Lubricants")
    description: str = Field(None, description="分类描述", example="Lubricants category")
    icon: str = Field(None, description="分类图标")
    image_url: str | None = Field(None, description="分类图片URL")
    is_active: bool = Field(True, description="是否启用")
    order: int = Field(0, description="排序")


class CategoryCreate(BaseCategory):
    pass


class CategoryUpdate(BaseCategory):
    id: int

    def update_dict(self):
        return self.model_dump(exclude_unset=True, exclude={"id"})

