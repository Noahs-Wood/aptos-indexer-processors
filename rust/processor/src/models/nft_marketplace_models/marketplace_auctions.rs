// Copyright © Aptos Foundation

// Copyright (c) Aptos
// SPDX-License-Identifier: Apache-2.0

// This is required because a diesel macro makes clippy sad
#![allow(clippy::extra_unused_lifetimes)]
#![allow(clippy::unused_unit)]

use bigdecimal::BigDecimal;
use field_count::FieldCount;
use serde::{Deserialize, Serialize};

use crate::schema::current_nft_marketplace_auctions;

#[derive(Debug, Deserialize, FieldCount, Identifiable, Insertable, Serialize)]
#[diesel(primary_key(listing_id, token_data_id))]
#[diesel(table_name = current_nft_marketplace_auctions)]
pub struct MarketplaceAuction {
    pub listing_id: String,
    pub token_data_id: String,
    pub collection_id: String,
    pub fee_schedule_id: String,
    pub seller: String,
    pub current_bid_price: Option<BigDecimal>,
    pub current_bidder: Option<String>,
    pub starting_bid_price: BigDecimal,
    pub buy_it_now_price: Option<BigDecimal>,
    pub token_amount: BigDecimal,
    pub expiration_time: BigDecimal,
    pub is_deleted: bool,
    pub token_standard: String,
    pub coin_type: Option<String>,
    pub marketplace: String,
    pub contract_address: String,
    pub entry_function_id_str: String,
    pub last_transaction_version: i64,
    pub last_transaction_timestamp: chrono::NaiveDateTime,
}