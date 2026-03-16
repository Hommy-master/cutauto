from fastapi import APIRouter
from src.schemas.create_draft import CreateDraftRequest, CreateDraftResponse
from src import service
import config


router = APIRouter(prefix="/v1", tags=["v1"])

@router.post(path="/create_draft", response_model=CreateDraftResponse)
def create_draft(cdr: CreateDraftRequest) -> CreateDraftResponse:
    """
    创建剪映草稿 (v1版本)
    """

    # 调用service层处理业务逻辑
    draft_url = service.create_draft(
        tpl_name=cdr.tpl_name
    )

    return CreateDraftResponse(draft_url=draft_url, tip_url=config.TIP_URL)

@router.post(path="/mashup688001", response_model=CreateDraftResponse)
def mashup688001() -> CreateDraftResponse:
    """
    使用688001模板创建剪映草稿
    """

    # 调用service层处理业务逻辑
    draft_url = service.create_draft(tpl_name="688001")

    return CreateDraftResponse(draft_url=draft_url, tip_url=config.TIP_URL)

