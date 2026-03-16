from pydantic import BaseModel, Field


class CreateDraftRequest(BaseModel):
    """创建草稿请求参数"""
    tpl_name: str = Field(default="", description="模板名称")

class CreateDraftResponse(BaseModel):
    """创建草稿响应参数"""
    draft_url: str = Field(default="", description="草稿URL")
    tip_url: str = Field(default="", description="草稿提示URL，获取帮助文档")
