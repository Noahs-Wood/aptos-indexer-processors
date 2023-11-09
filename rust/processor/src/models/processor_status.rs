// Copyright © Aptos Foundation
// SPDX-License-Identifier: Apache-2.0

#![allow(clippy::extra_unused_lifetimes)]
use crate::{schemas::public::processor_status, utils::database::PgPoolConnection};
use diesel::{ExpressionMethods, OptionalExtension, QueryDsl};
use diesel_async::RunQueryDsl;

#[derive(AsChangeset, Debug, Insertable)]
#[diesel(table_name = processor_status)]
/// Only tracking the latest version successfully processed
pub struct ProcessorStatus {
    pub processor: String,
    pub last_success_version: i64,
}

#[derive(AsChangeset, Debug, Queryable)]
#[diesel(table_name = processor_status)]
/// Only tracking the latest version successfully processed
pub struct ProcessorStatusQuery {
    pub processor: String,
    pub last_success_version: i64,
    pub last_updated: chrono::NaiveDateTime,
}

impl ProcessorStatusQuery {
    pub async fn get_by_processor(
        processor_name: &str,
        conn: &mut PgPoolConnection<'_>,
    ) -> diesel::QueryResult<Option<Self>> {
        processor_status::table
            .filter(processor_status::processor.eq(processor_name))
            .first::<Self>(conn)
            .await
            .optional()
    }
}
