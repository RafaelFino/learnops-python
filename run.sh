#!/bin/bash
uvicorn app.main:app --reload --port 8081 --log-level trace
