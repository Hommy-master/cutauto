from urllib.parse import urlparse, parse_qs
import datetime
import uuid


def get_url_param(url: str, key: str, default=None):
    """
    从 URL 中提取指定查询参数的值（返回第一个值）。
    若参数不存在，返回 default。
    """
    query = parse_qs(urlparse(url).query)
    return query.get(key, [default])[0]

def gen_unique_id() -> str:
    """
    生成唯一ID
    """
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    unique_id = uuid.uuid4().hex[:8]

    return f"{timestamp}{unique_id}"