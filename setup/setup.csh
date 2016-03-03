#!/bin/tcsh
set sourced = ($_)
set setup_dir = `/usr/bin/dirname $sourced[2]`
set inst_dir = `\cd ${setup_dir}/..; \pwd -P`
setenv PYTHONPATH ${inst_dir}/python:${PYTHONPATH}
