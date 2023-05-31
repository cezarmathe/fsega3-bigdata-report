#!/usr/bin/env bash

# scripts/prepare.sh
#
# Prepare original datasets for processing.
# This script fixes column lengths and removes unused rows and unused columns.

set -euxo pipefail

ORIGINAL_FILE="datasets/original.csv"
ORIGINAL_FIXED_FILE="datasets/original_fixed.csv"
INPUT_FILE="datasets/input.csv"
STATS_FILE="datasets/stats.csv"

# Fix column lengths so that xsv doesn't complain.
xsv fixlengths "${ORIGINAL_FILE}" > "${ORIGINAL_FIXED_FILE}"

# Create an index file - this should speed up processing.
xsv index "${ORIGINAL_FIXED_FILE}"

# Prepare the file:
#
# 1. Remove movies in Hindi.
# 2. Remove unused columns.
cat "${ORIGINAL_FIXED_FILE}" \
    | xsv search -i -s original_language en \
    | xsv select '!1,adult,original_language,backdrop_path,poster_path,video,cast,crew' \
    > "${INPUT_FILE}"

cat "${INPUT_FILE}" \
    | xsv select 'popularity,release_date,vote_average,vote_count,genres,keywords' \
    | xsv stats \
    | xsv select 'field,type,min,max,mean,stddev' \
    | xsv table \
    > "${STATS_FILE}"
