from aptos_protos.aptos.transaction.v1 import transaction_pb2
from processors.coin_flip.models import RewardEvent
from typing import List
from utils.transactions_processor import ProcessingResult
from utils import general_utils
from utils.transactions_processor import TransactionsProcessor
from utils.models.schema_names import NFT_LOTTERY_SCHEMA
from utils.session import Session
from utils.processor_name import ProcessorName
import json
from datetime import datetime
from time import perf_counter

MODULE_ADDRESS = general_utils.standardize_address(
    "<>"
)


class NFTLotteryProcessor(TransactionsProcessor):
    def name(self) -> str:
        return ProcessorName.NFT_LOTTERY.value

    def schema(self) -> str:
        return NFT_LOTTERY_SCHEMA

    def process_transactions(
        self,
        transactions: list[transaction_pb2.Transaction],
        start_version: int,
        end_version: int,
    ) -> ProcessingResult:
        event_db_objs: List[RewardEvent] = []
        start_time = perf_counter()
        for transaction in transactions:
            # Custom filtering
            # Here we filter out all transactions that are not of type TRANSACTION_TYPE_USER
            if transaction.type != transaction_pb2.Transaction.TRANSACTION_TYPE_USER:
                continue

            # Parse Transaction struct
            transaction_version = transaction.version
            transaction_block_height = transaction.block_height
            transaction_timestamp = general_utils.parse_pb_timestamp(
                transaction.timestamp
            )
            user_transaction = transaction.user

            # Parse CoinFlipEvent struct
            for event_index, event in enumerate(user_transaction.events):
                # Skip events that don't match our filter criteria
                if not NFTLotteryProcessor.included_event_type(event.type_str):
                    continue

                reward_address = general_utils.standardize_address(
                    event.key.reward_address
                )

                data = json.loads(event.data)

                # Create an instance of RewardEvent
                event_db_obj = RewardEvent(
                    reward_address=reward_address
                )
                event_db_objs.append(event_db_obj)

        processing_duration_in_secs = perf_counter() - start_time
        start_time = perf_counter()
        self.insert_to_db(event_db_objs)
        db_insertion_duration_in_secs = perf_counter() - start_time
        return ProcessingResult(
            start_version=start_version,
            end_version=end_version,
            processing_duration_in_secs=processing_duration_in_secs,
            db_insertion_duration_in_secs=db_insertion_duration_in_secs,
        )

    def insert_to_db(self, parsed_objs: List[RewardEvent]) -> None:
        with Session() as session, session.begin():
            for obj in parsed_objs:
                session.merge(obj)

    @staticmethod
    def included_event_type(event_type: str) -> bool:
        parsed_tag = event_type.split("::")
        module_address = general_utils.standardize_address(parsed_tag[0])
        module_name = parsed_tag[1]
        event_type = parsed_tag[2]
        # Now we can filter out events that are not of type CoinFlipEvent
        # We can filter by the module address, module name, and event type
        # If someone deploys a different version of our contract with the same event type, we may want to index it one day.
        # So we could only check the event type instead of the full string
        # For our sake, check the full string
        return (
            module_address == MODULE_ADDRESS
            and module_name == "nft_lottery"
            and event_type == "RewardEvent"
        )
