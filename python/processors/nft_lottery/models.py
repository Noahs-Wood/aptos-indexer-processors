from utils.models.annotated_types import StringType
from utils.models.annotated_types import (
    BooleanType,
    StringPrimaryKeyType,
    BigIntegerType,
    BigIntegerPrimaryKeyType,
    InsertedAtType,
    TimestampType,
    NumericType,
)
from utils.models.general_models import Base
from utils.models.schema_names import NFT_LOTTERY_SCHEMA


class RewardEvent(Base):
    __tablename__ = "reward_events"
    __table_args__ = ({"schema": NFT_LOTTERY_SCHEMA},)

    reward_address: StringPrimaryKeyType
