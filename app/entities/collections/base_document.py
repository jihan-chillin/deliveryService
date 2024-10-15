import dataclasses

from bson import ObjectId

# 모든 document의 조상 클래스
@dataclasses.dataclass(kw_only=True)
class BaseDocument:
    _id: ObjectId

    @property
    def id(self) -> ObjectId:
        return self._id