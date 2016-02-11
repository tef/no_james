#!/bin/bash
MARKDOWN="markdown_github-implicit_figures+header_attributes+yaml_metadata_block+inline_code_attributes+footnotes"
chmod +x ./filter.py
pandoc --from=$MARKDOWN --to $MARKDOWN --filter="./filter.py" "$@"
