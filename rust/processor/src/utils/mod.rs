// Copyright © Aptos Foundation
// SPDX-License-Identifier: Apache-2.0

use serde::{Deserialize, Serialize};

pub mod counters;
pub mod database;
pub mod util;

#[derive(Clone, Debug, Serialize, Deserialize)]
pub struct EventStreamMessage {
    pub sequence_number: i64,
    pub creation_number: i64,
    pub account_address: String,
    pub transaction_version: i64,
    pub transaction_block_height: i64,
    pub type_: String,
    pub data: serde_json::Value,
    pub event_index: i64,
    pub indexed_type: String,
    pub transaction_timestamp: chrono::NaiveDateTime,
}
