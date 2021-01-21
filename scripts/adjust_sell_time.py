from hummingbot.script.script_base import ScriptBase
from hummingbot.core.event.events import (
    BuyOrderCompletedEvent,
    SellOrderCompletedEvent
)


class AdjustSellTime(ScriptBase):
    """
    Demonstrates how to set up a ping pong trading strategy which alternates buy and sell orders.
    If a buy order is filled, there will be one less buy order submitted at the next refresh cycle.
    If a sell order is filled, there will be one less sell order submitted at the next refresh cycle.
    The balance is positive if there are more completed buy orders than sell orders.
    """
    original_refresh_time = 0

    def __init__(self):
        super().__init__()

    def on_buy_order_completed(self, event: BuyOrderCompletedEvent):
        original_refresh_time = self.pmm_parameters.order_refresh_time
        self.pmm_parameters.order_refresh_time = 100000

    def on_sell_order_completed(self, event: SellOrderCompletedEvent):
        self.pmm_parameters.order_refresh_time = original_refresh_time


